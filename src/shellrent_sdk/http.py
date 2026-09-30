"""HTTP layer of the Shellrent SDKs: retries on 429 and the configuration of the httpx clients.

This module does not depend on the generated client: other SDKs, with clients of their own, use it too.
"""

from __future__ import annotations

import asyncio
import email.utils
import importlib.metadata
import logging
import threading
import time
import urllib.request
from collections.abc import Awaitable, Callable
from typing import Any, Final

import httpx

from .auth import ClientCredentials, OAuth2Auth, TokenStore

__all__ = [
    "MAX_RETRIES",
    "MAX_RETRY_DELAY",
    "RetryTransport",
    "client_args",
    "default_user_agent",
]

#: Retries of a request rejected with 429 Too Many Requests.
MAX_RETRIES: Final = 2

#: Longest wait, in seconds, before a retry: a longer Retry-After returns the 429 to the caller.
MAX_RETRY_DELAY: Final = 60.0

logger = logging.getLogger(__name__)


class RetryTransport(httpx.BaseTransport, httpx.AsyncBaseTransport):
    """Transport that retries the requests rejected with 429 Too Many Requests.

    It waits for the time given by ``Retry-After`` (seconds or HTTP date; 1 s, then 2 s, when the
    header is missing) and retries up to ``max_retries`` times; if the wait would be longer than
    ``max_delay`` seconds, or the retries are over, it returns the 429 response.

    It wraps a sync transport, for ``httpx.Client``, and an async one, for ``httpx.AsyncClient``, so
    the same instance can serve both, as the generated client requires.

    By default it sends the requests through ``httpx.HTTPTransport`` and ``httpx.AsyncHTTPTransport``
    that, like the default transports of an httpx client, follow the environment: the proxies of
    ``HTTP_PROXY``, ``HTTPS_PROXY`` and ``ALL_PROXY`` (or of the system settings on Windows and macOS),
    except for the hosts in ``NO_PROXY``, and the certificates of ``SSL_CERT_FILE`` and
    ``SSL_CERT_DIR``. The proxies are read when the transport is created; ``trust_env=False`` ignores
    the environment. Pass ``transport`` and ``async_transport`` to use transports of your own instead.
    """

    def __init__(
        self,
        transport: httpx.BaseTransport | None = None,
        async_transport: httpx.AsyncBaseTransport | None = None,
        *,
        trust_env: bool = True,
        max_retries: int = MAX_RETRIES,
        max_delay: float = MAX_RETRY_DELAY,
        sleep: Callable[[float], None] = time.sleep,
        async_sleep: Callable[[float], Awaitable[None]] = asyncio.sleep,
    ) -> None:
        self._transport = transport
        self._async_transport = async_transport
        self._trust_env = trust_env
        self._proxies = _environment_proxies() if trust_env else {}
        self._max_retries = max_retries
        self._max_delay = max_delay
        self._sleep = sleep
        self._async_sleep = async_sleep
        self._lock = threading.Lock()
        # Default transports, created on first use: one per proxy URL, None for no proxy.
        self._sync_transports: dict[str | None, httpx.HTTPTransport] = {}
        self._async_transports: dict[str | None, httpx.AsyncHTTPTransport] = {}

    def handle_request(self, request: httpx.Request) -> httpx.Response:
        transport = self._sync_transport(request.url)
        request.read()  # The body is sent again on retry.
        retries = 0
        while True:
            response = transport.handle_request(request)
            delay = self._retry_delay(response, retries)
            if delay is None:
                return response
            response.close()
            logger.info("%s %s: HTTP 429, retrying in %.1f s", request.method, request.url, delay)
            self._sleep(delay)
            retries += 1

    async def handle_async_request(self, request: httpx.Request) -> httpx.Response:
        transport = self._async_transport_for(request.url)
        await request.aread()  # The body is sent again on retry.
        retries = 0
        while True:
            response = await transport.handle_async_request(request)
            delay = self._retry_delay(response, retries)
            if delay is None:
                return response
            await response.aclose()
            logger.info("%s %s: HTTP 429, retrying in %.1f s", request.method, request.url, delay)
            await self._async_sleep(delay)
            retries += 1

    def close(self) -> None:
        if self._transport is not None:
            self._transport.close()
        with self._lock:
            transports = list(self._sync_transports.values())
            self._sync_transports.clear()
        for transport in transports:
            transport.close()

    async def aclose(self) -> None:
        if self._async_transport is not None:
            await self._async_transport.aclose()
        with self._lock:
            transports = list(self._async_transports.values())
            self._async_transports.clear()
        for transport in transports:
            await transport.aclose()

    def _sync_transport(self, url: httpx.URL) -> httpx.BaseTransport:
        if self._transport is not None:
            return self._transport
        proxy = self._proxy_for(url)
        with self._lock:
            transport = self._sync_transports.get(proxy)
            if transport is None:
                transport = httpx.HTTPTransport(trust_env=self._trust_env, proxy=_proxy(proxy))
                self._sync_transports[proxy] = transport
            return transport

    def _async_transport_for(self, url: httpx.URL) -> httpx.AsyncBaseTransport:
        if self._async_transport is not None:
            return self._async_transport
        proxy = self._proxy_for(url)
        with self._lock:
            transport = self._async_transports.get(proxy)
            if transport is None:
                transport = httpx.AsyncHTTPTransport(trust_env=self._trust_env, proxy=_proxy(proxy))
                self._async_transports[proxy] = transport
            return transport

    def _proxy_for(self, url: httpx.URL) -> str | None:
        """URL of the proxy for a request to ``url``, or None to connect directly."""
        proxy = self._proxies.get(url.scheme) or self._proxies.get("all")
        if proxy is None:
            return None
        host = url.host
        if url.port is not None and ":" not in host:  # Not for IPv6 addresses.
            host = f"{host}:{url.port}"
        return None if urllib.request.proxy_bypass(host) else proxy

    def _retry_delay(self, response: httpx.Response, retries: int) -> float | None:
        """Seconds to wait before retrying the request, or None to return the response."""
        if response.status_code != 429 or retries >= self._max_retries:
            return None
        delay = _retry_after(response.headers.get("Retry-After", ""))
        if delay is None:
            delay = float(2**retries)
        return delay if delay <= self._max_delay else None


