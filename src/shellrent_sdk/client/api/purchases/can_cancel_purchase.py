from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.purchase_can_cancel_response import PurchaseCanCancelResponse
from ...types import Response


def _get_kwargs(
    purchase_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v3/purchases/{purchase_id}/can-cancel".format(
            purchase_id=quote(str(purchase_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | PurchaseCanCancelResponse | None:
    if response.status_code == 200:
        response_200 = PurchaseCanCancelResponse.from_dict(response.json())

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
) -> Response[ApiError | PurchaseCanCancelResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    purchase_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[ApiError | PurchaseCanCancelResponse]:
    """Can cancel

     Know if it's possible to cancel a purchase

    Args:
        purchase_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | PurchaseCanCancelResponse]
    """

    kwargs = _get_kwargs(
        purchase_id=purchase_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    purchase_id: int,
    *,
    client: AuthenticatedClient,
) -> ApiError | PurchaseCanCancelResponse | None:
    """Can cancel

     Know if it's possible to cancel a purchase

    Args:
        purchase_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | PurchaseCanCancelResponse
    """

    return sync_detailed(
        purchase_id=purchase_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    purchase_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[ApiError | PurchaseCanCancelResponse]:
    """Can cancel

     Know if it's possible to cancel a purchase

    Args:
        purchase_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | PurchaseCanCancelResponse]
    """

    kwargs = _get_kwargs(
        purchase_id=purchase_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    purchase_id: int,
    *,
    client: AuthenticatedClient,
) -> ApiError | PurchaseCanCancelResponse | None:
    """Can cancel

     Know if it's possible to cancel a purchase

    Args:
        purchase_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | PurchaseCanCancelResponse
    """

    return (
        await asyncio_detailed(
            purchase_id=purchase_id,
            client=client,
        )
    ).parsed
