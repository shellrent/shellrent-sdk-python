from __future__ import annotations

import asyncio
import email.utils
import importlib.metadata
import time
from typing import Any

import httpx
import pytest

from shellrent_sdk.auth import OAuth2Auth
from shellrent_sdk.http import RetryTransport, client_args, default_user_agent
from tests.support import (
    API_URL,
    TOKEN_URL,
    FakeApi,
    Sleeps,
    body,
    credentials,
    error_response,
    health_response,
    token_response,
)


def too_many_requests(retry_after: str | None = None) -> httpx.Response:
    headers = {"Retry-After": retry_after} if retry_after is not None else {}
    return error_response(429, "Too Many Requests", headers=headers)


def retrying_client(api: FakeApi, sleeps: Sleeps, **kwargs: Any) -> httpx.Client:
    transport = RetryTransport(api.transport(), sleep=sleeps.sleep, **kwargs)
    return httpx.Client(base_url=API_URL, transport=transport)


# RetryTransport


def test_retries_after_the_time_given_by_retry_after() -> None:
    api, sleeps = FakeApi(too_many_requests("3"), health_response()), Sleeps()

    with retrying_client(api, sleeps) as client:
        response = client.get("/api/health")

    assert response.status_code == 200
    assert sleeps.delays == [3.0]
    assert len(api.requests) == 2


def test_retries_twice_at_most() -> None:
    api, sleeps = (
        FakeApi(too_many_requests("1"), too_many_requests("1"), too_many_requests("1")),
        Sleeps(),
    )

    with retrying_client(api, sleeps) as client:
        response = client.get("/api/health")

    assert response.status_code == 429
    assert response.headers["Retry-After"] == "1"
    assert response.json()["message"] == "Too Many Requests"
    assert sleeps.delays == [1.0, 1.0]
    assert len(api.requests) == 3


def test_waits_1_then_2_seconds_without_retry_after() -> None:
    api, sleeps = FakeApi(too_many_requests(), too_many_requests(), health_response()), Sleeps()

    with retrying_client(api, sleeps) as client:
        response = client.get("/api/health")

    assert response.status_code == 200
    assert sleeps.delays == [1.0, 2.0]


def test_accepts_retry_after_as_http_date() -> None:
    date = email.utils.formatdate(time.time() + 30, usegmt=True)
    api, sleeps = FakeApi(too_many_requests(date), health_response()), Sleeps()

    with retrying_client(api, sleeps) as client:
        client.get("/api/health")

    [delay] = sleeps.delays
    assert 28 <= delay <= 30


def test_gives_up_when_retry_after_is_longer_than_60_seconds() -> None:
    api, sleeps = FakeApi(too_many_requests("61")), Sleeps()

    with retrying_client(api, sleeps) as client:
        response = client.get("/api/health")

    assert response.status_code == 429
    assert sleeps.delays == []


def test_limits_can_be_changed() -> None:
    api, sleeps = FakeApi(too_many_requests("5"), too_many_requests("5")), Sleeps()

    with retrying_client(api, sleeps, max_retries=1, max_delay=10) as client:
        response = client.get("/api/health")

    assert response.status_code == 429
    assert sleeps.delays == [5.0]


def test_does_not_retry_other_errors() -> None:
    api, sleeps = (
        FakeApi(error_response(503, "Unavailable", headers={"Retry-After": "1"})),
        Sleeps(),
    )

    with retrying_client(api, sleeps) as client:
        response = client.get("/api/health")

    assert response.status_code == 503
    assert sleeps.delays == []


def test_sends_the_body_again() -> None:
    api, sleeps = FakeApi(too_many_requests("1"), health_response()), Sleeps()

    with retrying_client(api, sleeps) as client:
        client.post("/api/v3/orders/pay", json={"order_ids": [1, 2]})

    assert [body(request) for request in api.requests] == [{"order_ids": [1, 2]}] * 2


def test_retries_async_requests() -> None:
    api, sleeps = FakeApi(too_many_requests("2"), too_many_requests(), health_response()), Sleeps()
    transport = RetryTransport(async_transport=api.transport(), async_sleep=sleeps.async_sleep)

    async def run() -> int:
        async with httpx.AsyncClient(base_url=API_URL, transport=transport) as client:
            return (await client.get("/api/health")).status_code

    assert asyncio.run(run()) == 200
    assert sleeps.delays == [2.0, 2.0]


def test_the_same_transport_serves_sync_and_async_clients() -> None:
    api = FakeApi(health_response(), health_response())
    transport = RetryTransport(api.transport(), api.transport())

    with httpx.Client(base_url=API_URL, transport=transport) as client:
        client.get("/api/health")

    async def run() -> None:
        async with httpx.AsyncClient(base_url=API_URL, transport=transport) as client:
            await client.get("/api/health")

    asyncio.run(run())
    assert len(api.requests) == 2


def test_retries_the_token_endpoint_too() -> None:
    api, sleeps = FakeApi(too_many_requests("4"), token_response(), health_response()), Sleeps()
    transport = RetryTransport(api.transport(), sleep=sleeps.sleep)

    with httpx.Client(
        base_url=API_URL, auth=OAuth2Auth(credentials()), transport=transport
    ) as client:
        response = client.get("/api/health")

    assert response.status_code == 200
    assert sleeps.delays == [4.0]
    assert [str(r.url) for r in api.requests] == [TOKEN_URL, TOKEN_URL, f"{API_URL}/api/health"]


# client_args


def test_client_args() -> None:
    args = client_args(credentials(), timeout=12)

    assert args["base_url"] == API_URL
    assert isinstance(args["auth"], OAuth2Auth)
    assert isinstance(args["transport"], RetryTransport)
    assert args["headers"] == {"User-Agent": default_user_agent()}
    assert args["timeout"] == httpx.Timeout(12)


def test_client_args_without_retry() -> None:
    args = client_args(credentials(), retry=False, user_agent="internal-sdk/1.0")

    assert "transport" not in args
    assert args["headers"] == {"User-Agent": "internal-sdk/1.0"}
    assert args["timeout"] == httpx.Timeout(30.0)


def test_user_agent_has_the_package_version() -> None:
    version = importlib.metadata.version("shellrent-sdk")
    assert default_user_agent() == f"shellrent-sdk-python/{version}"


@pytest.mark.parametrize("client_class", [httpx.Client, httpx.AsyncClient])
def test_clients_send_user_agent_and_timeout_to_the_token_endpoint_too(
    client_class: type[httpx.Client | httpx.AsyncClient],
) -> None:
    api = FakeApi(token_response(), health_response())
    args = client_args(credentials(), timeout=7)
    args["transport"] = RetryTransport(api.transport(), api.transport())
    timeouts: list[Any] = []

    def record_timeout(request: httpx.Request) -> None:
        timeouts.append(request.extensions.get("timeout"))

    if client_class is httpx.Client:
        with httpx.Client(**args, event_hooks={"request": [record_timeout]}) as client:
            client.get("/api/health")
    else:

        async def record_timeout_async(request: httpx.Request) -> None:
            record_timeout(request)

        async def run() -> None:
            async with httpx.AsyncClient(
                **args, event_hooks={"request": [record_timeout_async]}
            ) as client:
                await client.get("/api/health")

        asyncio.run(run())

    assert [r.headers["User-Agent"] for r in api.requests] == [default_user_agent()] * 2
    assert timeouts == [httpx.Timeout(7).as_dict()] * 2