def default_user_agent() -> str:
    """``shellrent-sdk-python/<version>``, with the installed version of the package."""
    return f"shellrent-sdk-python/{_package_version()}"


def client_args(
    credentials: ClientCredentials,
    *,
    token_store: TokenStore | None = None,
    retry: bool = True,
    timeout: float | httpx.Timeout | None = 30.0,
    user_agent: str | None = None,
) -> dict[str, Any]:
    """Keyword arguments for ``httpx.Client`` and ``httpx.AsyncClient`` that call the Shellrent APIs.

    They set ``base_url`` (the API URL of the credentials), ``auth`` (an ``OAuth2Auth``),
    ``transport`` (a ``RetryTransport``, unless ``retry`` is false), the ``User-Agent`` header
    (default: ``default_user_agent()``) and ``timeout``.

    A generated client takes ``base_url``, ``headers`` and ``timeout`` as arguments of its own and
    the rest as ``httpx_args``.

    Args:
        token_store: Cache of the access token; default a new ``MemoryTokenStore``.
    """
    args: dict[str, Any] = {
        "base_url": credentials.api_url,
        "auth": OAuth2Auth(credentials, token_store),
        "headers": {"User-Agent": user_agent or default_user_agent()},
        "timeout": httpx.Timeout(timeout),
    }
    if retry:
        args["transport"] = RetryTransport()
    return args


def _package_version() -> str:
    try:
        return importlib.metadata.version("shellrent-sdk")
    except importlib.metadata.PackageNotFoundError:
        return "unknown"


def _environment_proxies() -> dict[str, str]:
    """Proxies by URL scheme ("http", "https" and "all" for any), as httpx reads them."""
    proxies = urllib.request.getproxies()
    return {
        scheme: url if "://" in url else f"http://{url}"
        for scheme in ("http", "https", "all")
        if (url := proxies.get(scheme))
    }


def _proxy(url: str | None) -> httpx.Proxy | None:
    return httpx.Proxy(url) if url is not None else None


def _retry_after(value: str) -> float | None:
    """Seconds given by a Retry-After header: a number of seconds or an HTTP date."""
    value = value.strip()
    if value.isascii() and value.isdigit():
        return float(value)
    if not value:
        return None
    try:
        date = email.utils.parsedate_to_datetime(value)
    except (TypeError, ValueError):
        return None
    return max(0.0, date.timestamp() - time.time())
