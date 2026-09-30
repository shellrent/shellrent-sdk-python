"""Fakes shared by the tests: the API behind an httpx.MockTransport, a clock, a sleep that does not sleep."""

from __future__ import annotations

import json
from typing import Any

import httpx

from shellrent_sdk.auth import ClientCredentials

CLIENT_ID = "client-id"
CLIENT_SECRET = "s3cr3t-never-shown"
API_URL = "https://api.test"
TOKEN_URL = f"{API_URL}/oauth/token"


def credentials(**kwargs: Any) -> ClientCredentials:
    return ClientCredentials(CLIENT_ID, CLIENT_SECRET, api_url=API_URL, **kwargs)


def token_response(access_token: str = "token-1", expires_in: int = 600) -> httpx.Response:
    return httpx.Response(
        200,
        json={
            "access_token": access_token,
            "token_type": "Bearer",
            "expires_in": expires_in,
            "scope": "purchases:read",
            "audience": "api-public",
        },
    )


def json_response(status: int = 200, data: Any = None, **kwargs: Any) -> httpx.Response:
    body = {"error": 0 if status < 400 else status, "message": "", "data": data or {}, "meta": None}
    return httpx.Response(status, json=body, **kwargs)


def health_response() -> httpx.Response:
    return json_response(200, {"status": "ok"})


def error_response(status: int, message: str, **kwargs: Any) -> httpx.Response:
    """An error response as the API sends it, with data and meta null."""
    body = {"error": status, "message": message, "data": None, "meta": None}
    return httpx.Response(status, json=body, **kwargs)


class FakeApi:
    """Handler of an httpx.MockTransport: answers with the given responses, in order."""

    def __init__(self, *responses: httpx.Response) -> None:
        self.responses = list(responses)
        self.requests: list[httpx.Request] = []

    def __call__(self, request: httpx.Request) -> httpx.Response:
        # A copy: the request sent again after a 401 is the same object, with another token.
        self.requests.append(
            httpx.Request(
                request.method, request.url, headers=request.headers.copy(), content=request.read()
            )
        )
        if not self.responses:
            raise AssertionError(f"Unexpected request: {request.method} {request.url}")
        return self.responses.pop(0)

    @property
    def token_requests(self) -> list[httpx.Request]:
        return [request for request in self.requests if str(request.url) == TOKEN_URL]

    @property
    def api_requests(self) -> list[httpx.Request]:
        return [request for request in self.requests if str(request.url) != TOKEN_URL]

    def transport(self) -> httpx.MockTransport:
        return httpx.MockTransport(self)


def form(request: httpx.Request) -> dict[str, str]:
    """The form-urlencoded body of a request."""
    return dict(httpx.QueryParams(request.content.decode()))


def body(request: httpx.Request) -> Any:
    return json.loads(request.content)


class FakeClock:
    def __init__(self, now: float = 1_000_000.0) -> None:
        self.now = now

    def __call__(self) -> float:
        return self.now


class Sleeps:
    """Records the waits instead of sleeping, sync or async."""

    def __init__(self) -> None:
        self.delays: list[float] = []

    def sleep(self, delay: float) -> None:
        self.delays.append(delay)

    async def async_sleep(self, delay: float) -> None:
        self.delays.append(delay)
