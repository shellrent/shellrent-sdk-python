from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.tld_paginated_list_response import TldPaginatedListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    extension: str | Unset = UNSET,
    extension_exact: str | Unset = UNSET,
    is_it: bool | Unset = UNSET,
    country: str | Unset = UNSET,
    page: int | Unset = 1,
    per_page: int | Unset = 15,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["extension"] = extension

    params["extension_exact"] = extension_exact

    params["is_it"] = is_it

    params["country"] = country

    params["page"] = page

    params["per_page"] = per_page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v3/tlds",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | TldPaginatedListResponse | None:
    if response.status_code == 200:
        response_200 = TldPaginatedListResponse.from_dict(response.json())

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
) -> Response[ApiError | TldPaginatedListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    extension: str | Unset = UNSET,
    extension_exact: str | Unset = UNSET,
    is_it: bool | Unset = UNSET,
    country: str | Unset = UNSET,
    page: int | Unset = 1,
    per_page: int | Unset = 15,
) -> Response[ApiError | TldPaginatedListResponse]:
    """List all TLDs

     Get a list of all TLD extensions for domains

    Args:
        extension (str | Unset):
        extension_exact (str | Unset):
        is_it (bool | Unset):
        country (str | Unset):
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 15.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | TldPaginatedListResponse]
    """

    kwargs = _get_kwargs(
        extension=extension,
        extension_exact=extension_exact,
        is_it=is_it,
        country=country,
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
    extension: str | Unset = UNSET,
    extension_exact: str | Unset = UNSET,
    is_it: bool | Unset = UNSET,
    country: str | Unset = UNSET,
    page: int | Unset = 1,
    per_page: int | Unset = 15,
) -> ApiError | TldPaginatedListResponse | None:
    """List all TLDs

     Get a list of all TLD extensions for domains

    Args:
        extension (str | Unset):
        extension_exact (str | Unset):
        is_it (bool | Unset):
        country (str | Unset):
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 15.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | TldPaginatedListResponse
    """

    return sync_detailed(
        client=client,
        extension=extension,
        extension_exact=extension_exact,
        is_it=is_it,
        country=country,
        page=page,
        per_page=per_page,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    extension: str | Unset = UNSET,
    extension_exact: str | Unset = UNSET,
    is_it: bool | Unset = UNSET,
    country: str | Unset = UNSET,
    page: int | Unset = 1,
    per_page: int | Unset = 15,
) -> Response[ApiError | TldPaginatedListResponse]:
    """List all TLDs

     Get a list of all TLD extensions for domains

    Args:
        extension (str | Unset):
        extension_exact (str | Unset):
        is_it (bool | Unset):
        country (str | Unset):
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 15.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | TldPaginatedListResponse]
    """

    kwargs = _get_kwargs(
        extension=extension,
        extension_exact=extension_exact,
        is_it=is_it,
        country=country,
        page=page,
        per_page=per_page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    extension: str | Unset = UNSET,
    extension_exact: str | Unset = UNSET,
    is_it: bool | Unset = UNSET,
    country: str | Unset = UNSET,
    page: int | Unset = 1,
    per_page: int | Unset = 15,
) -> ApiError | TldPaginatedListResponse | None:
    """List all TLDs

     Get a list of all TLD extensions for domains

    Args:
        extension (str | Unset):
        extension_exact (str | Unset):
        is_it (bool | Unset):
        country (str | Unset):
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 15.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | TldPaginatedListResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            extension=extension,
            extension_exact=extension_exact,
            is_it=is_it,
            country=country,
            page=page,
            per_page=per_page,
        )
    ).parsed
