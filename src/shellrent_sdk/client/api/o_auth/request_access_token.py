from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.o_auth_error import OAuthError
from ...models.o_auth_token_response import OAuthTokenResponse
from ...models.request_access_token_body import RequestAccessTokenBody
from ...types import Response


def _get_kwargs(
    *,
    body: RequestAccessTokenBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/oauth/token",
    }

    _kwargs["data"] = body.to_dict()
    headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> OAuthError | OAuthTokenResponse | None:
    if response.status_code == 200:
        response_200 = OAuthTokenResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = OAuthError.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = OAuthError.from_dict(response.json())

        return response_401

    if response.status_code == 429:
        response_429 = OAuthError.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = OAuthError.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[OAuthError | OAuthTokenResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RequestAccessTokenBody,
) -> Response[OAuthError | OAuthTokenResponse]:
    """Richiedi un access token

     Eroga un access token JWT tramite grant `client_credentials`. I parametri `audience` e `scope` sono
    opzionali: senza `audience` il token usa l'unica audience del client (un client con più audience
    deve indicarla), senza `scope` riceve tutti gli scope assegnati al client, come con
    `scope=api:full`. Gli scope interni sono concessi solo con audience `api-internal`. La risposta
    riporta l'audience e gli scope concessi.

    Args:
        body (RequestAccessTokenBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OAuthError | OAuthTokenResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: RequestAccessTokenBody,
) -> OAuthError | OAuthTokenResponse | None:
    """Richiedi un access token

     Eroga un access token JWT tramite grant `client_credentials`. I parametri `audience` e `scope` sono
    opzionali: senza `audience` il token usa l'unica audience del client (un client con più audience
    deve indicarla), senza `scope` riceve tutti gli scope assegnati al client, come con
    `scope=api:full`. Gli scope interni sono concessi solo con audience `api-internal`. La risposta
    riporta l'audience e gli scope concessi.

    Args:
        body (RequestAccessTokenBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OAuthError | OAuthTokenResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RequestAccessTokenBody,
) -> Response[OAuthError | OAuthTokenResponse]:
    """Richiedi un access token

     Eroga un access token JWT tramite grant `client_credentials`. I parametri `audience` e `scope` sono
    opzionali: senza `audience` il token usa l'unica audience del client (un client con più audience
    deve indicarla), senza `scope` riceve tutti gli scope assegnati al client, come con
    `scope=api:full`. Gli scope interni sono concessi solo con audience `api-internal`. La risposta
    riporta l'audience e gli scope concessi.

    Args:
        body (RequestAccessTokenBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OAuthError | OAuthTokenResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: RequestAccessTokenBody,
) -> OAuthError | OAuthTokenResponse | None:
    """Richiedi un access token

     Eroga un access token JWT tramite grant `client_credentials`. I parametri `audience` e `scope` sono
    opzionali: senza `audience` il token usa l'unica audience del client (un client con più audience
    deve indicarla), senza `scope` riceve tutti gli scope assegnati al client, come con
    `scope=api:full`. Gli scope interni sono concessi solo con audience `api-internal`. La risposta
    riporta l'audience e gli scope concessi.

    Args:
        body (RequestAccessTokenBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OAuthError | OAuthTokenResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
