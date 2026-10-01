import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.purchase_paginated_list_response import PurchasePaginatedListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    alive_only: bool | Unset = True,
    suspended: bool | Unset = UNSET,
    do_not_renew: bool | Unset = UNSET,
    purchase_id_primary: int | Unset = UNSET,
    activation_date_from: datetime.date | Unset = UNSET,
    activation_date_to: datetime.date | Unset = UNSET,
    expire_date_from: datetime.date | Unset = UNSET,
    expire_date_to: datetime.date | Unset = UNSET,
    purchase_ids: list[int] | Unset = UNSET,
    service_code: str | Unset = UNSET,
    service_category_code: str | Unset = UNSET,
    search: str | Unset = UNSET,
    page: int | Unset = 1,
    per_page: int | Unset = 15,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["alive_only"] = alive_only

    params["suspended"] = suspended

    params["do_not_renew"] = do_not_renew

    params["purchase_id_primary"] = purchase_id_primary

    json_activation_date_from: str | Unset = UNSET
    if not isinstance(activation_date_from, Unset):
        json_activation_date_from = activation_date_from.isoformat()
    params["activation_date_from"] = json_activation_date_from

    json_activation_date_to: str | Unset = UNSET
    if not isinstance(activation_date_to, Unset):
        json_activation_date_to = activation_date_to.isoformat()
    params["activation_date_to"] = json_activation_date_to

    json_expire_date_from: str | Unset = UNSET
    if not isinstance(expire_date_from, Unset):
        json_expire_date_from = expire_date_from.isoformat()
    params["expire_date_from"] = json_expire_date_from

    json_expire_date_to: str | Unset = UNSET
    if not isinstance(expire_date_to, Unset):
        json_expire_date_to = expire_date_to.isoformat()
    params["expire_date_to"] = json_expire_date_to

    json_purchase_ids: list[int] | Unset = UNSET
    if not isinstance(purchase_ids, Unset):
        json_purchase_ids = purchase_ids

    params["purchase_ids"] = json_purchase_ids

    params["service_code"] = service_code

    params["service_category_code"] = service_category_code

    params["search"] = search

    params["page"] = page

    params["per_page"] = per_page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v3/purchases",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | PurchasePaginatedListResponse | None:
    if response.status_code == 200:
        response_200 = PurchasePaginatedListResponse.from_dict(response.json())

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
) -> Response[ApiError | PurchasePaginatedListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    alive_only: bool | Unset = True,
    suspended: bool | Unset = UNSET,
    do_not_renew: bool | Unset = UNSET,
    purchase_id_primary: int | Unset = UNSET,
    activation_date_from: datetime.date | Unset = UNSET,
    activation_date_to: datetime.date | Unset = UNSET,
    expire_date_from: datetime.date | Unset = UNSET,
    expire_date_to: datetime.date | Unset = UNSET,
    purchase_ids: list[int] | Unset = UNSET,
    service_code: str | Unset = UNSET,
    service_category_code: str | Unset = UNSET,
    search: str | Unset = UNSET,
    page: int | Unset = 1,
    per_page: int | Unset = 15,
) -> Response[ApiError | PurchasePaginatedListResponse]:
    """List purchases

     Get a list of all purchases

    Args:
        alive_only (bool | Unset):  Default: True.
        suspended (bool | Unset):
        do_not_renew (bool | Unset):
        purchase_id_primary (int | Unset):
        activation_date_from (datetime.date | Unset):
        activation_date_to (datetime.date | Unset):
        expire_date_from (datetime.date | Unset):
        expire_date_to (datetime.date | Unset):
        purchase_ids (list[int] | Unset):
        service_code (str | Unset):
        service_category_code (str | Unset):
        search (str | Unset):
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 15.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | PurchasePaginatedListResponse]
    """

    kwargs = _get_kwargs(
        alive_only=alive_only,
        suspended=suspended,
        do_not_renew=do_not_renew,
        purchase_id_primary=purchase_id_primary,
        activation_date_from=activation_date_from,
        activation_date_to=activation_date_to,
        expire_date_from=expire_date_from,
        expire_date_to=expire_date_to,
        purchase_ids=purchase_ids,
        service_code=service_code,
        service_category_code=service_category_code,
        search=search,
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
    alive_only: bool | Unset = True,
    suspended: bool | Unset = UNSET,
    do_not_renew: bool | Unset = UNSET,
    purchase_id_primary: int | Unset = UNSET,
    activation_date_from: datetime.date | Unset = UNSET,
    activation_date_to: datetime.date | Unset = UNSET,
    expire_date_from: datetime.date | Unset = UNSET,
    expire_date_to: datetime.date | Unset = UNSET,
    purchase_ids: list[int] | Unset = UNSET,
    service_code: str | Unset = UNSET,
    service_category_code: str | Unset = UNSET,
    search: str | Unset = UNSET,
    page: int | Unset = 1,
    per_page: int | Unset = 15,
) -> ApiError | PurchasePaginatedListResponse | None:
    """List purchases

     Get a list of all purchases

    Args:
        alive_only (bool | Unset):  Default: True.
        suspended (bool | Unset):
        do_not_renew (bool | Unset):
        purchase_id_primary (int | Unset):
        activation_date_from (datetime.date | Unset):
        activation_date_to (datetime.date | Unset):
        expire_date_from (datetime.date | Unset):
        expire_date_to (datetime.date | Unset):
        purchase_ids (list[int] | Unset):
        service_code (str | Unset):
        service_category_code (str | Unset):
        search (str | Unset):
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 15.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | PurchasePaginatedListResponse
    """

    return sync_detailed(
        client=client,
        alive_only=alive_only,
        suspended=suspended,
        do_not_renew=do_not_renew,
        purchase_id_primary=purchase_id_primary,
        activation_date_from=activation_date_from,
        activation_date_to=activation_date_to,
        expire_date_from=expire_date_from,
        expire_date_to=expire_date_to,
        purchase_ids=purchase_ids,
        service_code=service_code,
        service_category_code=service_category_code,
        search=search,
        page=page,
        per_page=per_page,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    alive_only: bool | Unset = True,
    suspended: bool | Unset = UNSET,
    do_not_renew: bool | Unset = UNSET,
    purchase_id_primary: int | Unset = UNSET,
    activation_date_from: datetime.date | Unset = UNSET,
    activation_date_to: datetime.date | Unset = UNSET,
    expire_date_from: datetime.date | Unset = UNSET,
    expire_date_to: datetime.date | Unset = UNSET,
    purchase_ids: list[int] | Unset = UNSET,
    service_code: str | Unset = UNSET,
    service_category_code: str | Unset = UNSET,
    search: str | Unset = UNSET,
    page: int | Unset = 1,
    per_page: int | Unset = 15,
) -> Response[ApiError | PurchasePaginatedListResponse]:
    """List purchases

     Get a list of all purchases

    Args:
        alive_only (bool | Unset):  Default: True.
        suspended (bool | Unset):
        do_not_renew (bool | Unset):
        purchase_id_primary (int | Unset):
        activation_date_from (datetime.date | Unset):
        activation_date_to (datetime.date | Unset):
        expire_date_from (datetime.date | Unset):
        expire_date_to (datetime.date | Unset):
        purchase_ids (list[int] | Unset):
        service_code (str | Unset):
        service_category_code (str | Unset):
        search (str | Unset):
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 15.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | PurchasePaginatedListResponse]
    """

    kwargs = _get_kwargs(
        alive_only=alive_only,
        suspended=suspended,
        do_not_renew=do_not_renew,
        purchase_id_primary=purchase_id_primary,
        activation_date_from=activation_date_from,
        activation_date_to=activation_date_to,
        expire_date_from=expire_date_from,
        expire_date_to=expire_date_to,
        purchase_ids=purchase_ids,
        service_code=service_code,
        service_category_code=service_category_code,
        search=search,
        page=page,
        per_page=per_page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    alive_only: bool | Unset = True,
    suspended: bool | Unset = UNSET,
    do_not_renew: bool | Unset = UNSET,
    purchase_id_primary: int | Unset = UNSET,
    activation_date_from: datetime.date | Unset = UNSET,
    activation_date_to: datetime.date | Unset = UNSET,
    expire_date_from: datetime.date | Unset = UNSET,
    expire_date_to: datetime.date | Unset = UNSET,
    purchase_ids: list[int] | Unset = UNSET,
    service_code: str | Unset = UNSET,
    service_category_code: str | Unset = UNSET,
    search: str | Unset = UNSET,
    page: int | Unset = 1,
    per_page: int | Unset = 15,
) -> ApiError | PurchasePaginatedListResponse | None:
    """List purchases

     Get a list of all purchases

    Args:
        alive_only (bool | Unset):  Default: True.
        suspended (bool | Unset):
        do_not_renew (bool | Unset):
        purchase_id_primary (int | Unset):
        activation_date_from (datetime.date | Unset):
        activation_date_to (datetime.date | Unset):
        expire_date_from (datetime.date | Unset):
        expire_date_to (datetime.date | Unset):
        purchase_ids (list[int] | Unset):
        service_code (str | Unset):
        service_category_code (str | Unset):
        search (str | Unset):
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 15.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | PurchasePaginatedListResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            alive_only=alive_only,
            suspended=suspended,
            do_not_renew=do_not_renew,
            purchase_id_primary=purchase_id_primary,
            activation_date_from=activation_date_from,
            activation_date_to=activation_date_to,
            expire_date_from=expire_date_from,
            expire_date_to=expire_date_to,
            purchase_ids=purchase_ids,
            service_code=service_code,
            service_category_code=service_category_code,
            search=search,
            page=page,
            per_page=per_page,
        )
    ).parsed
