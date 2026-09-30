from http import HTTPStatus
from io import BytesIO
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...types import UNSET, File, Response, Unset


def _get_kwargs(
    invoice_id: int,
    *,
    prefer_xml: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["prefer_xml"] = prefer_xml

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v3/invoices/{invoice_id}/download".format(
            invoice_id=quote(str(invoice_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | File | None:
    if response.status_code == 200:
        response_200 = File(payload=BytesIO(response.content))

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
) -> Response[ApiError | File]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    invoice_id: int,
    *,
    client: AuthenticatedClient,
    prefer_xml: bool | Unset = UNSET,
) -> Response[ApiError | File]:
    """Download invoice XML

     Download the XML file of an Invoice

    Args:
        invoice_id (int):
        prefer_xml (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | File]
    """

    kwargs = _get_kwargs(
        invoice_id=invoice_id,
        prefer_xml=prefer_xml,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    invoice_id: int,
    *,
    client: AuthenticatedClient,
    prefer_xml: bool | Unset = UNSET,
) -> ApiError | File | None:
    """Download invoice XML

     Download the XML file of an Invoice

    Args:
        invoice_id (int):
        prefer_xml (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | File
    """

    return sync_detailed(
        invoice_id=invoice_id,
        client=client,
        prefer_xml=prefer_xml,
    ).parsed


async def asyncio_detailed(
    invoice_id: int,
    *,
    client: AuthenticatedClient,
    prefer_xml: bool | Unset = UNSET,
) -> Response[ApiError | File]:
    """Download invoice XML

     Download the XML file of an Invoice

    Args:
        invoice_id (int):
        prefer_xml (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | File]
    """

    kwargs = _get_kwargs(
        invoice_id=invoice_id,
        prefer_xml=prefer_xml,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    invoice_id: int,
    *,
    client: AuthenticatedClient,
    prefer_xml: bool | Unset = UNSET,
) -> ApiError | File | None:
    """Download invoice XML

     Download the XML file of an Invoice

    Args:
        invoice_id (int):
        prefer_xml (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | File
    """

    return (
        await asyncio_detailed(
            invoice_id=invoice_id,
            client=client,
            prefer_xml=prefer_xml,
        )
    ).parsed
