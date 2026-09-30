from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.pec_owner_change_paginated_list_response import PecOwnerChangePaginatedListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    pec_id: int,
    *,
    page: int | Unset = 1,
    per_page: int | Unset = 20,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["per_page"] = per_page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v3/pec-mailboxes/{pec_id}/owner-changes".format(
            pec_id=quote(str(pec_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | PecOwnerChangePaginatedListResponse | None:
    if response.status_code == 200:
        response_200 = PecOwnerChangePaginatedListResponse.from_dict(response.json())

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
) -> Response[ApiError | PecOwnerChangePaginatedListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    pec_id: int,
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    per_page: int | Unset = 20,
) -> Response[ApiError | PecOwnerChangePaginatedListResponse]:
    """List PEC mailbox owner changes

     Get a paginated list of owner change requests for a PEC mailbox

    Args:
        pec_id (int):
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | PecOwnerChangePaginatedListResponse]
    """

    kwargs = _get_kwargs(
        pec_id=pec_id,
        page=page,
        per_page=per_page,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    pec_id: int,
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    per_page: int | Unset = 20,
) -> ApiError | PecOwnerChangePaginatedListResponse | None:
    """List PEC mailbox owner changes

     Get a paginated list of owner change requests for a PEC mailbox

    Args:
        pec_id (int):
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | PecOwnerChangePaginatedListResponse
    """

    return sync_detailed(
        pec_id=pec_id,
        client=client,
        page=page,
        per_page=per_page,
    ).parsed


async def asyncio_detailed(
    pec_id: int,
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    per_page: int | Unset = 20,
) -> Response[ApiError | PecOwnerChangePaginatedListResponse]:
    """List PEC mailbox owner changes

     Get a paginated list of owner change requests for a PEC mailbox

    Args:
        pec_id (int):
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | PecOwnerChangePaginatedListResponse]
    """

    kwargs = _get_kwargs(
        pec_id=pec_id,
        page=page,
        per_page=per_page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    pec_id: int,
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    per_page: int | Unset = 20,
) -> ApiError | PecOwnerChangePaginatedListResponse | None:
    """List PEC mailbox owner changes

     Get a paginated list of owner change requests for a PEC mailbox

    Args:
        pec_id (int):
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | PecOwnerChangePaginatedListResponse
    """

    return (
        await asyncio_detailed(
            pec_id=pec_id,
            client=client,
            page=page,
            per_page=per_page,
        )
    ).parsed
