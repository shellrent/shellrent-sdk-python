import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.payment_paginated_list_response import PaymentPaginatedListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    payment_method: str | Unset = UNSET,
    date_payment_from: datetime.datetime | Unset = UNSET,
    date_payment_to: datetime.datetime | Unset = UNSET,
    page: int | Unset = 1,
    per_page: int | Unset = 20,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["payment_method"] = payment_method

    json_date_payment_from: str | Unset = UNSET
    if not isinstance(date_payment_from, Unset):
        json_date_payment_from = date_payment_from.isoformat()
    params["date_payment_from"] = json_date_payment_from

    json_date_payment_to: str | Unset = UNSET
    if not isinstance(date_payment_to, Unset):
        json_date_payment_to = date_payment_to.isoformat()
    params["date_payment_to"] = json_date_payment_to

    params["page"] = page

    params["per_page"] = per_page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v3/payments",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | PaymentPaginatedListResponse | None:
    if response.status_code == 200:
        response_200 = PaymentPaginatedListResponse.from_dict(response.json())

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
) -> Response[ApiError | PaymentPaginatedListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    payment_method: str | Unset = UNSET,
    date_payment_from: datetime.datetime | Unset = UNSET,
    date_payment_to: datetime.datetime | Unset = UNSET,
    page: int | Unset = 1,
    per_page: int | Unset = 20,
) -> Response[ApiError | PaymentPaginatedListResponse]:
    """List all Payments

     Get a list of all Payments

    Args:
        payment_method (str | Unset):
        date_payment_from (datetime.datetime | Unset):
        date_payment_to (datetime.datetime | Unset):
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | PaymentPaginatedListResponse]
    """

    kwargs = _get_kwargs(
        payment_method=payment_method,
        date_payment_from=date_payment_from,
        date_payment_to=date_payment_to,
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
    payment_method: str | Unset = UNSET,
    date_payment_from: datetime.datetime | Unset = UNSET,
    date_payment_to: datetime.datetime | Unset = UNSET,
    page: int | Unset = 1,
    per_page: int | Unset = 20,
) -> ApiError | PaymentPaginatedListResponse | None:
    """List all Payments

     Get a list of all Payments

    Args:
        payment_method (str | Unset):
        date_payment_from (datetime.datetime | Unset):
        date_payment_to (datetime.datetime | Unset):
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | PaymentPaginatedListResponse
    """

    return sync_detailed(
        client=client,
        payment_method=payment_method,
        date_payment_from=date_payment_from,
        date_payment_to=date_payment_to,
        page=page,
        per_page=per_page,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    payment_method: str | Unset = UNSET,
    date_payment_from: datetime.datetime | Unset = UNSET,
    date_payment_to: datetime.datetime | Unset = UNSET,
    page: int | Unset = 1,
    per_page: int | Unset = 20,
) -> Response[ApiError | PaymentPaginatedListResponse]:
    """List all Payments

     Get a list of all Payments

    Args:
        payment_method (str | Unset):
        date_payment_from (datetime.datetime | Unset):
        date_payment_to (datetime.datetime | Unset):
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | PaymentPaginatedListResponse]
    """

    kwargs = _get_kwargs(
        payment_method=payment_method,
        date_payment_from=date_payment_from,
        date_payment_to=date_payment_to,
        page=page,
        per_page=per_page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    payment_method: str | Unset = UNSET,
    date_payment_from: datetime.datetime | Unset = UNSET,
    date_payment_to: datetime.datetime | Unset = UNSET,
    page: int | Unset = 1,
    per_page: int | Unset = 20,
) -> ApiError | PaymentPaginatedListResponse | None:
    """List all Payments

     Get a list of all Payments

    Args:
        payment_method (str | Unset):
        date_payment_from (datetime.datetime | Unset):
        date_payment_to (datetime.datetime | Unset):
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | PaymentPaginatedListResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            payment_method=payment_method,
            date_payment_from=date_payment_from,
            date_payment_to=date_payment_to,
            page=page,
            per_page=per_page,
        )
    ).parsed
