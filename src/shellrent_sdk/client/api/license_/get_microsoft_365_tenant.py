from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.microsoft_365_tenant_response import Microsoft365TenantResponse
from ...types import Response


def _get_kwargs(
    microsoft_365_tenant_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v3/microsoft365-tenants/{microsoft_365_tenant_id}".format(
            microsoft_365_tenant_id=quote(str(microsoft_365_tenant_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | Microsoft365TenantResponse | None:
    if response.status_code == 200:
        response_200 = Microsoft365TenantResponse.from_dict(response.json())

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
) -> Response[ApiError | Microsoft365TenantResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    microsoft_365_tenant_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[ApiError | Microsoft365TenantResponse]:
    """Get Microsoft 365 tenant

     Get details of a Microsoft 365 tenant

    Args:
        microsoft_365_tenant_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | Microsoft365TenantResponse]
    """

    kwargs = _get_kwargs(
        microsoft_365_tenant_id=microsoft_365_tenant_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    microsoft_365_tenant_id: int,
    *,
    client: AuthenticatedClient,
) -> ApiError | Microsoft365TenantResponse | None:
    """Get Microsoft 365 tenant

     Get details of a Microsoft 365 tenant

    Args:
        microsoft_365_tenant_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | Microsoft365TenantResponse
    """

    return sync_detailed(
        microsoft_365_tenant_id=microsoft_365_tenant_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    microsoft_365_tenant_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[ApiError | Microsoft365TenantResponse]:
    """Get Microsoft 365 tenant

     Get details of a Microsoft 365 tenant

    Args:
        microsoft_365_tenant_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | Microsoft365TenantResponse]
    """

    kwargs = _get_kwargs(
        microsoft_365_tenant_id=microsoft_365_tenant_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    microsoft_365_tenant_id: int,
    *,
    client: AuthenticatedClient,
) -> ApiError | Microsoft365TenantResponse | None:
    """Get Microsoft 365 tenant

     Get details of a Microsoft 365 tenant

    Args:
        microsoft_365_tenant_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | Microsoft365TenantResponse
    """

    return (
        await asyncio_detailed(
            microsoft_365_tenant_id=microsoft_365_tenant_id,
            client=client,
        )
    ).parsed
