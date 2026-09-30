"""RetryTransport follows the proxy and certificate settings of the environment, as httpx does."""

from __future__ import annotations

import asyncio
import shutil
from collections.abc import Iterator
from pathlib import Path

import httpx
import pytest

from shellrent_sdk.auth import ClientCredentials
from shellrent_sdk.http import RetryTransport, client_args
from tests.servers import CA_FILE, CA_HASH_NAME, Server, proxy_server, tls_server

ENVIRONMENT = [
    "HTTP_PROXY",
    "HTTPS_PROXY",
    "ALL_PROXY",
    "NO_PROXY",
    "SSL_CERT_FILE",
    "SSL_CERT_DIR",
    "REQUEST_METHOD",
]

#: A port where nothing listens: a request sent there fails.
CLOSED = "http://127.0.0.1:9"


@pytest.fixture(autouse=True)
def clean_environment(monkeypatch: pytest.MonkeyPatch) -> None:
    for name in ENVIRONMENT:
        monkeypatch.delenv(name, raising=False)
        monkeypatch.delenv(name.lower(), raising=False)


@pytest.fixture
def proxy() -> Iterator[Server]:
    with proxy_server() as server:
        yield server


@pytest.fixture
def https() -> Iterator[Server]:
    with tls_server() as server:
        yield server


def get(url: str, transport: RetryTransport) -> httpx.Response:
    with httpx.Client(transport=transport) as client:
        return client.get(url)


def target(response: httpx.Response) -> str:
    """The request target seen by the proxy."""
    return str(response.json()["data"]["target"])


# Proxies


def test_uses_http_proxy(monkeypatch: pytest.MonkeyPatch, proxy: Server) -> None:
    monkeypatch.setenv("HTTP_PROXY", proxy.url)

    response = get("http://api.example.test/api/health", RetryTransport())

    assert target(response) == "http://api.example.test/api/health"


def test_uses_all_proxy(monkeypatch: pytest.MonkeyPatch, proxy: Server) -> None:
    monkeypatch.setenv("all_proxy", proxy.url)

    response = get("http://api.example.test/api/health", RetryTransport())

    assert target(response) == "http://api.example.test/api/health"


def test_accepts_proxies_without_scheme(monkeypatch: pytest.MonkeyPatch, proxy: Server) -> None:
    monkeypatch.setenv("HTTP_PROXY", f"127.0.0.1:{proxy.port}")

    response = get("http://api.example.test/api/health", RetryTransport())

    assert target(response) == "http://api.example.test/api/health"


def test_uses_https_proxy_with_ssl_cert_file(
    monkeypatch: pytest.MonkeyPatch, proxy: Server, https: Server
) -> None:
    monkeypatch.setenv("HTTPS_PROXY", proxy.url)
    monkeypatch.setenv("HTTP_PROXY", CLOSED)
    monkeypatch.setenv("SSL_CERT_FILE", str(CA_FILE))

    response = get(f"https://localhost:{https.port}/api/health", RetryTransport())

    assert response.text == "hello"
    assert proxy.requests == [f"CONNECT localhost:{https.port}"]


def test_no_proxy_skips_the_proxy(monkeypatch: pytest.MonkeyPatch, proxy: Server) -> None:
    monkeypatch.setenv("HTTP_PROXY", CLOSED)
    monkeypatch.setenv("NO_PROXY", "example.org, 127.0.0.1")

    response = get(f"{proxy.url}/api/health", RetryTransport())

    assert target(response) == "/api/health"


def test_no_proxy_star_skips_every_proxy(monkeypatch: pytest.MonkeyPatch, proxy: Server) -> None:
    monkeypatch.setenv("ALL_PROXY", CLOSED)
    monkeypatch.setenv("NO_PROXY", "*")

    response = get(f"{proxy.url}/api/health", RetryTransport())

    assert target(response) == "/api/health"


def test_uses_the_proxy_for_async_requests(monkeypatch: pytest.MonkeyPatch, proxy: Server) -> None:
    monkeypatch.setenv("HTTP_PROXY", proxy.url)
    transport = RetryTransport()

    async def run() -> httpx.Response:
        async with httpx.AsyncClient(transport=transport) as client:
            return await client.get("http://api.example.test/api/health")

    assert target(asyncio.run(run())) == "http://api.example.test/api/health"


def test_the_sdk_clients_use_the_proxy(monkeypatch: pytest.MonkeyPatch, proxy: Server) -> None:
    monkeypatch.setenv("HTTP_PROXY", proxy.url)
    credentials = ClientCredentials("client-id", "secret", api_url="http://api.example.test")

    with httpx.Client(**client_args(credentials)) as client:
        response = client.get("/api/v3/purchases")

    assert target(response) == "http://api.example.test/api/v3/purchases"
    assert proxy.requests == [
        "POST http://api.example.test/oauth/token",
        "GET http://api.example.test/api/v3/purchases",
    ]


def test_trust_env_false_ignores_the_proxies(
    monkeypatch: pytest.MonkeyPatch, proxy: Server
) -> None:
    monkeypatch.setenv("HTTP_PROXY", CLOSED)

    response = get(f"{proxy.url}/api/health", RetryTransport(trust_env=False))

    assert target(response) == "/api/health"


def test_transports_of_your_own_are_used_as_they_are(
    monkeypatch: pytest.MonkeyPatch, proxy: Server
) -> None:
    monkeypatch.setenv("HTTP_PROXY", CLOSED)

    response = get(f"{proxy.url}/api/health", RetryTransport(httpx.HTTPTransport()))

    assert target(response) == "/api/health"


# Certificates


def test_trusts_the_certificates_of_ssl_cert_file(
    monkeypatch: pytest.MonkeyPatch, https: Server
) -> None:
    monkeypatch.setenv("SSL_CERT_FILE", str(CA_FILE))

    assert get(f"https://localhost:{https.port}/", RetryTransport()).text == "hello"


def test_trusts_the_certificates_of_ssl_cert_dir(
    monkeypatch: pytest.MonkeyPatch, https: Server, tmp_path: Path
) -> None:
    shutil.copy(CA_FILE, tmp_path / CA_HASH_NAME)
    monkeypatch.setenv("SSL_CERT_DIR", str(tmp_path))

    assert get(f"https://localhost:{https.port}/", RetryTransport()).text == "hello"


def test_trusts_the_certificates_of_ssl_cert_file_in_async_requests(
    monkeypatch: pytest.MonkeyPatch, https: Server
) -> None:
    monkeypatch.setenv("SSL_CERT_FILE", str(CA_FILE))
    transport = RetryTransport()

    async def run() -> str:
        async with httpx.AsyncClient(transport=transport) as client:
            return (await client.get(f"https://localhost:{https.port}/")).text

    assert asyncio.run(run()) == "hello"


def test_rejects_unknown_certificates(https: Server) -> None:
    with pytest.raises(httpx.ConnectError, match="CERTIFICATE_VERIFY_FAILED"):
        get(f"https://localhost:{https.port}/", RetryTransport())


def test_trust_env_false_ignores_ssl_cert_file(
    monkeypatch: pytest.MonkeyPatch, https: Server
) -> None:
    monkeypatch.setenv("SSL_CERT_FILE", str(CA_FILE))

    with pytest.raises(httpx.ConnectError, match="CERTIFICATE_VERIFY_FAILED"):
        get(f"https://localhost:{https.port}/", RetryTransport(trust_env=False))
