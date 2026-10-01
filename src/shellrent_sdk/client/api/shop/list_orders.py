import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.list_orders_type import ListOrdersType
from ...models.order_paginated_list_response import OrderPaginatedListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    order_status: str | Unset = UNSET,
    type_: ListOrdersType | Unset = UNSET,
    invoice_id: int | Unset = UNSET,
    purchase_id: int | Unset = UNSET,
    payed: bool | Unset = UNSET,
    date_created_from: datetime.datetime | Unset = UNSET,
    date_created_to: datetime.datetime | Unset = UNSET,
    page: int | Unset = 1,
    per_page: int | Unset = 15,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["order_status"] = order_status

    json_type_: str | Unset = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_.value

    params["type"] = json_type_

    params["invoice_id"] = invoice_id

    params["purchase_id"] = purchase_id

    params["payed"] = payed

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
        "url": "/api/v3/orders",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | OrderPaginatedListResponse | None:
    if response.status_code == 200:
        response_200 = OrderPaginatedListResponse.from_dict(response.json())

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
) -> Response[ApiError | OrderPaginatedListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    order_status: str | Unset = UNSET,
    type_: ListOrdersType | Unset = UNSET,
    invoice_id: int | Unset = UNSET,
    purchase_id: int | Unset = UNSET,
    payed: bool | Unset = UNSET,
    date_created_from: datetime.datetime | Unset = UNSET,
    date_created_to: datetime.datetime | Unset = UNSET,
    page: int | Unset = 1,
    per_page: int | Unset = 15,
) -> Response[ApiError | OrderPaginatedListResponse]:
    """List all Orders

     Get a list of all Orders

    Args:
        order_status (str | Unset):
        type_ (ListOrdersType | Unset):
        invoice_id (int | Unset):
        purchase_id (int | Unset):
        payed (bool | Unset):
        date_created_from (datetime.datetime | Unset):
        date_created_to (datetime.datetime | Unset):
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 15.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | OrderPaginatedListResponse]
    """

    kwargs = _get_kwargs(
        order_status=order_status,
        type_=type_,
        invoice_id=invoice_id,
        purchase_id=purchase_id,
        payed=payed,
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
    order_status: str | Unset = UNSET,
    type_: ListOrdersType | Unset = UNSET,
    invoice_id: int | Unset = UNSET,
    purchase_id: int | Unset = UNSET,
    payed: bool | Unset = UNSET,
    date_created_from: datetime.datetime | Unset = UNSET,
    date_created_to: datetime.datetime | Unset = UNSET,
    page: int | Unset = 1,
    per_page: int | Unset = 15,
) -> ApiError | OrderPaginatedListResponse | None:
    """List all Orders

     Get a list of all Orders

    Args:
        order_status (str | Unset):
        type_ (ListOrdersType | Unset):
        invoice_id (int | Unset):
        purchase_id (int | Unset):
        payed (bool | Unset):
        date_created_from (datetime.datetime | Unset):
        date_created_to (datetime.datetime | Unset):
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 15.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | OrderPaginatedListResponse
    """

    return sync_detailed(
        client=client,
        order_status=order_status,
        type_=type_,
        invoice_id=invoice_id,
        purchase_id=purchase_id,
        payed=payed,
        date_created_from=date_created_from,
        date_created_to=date_created_to,
        page=page,
        per_page=per_page,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    order_status: str | Unset = UNSET,
    type_: ListOrdersType | Unset = UNSET,
    invoice_id: int | Unset = UNSET,
    purchase_id: int | Unset = UNSET,
    payed: bool | Unset = UNSET,
    date_created_from: datetime.datetime | Unset = UNSET,
    date_created_to: datetime.datetime | Unset = UNSET,
    page: int | Unset = 1,
    per_page: int | Unset = 15,
) -> Response[ApiError | OrderPaginatedListResponse]:
    """List all Orders

     Get a list of all Orders

    Args:
        order_status (str | Unset):
        type_ (ListOrdersType | Unset):
        invoice_id (int | Unset):
        purchase_id (int | Unset):
        payed (bool | Unset):
        date_created_from (datetime.datetime | Unset):
        date_created_to (datetime.datetime | Unset):
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 15.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | OrderPaginatedListResponse]
    """

    kwargs = _get_kwargs(
        order_status=order_status,
        type_=type_,
        invoice_id=invoice_id,
        purchase_id=purchase_id,
        payed=payed,
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
    order_status: str | Unset = UNSET,
    type_: ListOrdersType | Unset = UNSET,
    invoice_id: int | Unset = UNSET,
    purchase_id: int | Unset = UNSET,
    payed: bool | Unset = UNSET,
    date_created_from: datetime.datetime | Unset = UNSET,
    date_created_to: datetime.datetime | Unset = UNSET,
    page: int | Unset = 1,
    per_page: int | Unset = 15,
) -> ApiError | OrderPaginatedListResponse | None:
    """List all Orders

     Get a list of all Orders

    Args:
        order_status (str | Unset):
        type_ (ListOrdersType | Unset):
        invoice_id (int | Unset):
        purchase_id (int | Unset):
        payed (bool | Unset):
        date_created_from (datetime.datetime | Unset):
        date_created_to (datetime.datetime | Unset):
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 15.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | OrderPaginatedListResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            order_status=order_status,
            type_=type_,
            invoice_id=invoice_id,
            purchase_id=purchase_id,
            payed=payed,
            date_created_from=date_created_from,
            date_created_to=date_created_to,
            page=page,
            per_page=per_page,
        )
    ).parsed
