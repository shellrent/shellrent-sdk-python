import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.list_sms_sms_status import ListSmsSmsStatus
from ...models.sms_paginated_list_response import SmsPaginatedListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    sms_status: ListSmsSmsStatus | Unset = UNSET,
    date_created_from: datetime.datetime | Unset = UNSET,
    date_created_to: datetime.datetime | Unset = UNSET,
    page: int | Unset = 1,
    per_page: int | Unset = 15,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_sms_status: str | Unset = UNSET
    if not isinstance(sms_status, Unset):
        json_sms_status = sms_status.value

    params["sms_status"] = json_sms_status

    json_date_created_from: str | Unset = UNSET
    if not isinstance(date_created_from, Unset):
        json_date_created_from = date_created_from.isoformat()
    params["date_created_from"] = json_date_created_from

    json_date_created_to: str | Unset = UNSET
    if not isinstance(date_created_to, Unset):
        json_date_created_to = date_created_to.isoformat()
    params["date_created_to"] = json_date_created_to

    params["page"] = page

    params["per_page"] = per_page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v3/sms",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | SmsPaginatedListResponse | None:
    if response.status_code == 200:
        response_200 = SmsPaginatedListResponse.from_dict(response.json())

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
) -> Response[ApiError | SmsPaginatedListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    sms_status: ListSmsSmsStatus | Unset = UNSET,
    date_created_from: datetime.datetime | Unset = UNSET,
    date_created_to: datetime.datetime | Unset = UNSET,
    page: int | Unset = 1,
    per_page: int | Unset = 15,
) -> Response[ApiError | SmsPaginatedListResponse]:
    """List all SMS

     Get a list of all SMS

    Args:
        sms_status (ListSmsSmsStatus | Unset):
        date_created_from (datetime.datetime | Unset):
        date_created_to (datetime.datetime | Unset):
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 15.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | SmsPaginatedListResponse]
    """

    kwargs = _get_kwargs(
        sms_status=sms_status,
        date_created_from=date_created_from,
        date_created_to=date_created_to,
        page=page,
        per_page=per_page,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    sms_status: ListSmsSmsStatus | Unset = UNSET,
    date_created_from: datetime.datetime | Unset = UNSET,
    date_created_to: datetime.datetime | Unset = UNSET,
    page: int | Unset = 1,
    per_page: int | Unset = 15,
) -> ApiError | SmsPaginatedListResponse | None:
    """List all SMS

     Get a list of all SMS

    Args:
        sms_status (ListSmsSmsStatus | Unset):
        date_created_from (datetime.datetime | Unset):
        date_created_to (datetime.datetime | Unset):
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 15.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | SmsPaginatedListResponse
    """

    return sync_detailed(
        client=client,
        sms_status=sms_status,
        date_created_from=date_created_from,
        date_created_to=date_created_to,
        page=page,
        per_page=per_page,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    sms_status: ListSmsSmsStatus | Unset = UNSET,
    date_created_from: datetime.datetime | Unset = UNSET,
    date_created_to: datetime.datetime | Unset = UNSET,
    page: int | Unset = 1,
    per_page: int | Unset = 15,
) -> Response[ApiError | SmsPaginatedListResponse]:
    """List all SMS

     Get a list of all SMS

    Args:
        sms_status (ListSmsSmsStatus | Unset):
        date_created_from (datetime.datetime | Unset):
        date_created_to (datetime.datetime | Unset):
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 15.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | SmsPaginatedListResponse]
    """

    kwargs = _get_kwargs(
        sms_status=sms_status,
        date_created_from=date_created_from,
        date_created_to=date_created_to,
        page=page,
        per_page=per_page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    sms_status: ListSmsSmsStatus | Unset = UNSET,
    date_created_from: datetime.datetime | Unset = UNSET,
    date_created_to: datetime.datetime | Unset = UNSET,
    page: int | Unset = 1,
    per_page: int | Unset = 15,
) -> ApiError | SmsPaginatedListResponse | None:
    """List all SMS

     Get a list of all SMS

    Args:
        sms_status (ListSmsSmsStatus | Unset):
        date_created_from (datetime.datetime | Unset):
        date_created_to (datetime.datetime | Unset):
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 15.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | SmsPaginatedListResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            sms_status=sms_status,
            date_created_from=date_created_from,
            date_created_to=date_created_to,
            page=page,
            per_page=per_page,
        )
    ).parsed
