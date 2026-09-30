from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.ssl_certificate_change_csr_request import SslCertificateChangeCsrRequest
from ...models.ssl_certificate_key_response import SslCertificateKeyResponse
from ...types import Response


def _get_kwargs(
    ssl_certificate_id: int,
    *,
    body: SslCertificateChangeCsrRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v3/ssl-certificates/{ssl_certificate_id}/csr".format(
            ssl_certificate_id=quote(str(ssl_certificate_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | SslCertificateKeyResponse | None:
    if response.status_code == 200:
        response_200 = SslCertificateKeyResponse.from_dict(response.json())

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
) -> Response[ApiError | SslCertificateKeyResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    ssl_certificate_id: int,
    *,
    client: AuthenticatedClient,
    body: SslCertificateChangeCsrRequest,
) -> Response[ApiError | SslCertificateKeyResponse]:
    """Change SSL certificate CSR

     Change SSL certificate CSR

    Args:
        ssl_certificate_id (int):
        body (SslCertificateChangeCsrRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | SslCertificateKeyResponse]
    """

    kwargs = _get_kwargs(
        ssl_certificate_id=ssl_certificate_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    ssl_certificate_id: int,
    *,
    client: AuthenticatedClient,
    body: SslCertificateChangeCsrRequest,
) -> ApiError | SslCertificateKeyResponse | None:
    """Change SSL certificate CSR

     Change SSL certificate CSR

    Args:
        ssl_certificate_id (int):
        body (SslCertificateChangeCsrRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | SslCertificateKeyResponse
    """

    return sync_detailed(
        ssl_certificate_id=ssl_certificate_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    ssl_certificate_id: int,
    *,
    client: AuthenticatedClient,
    body: SslCertificateChangeCsrRequest,
) -> Response[ApiError | SslCertificateKeyResponse]:
    """Change SSL certificate CSR

     Change SSL certificate CSR

    Args:
        ssl_certificate_id (int):
        body (SslCertificateChangeCsrRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | SslCertificateKeyResponse]
    """

    kwargs = _get_kwargs(
        ssl_certificate_id=ssl_certificate_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    ssl_certificate_id: int,
    *,
    client: AuthenticatedClient,
    body: SslCertificateChangeCsrRequest,
) -> ApiError | SslCertificateKeyResponse | None:
    """Change SSL certificate CSR

     Change SSL certificate CSR

    Args:
        ssl_certificate_id (int):
        body (SslCertificateChangeCsrRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | SslCertificateKeyResponse
    """

    return (
        await asyncio_detailed(
            ssl_certificate_id=ssl_certificate_id,
            client=client,
            body=body,
        )
    ).parsed
