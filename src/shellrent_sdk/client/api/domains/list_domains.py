from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.domain_paginated_list_response import DomainPaginatedListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    domain_full_name: str | Unset = UNSET,
    domain_name: str | Unset = UNSET,
    tld_id: int | Unset = UNSET,
    tld_extension: str | Unset = UNSET,
    page: int | Unset = 1,
    per_page: int | Unset = 20,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["domain_full_name"] = domain_full_name

    params["domain_name"] = domain_name

    params["tld_id"] = tld_id

    params["tld_extension"] = tld_extension

    params["page"] = page

    params["per_page"] = per_page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v3/domains",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | DomainPaginatedListResponse | None:
    if response.status_code == 200:
        response_200 = DomainPaginatedListResponse.from_dict(response.json())

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
) -> Response[ApiError | DomainPaginatedListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    domain_full_name: str | Unset = UNSET,
    domain_name: str | Unset = UNSET,
    tld_id: int | Unset = UNSET,
    tld_extension: str | Unset = UNSET,
    page: int | Unset = 1,
    per_page: int | Unset = 20,
) -> Response[ApiError | DomainPaginatedListResponse]:
    """List domains

     Get a list of all Domains

    Args:
        domain_full_name (str | Unset):
        domain_name (str | Unset):
        tld_id (int | Unset):
        tld_extension (str | Unset):
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | DomainPaginatedListResponse]
    """

    kwargs = _get_kwargs(
        domain_full_name=domain_full_name,
        domain_name=domain_name,
        tld_id=tld_id,
        tld_extension=tld_extension,
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
    domain_full_name: str | Unset = UNSET,
    domain_name: str | Unset = UNSET,
    tld_id: int | Unset = UNSET,
    tld_extension: str | Unset = UNSET,
    page: int | Unset = 1,
    per_page: int | Unset = 20,
) -> ApiError | DomainPaginatedListResponse | None:
    """List domains

     Get a list of all Domains

    Args:
        domain_full_name (str | Unset):
        domain_name (str | Unset):
        tld_id (int | Unset):
        tld_extension (str | Unset):
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | DomainPaginatedListResponse
    """

    return sync_detailed(
        client=client,
        domain_full_name=domain_full_name,
        domain_name=domain_name,
        tld_id=tld_id,
        tld_extension=tld_extension,
        page=page,
        per_page=per_page,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    domain_full_name: str | Unset = UNSET,
    domain_name: str | Unset = UNSET,
    tld_id: int | Unset = UNSET,
    tld_extension: str | Unset = UNSET,
    page: int | Unset = 1,
    per_page: int | Unset = 20,
) -> Response[ApiError | DomainPaginatedListResponse]:
    """List domains

     Get a list of all Domains

    Args:
        domain_full_name (str | Unset):
        domain_name (str | Unset):
        tld_id (int | Unset):
        tld_extension (str | Unset):
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | DomainPaginatedListResponse]
    """

    kwargs = _get_kwargs(
        domain_full_name=domain_full_name,
        domain_name=domain_name,
        tld_id=tld_id,
        tld_extension=tld_extension,
        page=page,
        per_page=per_page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    domain_full_name: str | Unset = UNSET,
    domain_name: str | Unset = UNSET,
    tld_id: int | Unset = UNSET,
    tld_extension: str | Unset = UNSET,
    page: int | Unset = 1,
    per_page: int | Unset = 20,
) -> ApiError | DomainPaginatedListResponse | None:
    """List domains

     Get a list of all Domains

    Args:
        domain_full_name (str | Unset):
        domain_name (str | Unset):
        tld_id (int | Unset):
        tld_extension (str | Unset):
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | DomainPaginatedListResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            domain_full_name=domain_full_name,
            domain_name=domain_name,
            tld_id=tld_id,
            tld_extension=tld_extension,
            page=page,
            per_page=per_page,
        )
    ).parsed
