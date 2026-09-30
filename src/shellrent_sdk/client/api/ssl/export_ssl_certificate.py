from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.ssl_certificate_export_response import SslCertificateExportResponse
from ...types import Response


def _get_kwargs(
    ssl_certificate_id: int,
    format_: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v3/ssl-certificates/{ssl_certificate_id}/export_format/{format_}".format(
            ssl_certificate_id=quote(str(ssl_certificate_id), safe=""),
            format_=quote(str(format_), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | SslCertificateExportResponse | None:
    if response.status_code == 200:
        response_200 = SslCertificateExportResponse.from_dict(response.json())

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
) -> Response[ApiError | SslCertificateExportResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    ssl_certificate_id: int,
    format_: str,
    *,
    client: AuthenticatedClient,
) -> Response[ApiError | SslCertificateExportResponse]:
    """Export SSL certificate keys

     Export SSL certificate keys

    Args:
        ssl_certificate_id (int):
        format_ (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | SslCertificateExportResponse]
    """

    kwargs = _get_kwargs(
        ssl_certificate_id=ssl_certificate_id,
        format_=format_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    ssl_certificate_id: int,
    format_: str,
    *,
    client: AuthenticatedClient,
) -> ApiError | SslCertificateExportResponse | None:
    """Export SSL certificate keys

     Export SSL certificate keys

    Args:
        ssl_certificate_id (int):
        format_ (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | SslCertificateExportResponse
    """

    return sync_detailed(
        ssl_certificate_id=ssl_certificate_id,
        format_=format_,
        client=client,
    ).parsed


async def asyncio_detailed(
    ssl_certificate_id: int,
    format_: str,
    *,
    client: AuthenticatedClient,
) -> Response[ApiError | SslCertificateExportResponse]:
    """Export SSL certificate keys

     Export SSL certificate keys

    Args:
        ssl_certificate_id (int):
        format_ (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | SslCertificateExportResponse]
    """

    kwargs = _get_kwargs(
        ssl_certificate_id=ssl_certificate_id,
        format_=format_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    ssl_certificate_id: int,
    format_: str,
    *,
    client: AuthenticatedClient,
) -> ApiError | SslCertificateExportResponse | None:
    """Export SSL certificate keys

     Export SSL certificate keys

    Args:
        ssl_certificate_id (int):
        format_ (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | SslCertificateExportResponse
    """

    return (
        await asyncio_detailed(
            ssl_certificate_id=ssl_certificate_id,
            format_=format_,
            client=client,
        )
    ).parsed
