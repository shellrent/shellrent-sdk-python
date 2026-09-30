from __future__ import annotations

import asyncio
import logging
import threading
import time

import httpx
import pytest

from shellrent_sdk.auth import (
    ClientCredentials,
    MemoryTokenStore,
    OAuth2Auth,
    TokenError,
)
from tests.support import (
    API_URL,
    CLIENT_ID,
    CLIENT_SECRET,
    TOKEN_URL,
    FakeApi,
    FakeClock,
    body,
    credentials,
    error_response,
    form,
    health_response,
    token_response,
)


def sync_client(api: FakeApi, auth: OAuth2Auth) -> httpx.Client:
    return httpx.Client(base_url=API_URL, auth=auth, transport=api.transport())


def async_client(api: FakeApi, auth: OAuth2Auth) -> httpx.AsyncClient:
    return httpx.AsyncClient(base_url=API_URL, auth=auth, transport=api.transport())


class RecordingStore(MemoryTokenStore):
    def __init__(self) -> None:
        super().__init__()
        self.writes: list[tuple[str, str, int]] = []

    def set(self, key: str, value: str, ttl: int) -> None:
        self.writes.append((key, value, ttl))
        super().set(key, value, ttl)


class FailingStore:
    def get(self, key: str) -> str | None:
        raise OSError("read-only file system")

    def set(self, key: str, value: str, ttl: int) -> None:
        raise OSError("read-only file system")

    def delete(self, key: str) -> None:
        raise OSError("read-only file system")


# ClientCredentials


def test_credentials_derive_the_token_url_from_the_api_url() -> None:
    creds = ClientCredentials("id", "secret", api_url="https://api.staging.test/")

    assert creds.api_url == "https://api.staging.test"
    assert creds.token_url == "https://api.staging.test/oauth/token"
    assert ClientCredentials("id", "secret").token_url == "https://api.shellrent.com/oauth/token"


def test_credentials_keep_the_secret_out_of_repr() -> None:
    creds = credentials(scopes=["purchases:read"], audience="api-public")

    assert CLIENT_SECRET not in repr(creds)
    assert CLIENT_SECRET not in str(creds)
    assert "client-id" in repr(creds)
    assert creds.client_secret == CLIENT_SECRET


def test_credentials_treat_empty_scopes_as_all_scopes() -> None:
    assert credentials(scopes=[]).scopes is None
    assert credentials(scopes=("a", "b")).scopes == ("a", "b")


def test_credentials_reject_invalid_values() -> None:
    with pytest.raises(ValueError, match="must not be empty"):
        ClientCredentials("id", "")
    with pytest.raises(TypeError, match="not a string"):
        ClientCredentials("id", "secret", scopes="purchases:read")


