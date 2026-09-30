from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.tld_response import TldResponse
from ...types import Response


def _get_kwargs(
    tld_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v3/tlds/{tld_id}".format(
            tld_id=quote(str(tld_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | TldResponse | None:
    if response.status_code == 200:
        response_200 = TldResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ApiError.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ApiError.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ApiError.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ApiError.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = ApiError.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ApiError | TldResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tld_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[ApiError | TldResponse]:
    """Get a TLD

     Get details of a TLD extension

    Args:
        tld_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | TldResponse]
    """

    kwargs = _get_kwargs(
        tld_id=tld_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tld_id: int,
    *,
    client: AuthenticatedClient,
) -> ApiError | TldResponse | None:
    """Get a TLD

     Get details of a TLD extension

    Args:
        tld_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | TldResponse
    """

    return sync_detailed(
        tld_id=tld_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    tld_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[ApiError | TldResponse]:
    """Get a TLD

     Get details of a TLD extension

    Args:
        tld_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | TldResponse]
    """

    kwargs = _get_kwargs(
        tld_id=tld_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tld_id: int,
    *,
    client: AuthenticatedClient,
) -> ApiError | TldResponse | None:
    """Get a TLD

     Get details of a TLD extension

    Args:
        tld_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | TldResponse
    """

    return (
        await asyncio_detailed(
            tld_id=tld_id,
            client=client,
        )
    ).parsed
