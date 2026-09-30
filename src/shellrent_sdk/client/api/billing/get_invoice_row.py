from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.invoice_row_response import InvoiceRowResponse
from ...types import Response


def _get_kwargs(
    invoice_id: int,
    row_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v3/invoices/{invoice_id}/rows/{row_id}".format(
            invoice_id=quote(str(invoice_id), safe=""),
            row_id=quote(str(row_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | InvoiceRowResponse | None:
    if response.status_code == 200:
        response_200 = InvoiceRowResponse.from_dict(response.json())

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
) -> Response[ApiError | InvoiceRowResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    invoice_id: int,
    row_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[ApiError | InvoiceRowResponse]:
    """Get an invoice row

     Get details of an Invoice row

    Args:
        invoice_id (int):
        row_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | InvoiceRowResponse]
    """

    kwargs = _get_kwargs(
        invoice_id=invoice_id,
        row_id=row_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    invoice_id: int,
    row_id: int,
    *,
    client: AuthenticatedClient,
) -> ApiError | InvoiceRowResponse | None:
    """Get an invoice row

     Get details of an Invoice row

    Args:
        invoice_id (int):
        row_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | InvoiceRowResponse
    """

    return sync_detailed(
        invoice_id=invoice_id,
        row_id=row_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    invoice_id: int,
    row_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[ApiError | InvoiceRowResponse]:
    """Get an invoice row

     Get details of an Invoice row

    Args:
        invoice_id (int):
        row_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | InvoiceRowResponse]
    """

    kwargs = _get_kwargs(
        invoice_id=invoice_id,
        row_id=row_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    invoice_id: int,
    row_id: int,
    *,
    client: AuthenticatedClient,
) -> ApiError | InvoiceRowResponse | None:
    """Get an invoice row

     Get details of an Invoice row

    Args:
        invoice_id (int):
        row_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | InvoiceRowResponse
    """

    return (
        await asyncio_detailed(
            invoice_id=invoice_id,
            row_id=row_id,
            client=client,
        )
    ).parsed