def test_credentials_from_env(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("SHELLRENT_CLIENT_ID", "env-id")
    monkeypatch.setenv("SHELLRENT_CLIENT_SECRET", "env-secret")
    monkeypatch.setenv("SHELLRENT_SCOPES", " purchases:read, billing:read  shop:read ")
    monkeypatch.setenv("SHELLRENT_API_URL", "https://api.staging.test")

    creds = ClientCredentials.from_env()

    assert creds.client_id == "env-id"
    assert creds.client_secret == "env-secret"
    assert creds.scopes == ("purchases:read", "billing:read", "shop:read")
    assert creds.audience is None
    assert creds.token_url == "https://api.staging.test/oauth/token"


def test_credentials_from_env_with_defaults(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("SHELLRENT_CLIENT_ID", "env-id")
    monkeypatch.setenv("SHELLRENT_CLIENT_SECRET", "env-secret")
    monkeypatch.setenv("SHELLRENT_SCOPES", "")
    monkeypatch.delenv("SHELLRENT_API_URL", raising=False)

    creds = ClientCredentials.from_env()

    assert creds.scopes is None
    assert creds.api_url == "https://api.shellrent.com"


def test_credentials_from_env_require_id_and_secret(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("SHELLRENT_CLIENT_ID", "env-id")
    monkeypatch.delenv("SHELLRENT_CLIENT_SECRET", raising=False)

    with pytest.raises(ValueError, match="SHELLRENT_CLIENT_SECRET"):
        ClientCredentials.from_env()


# Token requests


def test_requests_a_token_and_sends_it() -> None:
    api = FakeApi(token_response("token-1"), health_response())

    with sync_client(api, OAuth2Auth(credentials())) as client:
        response = client.get("/api/health")

    assert response.status_code == 200
    token_request, api_request = api.requests
    assert token_request.method == "POST"
    assert str(token_request.url) == TOKEN_URL
    assert token_request.headers["Content-Type"] == "application/x-www-form-urlencoded"
    assert form(token_request) == {
        "grant_type": "client_credentials",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
    }
    assert "Authorization" not in token_request.headers
    assert api_request.headers["Authorization"] == "Bearer token-1"


def test_requests_the_given_scopes_and_audience() -> None:
    api = FakeApi(token_response(), health_response())
    creds = credentials(scopes=["purchases:read", "billing:read"], audience="api-internal")

    with sync_client(api, OAuth2Auth(creds)) as client:
        client.get("/api/health")

    assert form(api.token_requests[0])["scope"] == "purchases:read billing:read"
    assert form(api.token_requests[0])["audience"] == "api-internal"


def test_reuses_the_token_until_60_seconds_before_it_expires() -> None:
    clock = FakeClock()
    api = FakeApi(
        token_response("token-1", expires_in=600),
        health_response(),
        health_response(),
        token_response("token-2", expires_in=600),
        health_response(),
    )

    with sync_client(api, OAuth2Auth(credentials(), clock=clock)) as client:
        client.get("/api/health")
        clock.now += 539
        client.get("/api/health")
        clock.now += 1
        client.get("/api/health")

    assert len(api.token_requests) == 2
    assert [r.headers["Authorization"] for r in api.api_requests] == [
        "Bearer token-1",
        "Bearer token-1",
        "Bearer token-2",
    ]


def test_shares_the_token_through_the_store() -> None:
    store = MemoryTokenStore()
    api = FakeApi(token_response("token-1"), health_response(), health_response())

    with sync_client(api, OAuth2Auth(credentials(), store)) as client:
        client.get("/api/health")
    with sync_client(api, OAuth2Auth(credentials(), store)) as client:
        client.get("/api/health")

    assert len(api.token_requests) == 1
    assert api.api_requests[1].headers["Authorization"] == "Bearer token-1"


def test_keeps_the_tokens_of_different_scopes_apart() -> None:
    store = MemoryTokenStore()
    api = FakeApi(
        token_response("token-1"), health_response(), token_response("token-2"), health_response()
    )

    with sync_client(api, OAuth2Auth(credentials(scopes=["a"]), store)) as client:
        client.get("/api/health")
    with sync_client(api, OAuth2Auth(credentials(scopes=["b"]), store)) as client:
        client.get("/api/health")

    assert len(api.token_requests) == 2


def test_never_stores_the_secret() -> None:
    store = RecordingStore()
    api = FakeApi(token_response("token-1", expires_in=600), health_response())

    with sync_client(api, OAuth2Auth(credentials(), store)) as client:
        client.get("/api/health")

    [(key, value, ttl)] = store.writes
    assert ttl == 540
    assert "token-1" in value
    assert CLIENT_SECRET not in key
    assert CLIENT_SECRET not in value


def test_works_when_the_store_fails(caplog: pytest.LogCaptureFixture) -> None:
    api = FakeApi(token_response("token-1"), health_response(), health_response())

    with (
        caplog.at_level(logging.WARNING),
        sync_client(api, OAuth2Auth(credentials(), FailingStore())) as client,
    ):
        client.get("/api/health")
        client.get("/api/health")

    assert len(api.token_requests) == 1
    assert "read-only file system" in caplog.text


# 401


def test_retries_once_with_a_new_token_after_401() -> None:
    api = FakeApi(
        token_response("token-1"),
        error_response(401, "Token revoked"),
        token_response("token-2"),
        health_response(),
    )

    with sync_client(api, OAuth2Auth(credentials())) as client:
        response = client.get("/api/health")

    assert response.status_code == 200
    assert [r.headers["Authorization"] for r in api.api_requests] == [
        "Bearer token-1",
        "Bearer token-2",
    ]


def test_returns_the_second_401() -> None:
    api = FakeApi(
        token_response("token-1"),
        error_response(401, "Not authorized"),
        token_response("token-2"),
        error_response(401, "Not authorized"),
    )

    with sync_client(api, OAuth2Auth(credentials())) as client:
        response = client.get("/api/health")

    assert response.status_code == 401
    assert len(api.requests) == 4


def test_401_removes_the_token_from_the_store() -> None:
    store = MemoryTokenStore()
    api = FakeApi(
        token_response("token-1"),
        error_response(401, "Token revoked"),
        token_response("token-2"),
        health_response(),
        health_response(),
    )

    with sync_client(api, OAuth2Auth(credentials(), store)) as client:
        client.get("/api/health")
    # Another client, as another process would, finds the new token.
    with sync_client(api, OAuth2Auth(credentials(), store)) as client:
        client.get("/api/health")

    assert len(api.token_requests) == 2
    assert api.api_requests[-1].headers["Authorization"] == "Bearer token-2"


def test_sends_the_body_again_after_401() -> None:
    api = FakeApi(
        token_response("token-1"),
        error_response(401, "Expired"),
        token_response("token-2"),
        health_response(),
    )

    with sync_client(api, OAuth2Auth(credentials())) as client:
        client.post("/api/v3/orders/pay", json={"order_ids": [1]})

    first, second = api.api_requests
    assert body(first) == body(second) == {"order_ids": [1]}


# TokenError


def test_token_endpoint_errors_raise_token_error() -> None:
    api = FakeApi(
        httpx.Response(
            401,
            json={"error": "invalid_client", "error_description": "Client authentication failed"},
        )
    )

    with sync_client(api, OAuth2Auth(credentials())) as client, pytest.raises(TokenError) as info:
        client.get("/api/health")

    assert info.value.error == "invalid_client"
    assert info.value.error_description == "Client authentication failed"
    assert info.value.status_code == 401
    assert str(info.value) == (
        f"The token endpoint {TOKEN_URL} answered HTTP 401: invalid_client (Client authentication failed)"
    )
    assert CLIENT_SECRET not in str(info.value)
    assert len(api.api_requests) == 0


def test_token_error_for_the_rate_limit_of_the_token_endpoint() -> None:
    body = {"error": "rate_limited", "error_description": "Too many requests."}
    api = FakeApi(httpx.Response(429, json=body, headers={"Retry-After": "15"}))

    with sync_client(api, OAuth2Auth(credentials())) as client, pytest.raises(TokenError) as info:
        client.get("/api/health")

    assert info.value.status_code == 429
    assert info.value.error == "rate_limited"
    assert info.value.error_description == "Too many requests."
    assert str(info.value).endswith("answered HTTP 429: rate_limited (Too many requests.)")


def test_token_error_for_a_response_without_token() -> None:
    api = FakeApi(httpx.Response(200, json={"token_type": "Bearer"}))

    with sync_client(api, OAuth2Auth(credentials())) as client, pytest.raises(TokenError) as info:
        client.get("/api/health")

    assert info.value.error is None
    assert info.value.status_code == 200
    assert "without a valid access token" in str(info.value)


def test_token_error_for_a_response_that_is_not_json() -> None:
    api = FakeApi(httpx.Response(502, text="<html>Bad gateway</html>"))

    with sync_client(api, OAuth2Auth(credentials())) as client, pytest.raises(TokenError) as info:
        client.get("/api/health")

    assert info.value.status_code == 502
    assert info.value.error is None


# Async and concurrency


def test_works_with_the_async_client() -> None:
    api = FakeApi(
        token_response("token-1"),
        health_response(),
        error_response(401, "Token revoked"),
        token_response("token-2"),
        health_response(),
    )

    async def run() -> list[int]:
        async with async_client(api, OAuth2Auth(credentials())) as client:
            first = await client.get("/api/health")
            second = await client.get("/api/health")
            return [first.status_code, second.status_code]

    assert asyncio.run(run()) == [200, 200]
    assert [r.headers["Authorization"] for r in api.api_requests] == [
        "Bearer token-1",
        "Bearer token-1",
        "Bearer token-2",
    ]


def test_sync_and_async_clients_share_the_token() -> None:
    auth = OAuth2Auth(credentials())
    api = FakeApi(token_response("token-1"), health_response(), health_response())

    with sync_client(api, auth) as client:
        client.get("/api/health")

    async def run() -> None:
        async with async_client(api, auth) as client:
            await client.get("/api/health")

    asyncio.run(run())
    assert len(api.token_requests) == 1


def test_concurrent_tasks_request_a_single_token() -> None:
    token_requests = 0

    async def handler(request: httpx.Request) -> httpx.Response:
        nonlocal token_requests
        if str(request.url) == TOKEN_URL:
            token_requests += 1
            await asyncio.sleep(0.01)
            return token_response()
        return health_response()

    async def run() -> None:
        transport = httpx.MockTransport(handler)
        async with httpx.AsyncClient(
            base_url=API_URL, auth=OAuth2Auth(credentials()), transport=transport
        ) as client:
            await asyncio.gather(*(client.get("/api/health") for _ in range(10)))

    asyncio.run(run())
    assert token_requests == 1


def test_works_in_more_than_one_event_loop() -> None:
    clock = FakeClock()
    auth = OAuth2Auth(credentials(), clock=clock)

    async def handler(request: httpx.Request) -> httpx.Response:
        if str(request.url) == TOKEN_URL:
            await asyncio.sleep(0.01)
            return token_response()
        return health_response()

    async def run() -> list[int]:
        async with httpx.AsyncClient(
            base_url=API_URL, auth=auth, transport=httpx.MockTransport(handler)
        ) as client:
            responses = await asyncio.gather(*(client.get("/api/health") for _ in range(3)))
            return [response.status_code for response in responses]

    assert asyncio.run(run()) == [200] * 3
    clock.now += 600  # The next loop needs a new token, and waits on the lock again.
    assert asyncio.run(run()) == [200] * 3


def test_concurrent_threads_request_a_single_token() -> None:
    token_requests = 0
    counter_lock = threading.Lock()

    def handler(request: httpx.Request) -> httpx.Response:
        nonlocal token_requests
        if str(request.url) == TOKEN_URL:
            with counter_lock:
                token_requests += 1
            time.sleep(0.05)
            return token_response()
        return health_response()

    auth = OAuth2Auth(credentials())
    client = httpx.Client(base_url=API_URL, auth=auth, transport=httpx.MockTransport(handler))
    statuses: list[int] = []

    def call() -> None:
        statuses.append(client.get("/api/health").status_code)

    threads = [threading.Thread(target=call) for _ in range(8)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    client.close()

    assert statuses == [200] * 8
    assert token_requests == 1


# get_token


def test_get_token_uses_the_client_and_the_cache() -> None:
    api = FakeApi(token_response("token-1"))
    auth = OAuth2Auth(credentials())

    with httpx.Client(
        auth=auth, transport=api.transport(), headers={"User-Agent": "test-agent"}
    ) as client:
        assert auth.get_token(client) == "token-1"
        assert auth.get_token(client) == "token-1"

    [request] = api.requests
    assert request.headers["User-Agent"] == "test-agent"
    assert "Authorization" not in request.headers


def test_aget_token() -> None:
    api = FakeApi(token_response("token-1"))
    auth = OAuth2Auth(credentials())

    async def run() -> str:
        async with httpx.AsyncClient(auth=auth, transport=api.transport()) as client:
            await auth.aget_token(client)
            return await auth.aget_token(client)

    assert asyncio.run(run()) == "token-1"
    assert len(api.requests) == 1


def test_get_token_raises_token_error() -> None:
    api = FakeApi(httpx.Response(400, json={"error": "invalid_scope"}))
    auth = OAuth2Auth(credentials())

    with (
        httpx.Client(transport=api.transport()) as client,
        pytest.raises(TokenError, match="invalid_scope"),
    ):
        auth.get_token(client)
