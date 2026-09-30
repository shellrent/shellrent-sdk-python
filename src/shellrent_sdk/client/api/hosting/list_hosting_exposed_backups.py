from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.hosting_backup_list_response import HostingBackupListResponse
from ...types import Response


def _get_kwargs(
    hosting_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v3/hostings/{hosting_id}/backups/exhibitions".format(
            hosting_id=quote(str(hosting_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | HostingBackupListResponse | None:
    if response.status_code == 200:
        response_200 = HostingBackupListResponse.from_dict(response.json())

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
) -> Response[ApiError | HostingBackupListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    hosting_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[ApiError | HostingBackupListResponse]:
    """List exposed backups

     Get list of exposed backups for hosting

    Args:
        hosting_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | HostingBackupListResponse]
    """

    kwargs = _get_kwargs(
        hosting_id=hosting_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    hosting_id: int,
    *,
    client: AuthenticatedClient,
) -> ApiError | HostingBackupListResponse | None:
    """List exposed backups

     Get list of exposed backups for hosting

    Args:
        hosting_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | HostingBackupListResponse
    """

    return sync_detailed(
        hosting_id=hosting_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    hosting_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[ApiError | HostingBackupListResponse]:
    """List exposed backups

     Get list of exposed backups for hosting

    Args:
        hosting_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | HostingBackupListResponse]
    """

    kwargs = _get_kwargs(
        hosting_id=hosting_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    hosting_id: int,
    *,
    client: AuthenticatedClient,
) -> ApiError | HostingBackupListResponse | None:
    """List exposed backups

     Get list of exposed backups for hosting

    Args:
        hosting_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | HostingBackupListResponse
    """

    return (
        await asyncio_detailed(
            hosting_id=hosting_id,
            client=client,
        )
    ).parsed
