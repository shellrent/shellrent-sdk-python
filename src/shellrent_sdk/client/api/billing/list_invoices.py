import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.invoice_paginated_list_response import InvoicePaginatedListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    date_emission_from: datetime.date | Unset = UNSET,
    date_emission_to: datetime.date | Unset = UNSET,
    payed: bool | Unset = UNSET,
    page: int | Unset = 1,
    per_page: int | Unset = 20,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_date_emission_from: str | Unset = UNSET
    if not isinstance(date_emission_from, Unset):
        json_date_emission_from = date_emission_from.isoformat()
    params["date_emission_from"] = json_date_emission_from

    json_date_emission_to: str | Unset = UNSET
    if not isinstance(date_emission_to, Unset):
        json_date_emission_to = date_emission_to.isoformat()
    params["date_emission_to"] = json_date_emission_to

    params["payed"] = payed

    params["page"] = page

    params["per_page"] = per_page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v3/invoices",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | InvoicePaginatedListResponse | None:
    if response.status_code == 200:
        response_200 = InvoicePaginatedListResponse.from_dict(response.json())

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
) -> Response[ApiError | InvoicePaginatedListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    date_emission_from: datetime.date | Unset = UNSET,
    date_emission_to: datetime.date | Unset = UNSET,
    payed: bool | Unset = UNSET,
    page: int | Unset = 1,
    per_page: int | Unset = 20,
) -> Response[ApiError | InvoicePaginatedListResponse]:
    """List all Invoices

     Get a list of all Invoices

    Args:
        date_emission_from (datetime.date | Unset):
        date_emission_to (datetime.date | Unset):
        payed (bool | Unset):
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | InvoicePaginatedListResponse]
    """

    kwargs = _get_kwargs(
        date_emission_from=date_emission_from,
        date_emission_to=date_emission_to,
        payed=payed,
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
    date_emission_from: datetime.date | Unset = UNSET,
    date_emission_to: datetime.date | Unset = UNSET,
    payed: bool | Unset = UNSET,
    page: int | Unset = 1,
    per_page: int | Unset = 20,
) -> ApiError | InvoicePaginatedListResponse | None:
    """List all Invoices

     Get a list of all Invoices

    Args:
        date_emission_from (datetime.date | Unset):
        date_emission_to (datetime.date | Unset):
        payed (bool | Unset):
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | InvoicePaginatedListResponse
    """

    return sync_detailed(
        client=client,
        date_emission_from=date_emission_from,
        date_emission_to=date_emission_to,
        payed=payed,
        page=page,
        per_page=per_page,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    date_emission_from: datetime.date | Unset = UNSET,
    date_emission_to: datetime.date | Unset = UNSET,
    payed: bool | Unset = UNSET,
    page: int | Unset = 1,
    per_page: int | Unset = 20,
) -> Response[ApiError | InvoicePaginatedListResponse]:
    """List all Invoices

     Get a list of all Invoices

    Args:
        date_emission_from (datetime.date | Unset):
        date_emission_to (datetime.date | Unset):
        payed (bool | Unset):
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | InvoicePaginatedListResponse]
    """

    kwargs = _get_kwargs(
        date_emission_from=date_emission_from,
        date_emission_to=date_emission_to,
        payed=payed,
        page=page,
        per_page=per_page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    date_emission_from: datetime.date | Unset = UNSET,
    date_emission_to: datetime.date | Unset = UNSET,
    payed: bool | Unset = UNSET,
    page: int | Unset = 1,
    per_page: int | Unset = 20,
) -> ApiError | InvoicePaginatedListResponse | None:
    """List all Invoices

     Get a list of all Invoices

    Args:
        date_emission_from (datetime.date | Unset):
        date_emission_to (datetime.date | Unset):
        payed (bool | Unset):
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | InvoicePaginatedListResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            date_emission_from=date_emission_from,
            date_emission_to=date_emission_to,
            payed=payed,
            page=page,
            per_page=per_page,
        )
    ).parsed
