"""OAuth2 client credentials authentication for the Shellrent APIs.

This module does not depend on the generated client: other SDKs, with clients of their own, use it too.
"""

from __future__ import annotations

import asyncio
import contextlib
import hashlib
import json
import logging
import os
import re
import tempfile
import threading
import time
import weakref
from collections.abc import AsyncGenerator, Callable, Generator, Iterable, Iterator, Mapping
from pathlib import Path
from typing import Any, Final, NamedTuple, Protocol

import httpx

__all__ = [
    "DEFAULT_API_URL",
    "EXPIRY_MARGIN",
    "ClientCredentials",
    "FileTokenStore",
    "MemoryTokenStore",
    "OAuth2Auth",
    "TokenError",
    "TokenStore",
]

DEFAULT_API_URL: Final = "https://api.shellrent.com"

#: Seconds before its expiry after which an access token is no longer used.
EXPIRY_MARGIN: Final = 60

logger = logging.getLogger(__name__)


class ClientCredentials:
    """OAuth2 client credentials of a Shellrent API client.

    Args:
        client_id: ID of the API client.
        client_secret: Secret of the API client. It is never cached and never shown by ``repr()``.
        scopes: Scopes to request; ``None`` (or an empty list) lets the server grant every scope
            of the client.
        audience: Audience to request; ``None`` lets the server use the only audience of the client.
        api_url: Base URL of the API, to change only to use another environment such as staging.
        token_url: Token endpoint; ``None`` means ``{api_url}/oauth/token``.
    """

    def __init__(
        self,
        client_id: str,
        client_secret: str,
        *,
        scopes: Iterable[str] | None = None,
        audience: str | None = None,
        api_url: str = DEFAULT_API_URL,
        token_url: str | None = None,
    ) -> None:
        if not client_id or not client_secret:
            raise ValueError("The client ID and the client secret must not be empty.")
        if isinstance(scopes, str):
            raise TypeError("scopes must be a list of strings, not a string.")

        scope_list = tuple(scopes or ())
        api_url = api_url.rstrip("/")

        self.client_id: Final = client_id
        self._client_secret = client_secret
        self.scopes: Final = scope_list or None
        self.audience: Final = audience
        self.api_url: Final = api_url
        self.token_url: Final = token_url or f"{api_url}/oauth/token"

    @classmethod
    def from_env(cls) -> ClientCredentials:
        """Reads the credentials from the environment.

        ``SHELLRENT_CLIENT_ID`` and ``SHELLRENT_CLIENT_SECRET`` are required; ``SHELLRENT_SCOPES``
        (separated by spaces or commas) and ``SHELLRENT_API_URL`` are optional.

        Raises:
            ValueError: The client ID or the client secret is not set.
        """
        client_id = _env("SHELLRENT_CLIENT_ID")
        client_secret = _env("SHELLRENT_CLIENT_SECRET")
        if client_id is None or client_secret is None:
            raise ValueError(
                "The SHELLRENT_CLIENT_ID and SHELLRENT_CLIENT_SECRET environment variables must be set."
            )

        scopes = _env("SHELLRENT_SCOPES")
        return cls(
            client_id,
            client_secret,
            scopes=[scope for scope in re.split(r"[\s,]+", scopes) if scope] if scopes else None,
            api_url=_env("SHELLRENT_API_URL") or DEFAULT_API_URL,
        )

    @property
    def client_secret(self) -> str:
        return self._client_secret

    def __repr__(self) -> str:
        return (
            f"{type(self).__name__}(client_id={self.client_id!r}, scopes={self.scopes!r}, "
            f"audience={self.audience!r}, api_url={self.api_url!r}, token_url={self.token_url!r})"
        )


class TokenError(Exception):
    """The token endpoint did not issue an access token.

    Attributes:
        error: OAuth2 error code, such as ``invalid_client`` or ``invalid_scope``, if any.
        error_description: OAuth2 error description, if any.
        status_code: HTTP status of the response of the token endpoint.
    """

    def __init__(
        self,
        message: str,
        *,
        error: str | None = None,
        error_description: str | None = None,
        status_code: int,
    ) -> None:
        super().__init__(message)
        self.error = error
        self.error_description = error_description
        self.status_code = status_code


