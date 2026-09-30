from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.ip_address_response import IpAddressResponse
from ...types import Response


def _get_kwargs(
    server_id: int,
    ip_address_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v3/servers/{server_id}/ip_addresses/{ip_address_id}".format(
            server_id=quote(str(server_id), safe=""),
            ip_address_id=quote(str(ip_address_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | IpAddressResponse | None:
    if response.status_code == 200:
        response_200 = IpAddressResponse.from_dict(response.json())

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
) -> Response[ApiError | IpAddressResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    server_id: int,
    ip_address_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[ApiError | IpAddressResponse]:
    """Get server IP address

     Get IP address details for server

    Args:
        server_id (int):
        ip_address_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | IpAddressResponse]
    """

    kwargs = _get_kwargs(
        server_id=server_id,
        ip_address_id=ip_address_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    server_id: int,
    ip_address_id: int,
    *,
    client: AuthenticatedClient,
) -> ApiError | IpAddressResponse | None:
    """Get server IP address

     Get IP address details for server

    Args:
        server_id (int):
        ip_address_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | IpAddressResponse
    """

    return sync_detailed(
        server_id=server_id,
        ip_address_id=ip_address_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    server_id: int,
    ip_address_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[ApiError | IpAddressResponse]:
    """Get server IP address

     Get IP address details for server

    Args:
        server_id (int):
        ip_address_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | IpAddressResponse]
    """

    kwargs = _get_kwargs(
        server_id=server_id,
        ip_address_id=ip_address_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    server_id: int,
    ip_address_id: int,
    *,
    client: AuthenticatedClient,
) -> ApiError | IpAddressResponse | None:
    """Get server IP address

     Get IP address details for server

    Args:
        server_id (int):
        ip_address_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | IpAddressResponse
    """

    return (
        await asyncio_detailed(
            server_id=server_id,
            ip_address_id=ip_address_id,
            client=client,
        )
    ).parsed
