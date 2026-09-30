from __future__ import annotations

import httpx

from .auth import ClientCredentials, MemoryTokenStore, TokenStore
from .client import AuthenticatedClient
from .http import client_args


def create_client(
    credentials: ClientCredentials | None = None,
    *,
    token_store: TokenStore | None = None,
    retry: bool = True,
    timeout: float | httpx.Timeout | None = 30.0,
) -> AuthenticatedClient:
    """Creates the client of the Shellrent API, to pass to the functions of ``shellrent_sdk.client.api``.

    Args:
        credentials: Default ``ClientCredentials.from_env()``.
        token_store: Cache of the access token; default a ``MemoryTokenStore``. Pass a
            ``FileTokenStore`` (or a shared cache) to reuse the token across processes.
        retry: Retry the requests rejected with 429 Too Many Requests, see ``RetryTransport``.
        timeout: Timeout of the requests, in seconds.

    Documented error responses are returned as ``ApiError`` (see ``unwrap()``); undocumented status
    codes raise ``UnexpectedStatus``.
    """
    if credentials is None:
        credentials = ClientCredentials.from_env()

    args = client_args(
        credentials,
        token_store=token_store if token_store is not None else MemoryTokenStore(),
        retry=retry,
        timeout=timeout,
    )
    return AuthenticatedClient(
        base_url=args.pop("base_url"),
        # The generated client would send a fixed token: the header is set by OAuth2Auth instead,
        # which replaces this empty default in every request.
        token="",
        prefix="",
        headers=args.pop("headers"),
        timeout=args.pop("timeout"),
        httpx_args=args,
        raise_on_unexpected_status=True,
    )
