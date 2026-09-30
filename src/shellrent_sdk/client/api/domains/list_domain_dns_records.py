from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.dns_record_paginated_list_response import DnsRecordPaginatedListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    domain_id: int,
    *,
    type_: str | Unset = UNSET,
    host: str | Unset = UNSET,
    destination: str | Unset = UNSET,
    page: int | Unset = 1,
    per_page: int | Unset = 20,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["type"] = type_

    params["host"] = host

    params["destination"] = destination

    params["page"] = page

    params["per_page"] = per_page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v3/domains/{domain_id}/dns/records".format(
            domain_id=quote(str(domain_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | DnsRecordPaginatedListResponse | None:
    if response.status_code == 200:
        response_200 = DnsRecordPaginatedListResponse.from_dict(response.json())

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
) -> Response[ApiError | DnsRecordPaginatedListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    domain_id: int,
    *,
    client: AuthenticatedClient,
    type_: str | Unset = UNSET,
    host: str | Unset = UNSET,
    destination: str | Unset = UNSET,
    page: int | Unset = 1,
    per_page: int | Unset = 20,
) -> Response[ApiError | DnsRecordPaginatedListResponse]:
    """List DNS records

     Get a list of all DNS Records. The results are paginated but the pagination does not have
    information about the total number of items and the total number of pages. Only forward pages
    navigation is supported.

    Args:
        domain_id (int):
        type_ (str | Unset):
        host (str | Unset):
        destination (str | Unset):
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | DnsRecordPaginatedListResponse]
    """

    kwargs = _get_kwargs(
        domain_id=domain_id,
        type_=type_,
        host=host,
        destination=destination,
        page=page,
        per_page=per_page,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    domain_id: int,
    *,
    client: AuthenticatedClient,
    type_: str | Unset = UNSET,
    host: str | Unset = UNSET,
    destination: str | Unset = UNSET,
    page: int | Unset = 1,
    per_page: int | Unset = 20,
) -> ApiError | DnsRecordPaginatedListResponse | None:
    """List DNS records

     Get a list of all DNS Records. The results are paginated but the pagination does not have
    information about the total number of items and the total number of pages. Only forward pages
    navigation is supported.

    Args:
        domain_id (int):
        type_ (str | Unset):
        host (str | Unset):
        destination (str | Unset):
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | DnsRecordPaginatedListResponse
    """

    return sync_detailed(
        domain_id=domain_id,
        client=client,
        type_=type_,
        host=host,
        destination=destination,
        page=page,
        per_page=per_page,
    ).parsed


async def asyncio_detailed(
    domain_id: int,
    *,
    client: AuthenticatedClient,
    type_: str | Unset = UNSET,
    host: str | Unset = UNSET,
    destination: str | Unset = UNSET,
    page: int | Unset = 1,
    per_page: int | Unset = 20,
) -> Response[ApiError | DnsRecordPaginatedListResponse]:
    """List DNS records

     Get a list of all DNS Records. The results are paginated but the pagination does not have
    information about the total number of items and the total number of pages. Only forward pages
    navigation is supported.

    Args:
        domain_id (int):
        type_ (str | Unset):
        host (str | Unset):
        destination (str | Unset):
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | DnsRecordPaginatedListResponse]
    """

    kwargs = _get_kwargs(
        domain_id=domain_id,
        type_=type_,
        host=host,
        destination=destination,
        page=page,
        per_page=per_page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    domain_id: int,
    *,
    client: AuthenticatedClient,
    type_: str | Unset = UNSET,
    host: str | Unset = UNSET,
    destination: str | Unset = UNSET,
    page: int | Unset = 1,
    per_page: int | Unset = 20,
) -> ApiError | DnsRecordPaginatedListResponse | None:
    """List DNS records

     Get a list of all DNS Records. The results are paginated but the pagination does not have
    information about the total number of items and the total number of pages. Only forward pages
    navigation is supported.

    Args:
        domain_id (int):
        type_ (str | Unset):
        host (str | Unset):
        destination (str | Unset):
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | DnsRecordPaginatedListResponse
    """

    return (
        await asyncio_detailed(
            domain_id=domain_id,
            client=client,
            type_=type_,
            host=host,
            destination=destination,
            page=page,
            per_page=per_page,
        )
    ).parsed
