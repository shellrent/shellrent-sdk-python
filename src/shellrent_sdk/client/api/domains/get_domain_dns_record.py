from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.dns_record_response import DnsRecordResponse
from ...types import Response


def _get_kwargs(
    domain_id: int,
    record_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v3/domains/{domain_id}/dns/records/{record_id}".format(
            domain_id=quote(str(domain_id), safe=""),
            record_id=quote(str(record_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | DnsRecordResponse | None:
    if response.status_code == 200:
        response_200 = DnsRecordResponse.from_dict(response.json())

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
) -> Response[ApiError | DnsRecordResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    domain_id: int,
    record_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ApiError | DnsRecordResponse]:
    """Get DNS record

     Get a DNS record

    Args:
        domain_id (int):
        record_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | DnsRecordResponse]
    """

    kwargs = _get_kwargs(
        domain_id=domain_id,
        record_id=record_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    domain_id: int,
    record_id: str,
    *,
    client: AuthenticatedClient,
) -> ApiError | DnsRecordResponse | None:
    """Get DNS record

     Get a DNS record

    Args:
        domain_id (int):
        record_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | DnsRecordResponse
    """

    return sync_detailed(
        domain_id=domain_id,
        record_id=record_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    domain_id: int,
    record_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ApiError | DnsRecordResponse]:
    """Get DNS record

     Get a DNS record

    Args:
        domain_id (int):
        record_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | DnsRecordResponse]
    """

    kwargs = _get_kwargs(
        domain_id=domain_id,
        record_id=record_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    domain_id: int,
    record_id: str,
    *,
    client: AuthenticatedClient,
) -> ApiError | DnsRecordResponse | None:
    """Get DNS record

     Get a DNS record

    Args:
        domain_id (int):
        record_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | DnsRecordResponse
    """

    return (
        await asyncio_detailed(
            domain_id=domain_id,
            record_id=record_id,
            client=client,
        )
    ).parsed