class TokenStore(Protocol):
    """Cache of access tokens, shared by the clients (and the processes) that use it.

    The semantics are those of PSR-16 and of Django's cache: ``get`` returns ``None`` for missing
    and expired keys, ``set`` stores a value for ``ttl`` seconds, ``delete`` ignores missing keys.
    Values are opaque strings; the client secret is never stored.
    """

    def get(self, key: str, /) -> str | None: ...

    def set(self, key: str, value: str, ttl: int, /) -> object: ...

    def delete(self, key: str, /) -> object: ...


class MemoryTokenStore:
    """Keeps the tokens in memory, for the life of the process."""

    def __init__(self, *, clock: Callable[[], float] = time.monotonic) -> None:
        self._clock = clock
        self._items: dict[str, tuple[str, float]] = {}
        self._lock = threading.Lock()

    def get(self, key: str) -> str | None:
        with self._lock:
            item = self._items.get(key)
            if item is None:
                return None
            if item[1] <= self._clock():
                del self._items[key]
                return None
            return item[0]

    def set(self, key: str, value: str, ttl: int) -> None:
        with self._lock:
            if ttl > 0:
                self._items[key] = (value, self._clock() + ttl)
            else:
                self._items.pop(key, None)

    def delete(self, key: str) -> None:
        with self._lock:
            self._items.pop(key, None)


class FileTokenStore:
    """Keeps the tokens in files, one per key, shared by the processes of the same user.

    Without ``directory``, like the ``shellrent`` command, it follows ``SHELLRENT_TOKEN_CACHE``: a
    directory, or ``off`` to keep the tokens in memory instead, for the life of the process, as
    ``MemoryTokenStore`` does. Otherwise the directory is ``$XDG_CACHE_HOME/shellrent-sdk``, or
    ``~/.cache/shellrent-sdk``.

    When the directory does not exist it is created readable by its owner only (0700); the files
    are always written with mode 0600, through a temporary file and an atomic rename.
    """

    _KEY_PATTERN: Final = re.compile(r"[A-Za-z0-9_-][A-Za-z0-9_.-]*")

    def __init__(
        self,
        directory: str | os.PathLike[str] | None = None,
        *,
        clock: Callable[[], float] = time.time,
    ) -> None:
        setting = _env("SHELLRENT_TOKEN_CACHE") if directory is None else None
        off = setting is not None and setting.lower() == "off"
        if directory is None and setting is not None and not off:
            directory = setting

        self.directory: Final = Path(directory) if directory is not None else _default_cache_dir()
        self._clock = clock
        self._memory: Final = MemoryTokenStore(clock=clock) if off else None

    def get(self, key: str) -> str | None:
        path = self._path(key)
        if self._memory is not None:
            return self._memory.get(key)
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except FileNotFoundError:
            return None
        except ValueError:  # Not JSON: a file of someone else, or damaged.
            return None

        if not isinstance(data, dict):
            return None
        value, expires_at = data.get("value"), data.get("expires_at")
        if not isinstance(value, str) or not isinstance(expires_at, int | float):
            return None
        return value if expires_at > self._clock() else None

    def set(self, key: str, value: str, ttl: int) -> None:
        path = self._path(key)
        if self._memory is not None:
            self._memory.set(key, value, ttl)
            return
        if ttl <= 0:
            self.delete(key)
            return

        self._create_directory()
        content = json.dumps({"value": value, "expires_at": self._clock() + ttl})
        # mkstemp creates the file with mode 0600; the rename makes the new content visible at once.
        fd, temp_path = tempfile.mkstemp(dir=self.directory, prefix=".", suffix=".tmp")
        try:
            with os.fdopen(fd, "w", encoding="utf-8") as file:
                file.write(content)
            os.replace(temp_path, path)
        except BaseException:
            Path(temp_path).unlink(missing_ok=True)
            raise

    def delete(self, key: str) -> None:
        path = self._path(key)
        if self._memory is not None:
            self._memory.delete(key)
            return
        path.unlink(missing_ok=True)

    def _path(self, key: str) -> Path:
        if not self._KEY_PATTERN.fullmatch(key):
            raise ValueError(f"Invalid key for FileTokenStore: {key!r}")
        return self.directory / f"{key}.json"

    def _create_directory(self) -> None:
        try:
            self.directory.mkdir(mode=0o700, parents=True)
        except FileExistsError:
            return
        # The mode given to mkdir is reduced by the umask.
        self.directory.chmod(0o700)


class _Token(NamedTuple):
    access_token: str
    expires_at: float


class OAuth2Auth(httpx.Auth):
    """httpx authentication with the OAuth2 client credentials grant.

    The access token is requested by the authentication flow itself, through the client that sends
    the request (its transport, timeouts and retries included), so it works with both
    ``httpx.Client`` and ``httpx.AsyncClient``. The token is reused until ``EXPIRY_MARGIN`` seconds
    before it expires, and shared with the other clients and processes through ``token_store``.
    When the API answers 401 the token is discarded and the request is sent once more with a new one.

    The instance can be shared by threads and tasks: while one of them requests a token, the others
    wait for it instead of requesting their own.

    Raises (from the requests of the client):
        TokenError: The token endpoint did not issue an access token.
    """

    def __init__(
        self,
        credentials: ClientCredentials,
        token_store: TokenStore | None = None,
        *,
        clock: Callable[[], float] = time.time,
    ) -> None:
        self._credentials = credentials
        self._store: TokenStore = token_store if token_store is not None else MemoryTokenStore()
        self._clock = clock
        self._cache_key = _cache_key(credentials)
        self._token: _Token | None = None
        self._state_lock = threading.Lock()
        self._sync_request_lock = threading.Lock()
        # An asyncio.Lock works only in the event loop that first waits on it: one per loop.
        self._async_request_locks: weakref.WeakKeyDictionary[
            asyncio.AbstractEventLoop, asyncio.Lock
        ] = weakref.WeakKeyDictionary()

    def sync_auth_flow(
        self, request: httpx.Request
    ) -> Generator[httpx.Request, httpx.Response, None]:
        request.read()  # Sent twice after a 401.
        rejected: str | None = None
        while True:
            token = self._current_token(rejected)
            if token is None:
                with self._sync_request_lock:
                    token = self._current_token(rejected)
                    if token is None:
                        token_response = yield self._token_request(
                            request.headers, request.extensions
                        )
                        token_response.read()
                        token = self._save_token(token_response)

            request.headers["Authorization"] = f"Bearer {token}"
            response = yield request
            if response.status_code != 401 or rejected is not None:
                return
            self._discard(token)
            rejected = token

    async def async_auth_flow(
        self, request: httpx.Request
    ) -> AsyncGenerator[httpx.Request, httpx.Response]:
        await request.aread()  # Sent twice after a 401.
        rejected: str | None = None
        while True:
            token = self._current_token(rejected)
            if token is None:
                async with self._async_request_lock():
                    token = self._current_token(rejected)
                    if token is None:
                        token_response = yield self._token_request(
                            request.headers, request.extensions
                        )
                        await token_response.aread()
                        token = self._save_token(token_response)

            request.headers["Authorization"] = f"Bearer {token}"
            response = yield request
            if response.status_code != 401 or rejected is not None:
                return
            self._discard(token)
            rejected = token

    def get_token(self, client: httpx.Client) -> str:
        """Returns a valid access token, requesting a new one through ``client`` when needed.

        Raises:
            TokenError: The token endpoint did not issue an access token.
        """
        token = self._current_token(None)
        if token is not None:
            return token
        with self._sync_request_lock:
            token = self._current_token(None)
            if token is not None:
                return token
            request = self._token_request(client.headers, {"timeout": client.timeout.as_dict()})
            return self._save_token(client.send(request, auth=None))

    async def aget_token(self, client: httpx.AsyncClient) -> str:
        """Returns a valid access token, requesting a new one through ``client`` when needed.

        Raises:
            TokenError: The token endpoint did not issue an access token.
        """
        token = self._current_token(None)
        if token is not None:
            return token
        async with self._async_request_lock():
            token = self._current_token(None)
            if token is not None:
                return token
            request = self._token_request(client.headers, {"timeout": client.timeout.as_dict()})
            return self._save_token(await client.send(request, auth=None))

    def _async_request_lock(self) -> asyncio.Lock:
        loop = asyncio.get_running_loop()
        with self._state_lock:
            lock = self._async_request_locks.get(loop)
            if lock is None:
                lock = self._async_request_locks[loop] = asyncio.Lock()
            return lock

    def _current_token(self, rejected: str | None) -> str | None:
        """The token in memory or else in the store, if still valid and not the rejected one."""
        with self._state_lock:
            now = self._clock()
            token = self._token
            if token is None or token.expires_at <= now or token.access_token == rejected:
                token = self._stored_token()
                if token is not None and (
                    token.expires_at <= now or token.access_token == rejected
                ):
                    token = None
                self._token = token
            return token.access_token if token is not None else None

    def _token_request(
        self, headers: httpx.Headers, extensions: Mapping[str, Any]
    ) -> httpx.Request:
        credentials = self._credentials
        form = {
            "grant_type": "client_credentials",
            "client_id": credentials.client_id,
            "client_secret": credentials.client_secret,
        }
        if credentials.scopes is not None:
            form["scope"] = " ".join(credentials.scopes)
        if credentials.audience is not None:
            form["audience"] = credentials.audience

        token_headers = {"Accept": "application/json"}
        if "User-Agent" in headers:
            token_headers["User-Agent"] = headers["User-Agent"]
        token_extensions = {"timeout": extensions["timeout"]} if "timeout" in extensions else {}

        return httpx.Request(
            "POST",
            credentials.token_url,
            headers=token_headers,
            data=form,
            extensions=token_extensions,
        )

    def _save_token(self, response: httpx.Response) -> str:
        """Reads the token from the response of the token endpoint and keeps it."""
        try:
            body = response.json()
        except ValueError:
            body = None
        if not isinstance(body, dict):
            body = {}

        access_token = body.get("access_token")
        expires_in = body.get("expires_in")
        if (
            response.status_code != 200
            or not isinstance(access_token, str)
            or not access_token
            or not isinstance(expires_in, int | float)
            or isinstance(expires_in, bool)
        ):
            raise self._token_error(response, body)

        now = self._clock()
        token = _Token(access_token, now + expires_in - EXPIRY_MARGIN)
        with self._state_lock:
            self._token = token
            ttl = int(token.expires_at - now)
            if ttl > 0:
                value = json.dumps(
                    {"access_token": token.access_token, "expires_at": token.expires_at}
                )
                with self._store_errors_logged():
                    self._store.set(self._cache_key, value, ttl)
        return access_token

    def _discard(self, token: str) -> None:
        """Forgets a token rejected by the API, unless another request has replaced it already."""
        with self._state_lock:
            if self._token is not None and self._token.access_token == token:
                self._token = None
            stored = self._stored_token()
            if stored is not None and stored.access_token == token:
                with self._store_errors_logged():
                    self._store.delete(self._cache_key)

    def _stored_token(self) -> _Token | None:
        value: object = None
        with self._store_errors_logged():
            value = self._store.get(self._cache_key)
        if not isinstance(value, str):
            return None
        try:
            data = json.loads(value)
            return _Token(str(data["access_token"]), float(data["expires_at"]))
        except (ValueError, TypeError, KeyError):
            return None

    @contextlib.contextmanager
    def _store_errors_logged(self) -> Iterator[None]:
        # Without the store the token is still reused in memory; other processes request their own.
        try:
            yield
        except Exception as exc:  # noqa: BLE001 - any failure of a third-party cache.
            logger.warning("The token store %s failed: %s", type(self._store).__name__, exc)

    def _token_error(self, response: httpx.Response, body: dict[str, Any]) -> TokenError:
        error = body.get("error")
        description = body.get("error_description")
        error = error if isinstance(error, str) else None
        description = description if isinstance(description, str) else None

        message = (
            f"The token endpoint {self._credentials.token_url} answered HTTP {response.status_code}"
        )
        if error is not None:
            message += f": {error}" + (f" ({description})" if description is not None else "")
        elif response.status_code == 200:
            message += " without a valid access token"

        return TokenError(
            message, error=error, error_description=description, status_code=response.status_code
        )


def _cache_key(credentials: ClientCredentials) -> str:
    """Key of the token of these credentials: it identifies them without the secret."""
    identity = [
        credentials.token_url,
        credentials.client_id,
        credentials.audience,
        sorted(credentials.scopes) if credentials.scopes is not None else None,
    ]
    digest = hashlib.sha256(json.dumps(identity).encode()).hexdigest()
    return f"shellrent_sdk.token.{digest}"


def _default_cache_dir() -> Path:
    # The XDG specification says to ignore relative paths.
    xdg_cache_home = os.environ.get("XDG_CACHE_HOME", "")
    base = Path(xdg_cache_home) if os.path.isabs(xdg_cache_home) else Path.home() / ".cache"
    return base / "shellrent-sdk"


def _env(name: str) -> str | None:
    value = os.environ.get(name)
    return value if value else None
