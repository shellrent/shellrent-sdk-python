from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.microsoft_365_subscription_quantity_request import (
    Microsoft365SubscriptionQuantityRequest,
)
from ...models.order_response import OrderResponse
from ...types import Response


def _get_kwargs(
    microsoft365_id: int,
    *,
    body: Microsoft365SubscriptionQuantityRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v3/microsoft365-subscriptions/{microsoft365_id}/quantity-upgrade".format(
            microsoft365_id=quote(str(microsoft365_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | OrderResponse | None:
    if response.status_code == 200:
        response_200 = OrderResponse.from_dict(response.json())

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
) -> Response[ApiError | OrderResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    microsoft365_id: int,
    *,
    client: AuthenticatedClient,
    body: Microsoft365SubscriptionQuantityRequest,
) -> Response[ApiError | OrderResponse]:
    """Upgrade Microsoft 365 subscription quantity

     Increase the Microsoft 365 seats quantity. Returns the generated Order to pay the additional seats.

    Args:
        microsoft365_id (int):
        body (Microsoft365SubscriptionQuantityRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | OrderResponse]
    """

    kwargs = _get_kwargs(
        microsoft365_id=microsoft365_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    microsoft365_id: int,
    *,
    client: AuthenticatedClient,
    body: Microsoft365SubscriptionQuantityRequest,
) -> ApiError | OrderResponse | None:
    """Upgrade Microsoft 365 subscription quantity

     Increase the Microsoft 365 seats quantity. Returns the generated Order to pay the additional seats.

    Args:
        microsoft365_id (int):
        body (Microsoft365SubscriptionQuantityRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | OrderResponse
    """

    return sync_detailed(
        microsoft365_id=microsoft365_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    microsoft365_id: int,
    *,
    client: AuthenticatedClient,
    body: Microsoft365SubscriptionQuantityRequest,
) -> Response[ApiError | OrderResponse]:
    """Upgrade Microsoft 365 subscription quantity

     Increase the Microsoft 365 seats quantity. Returns the generated Order to pay the additional seats.

    Args:
        microsoft365_id (int):
        body (Microsoft365SubscriptionQuantityRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | OrderResponse]
    """

    kwargs = _get_kwargs(
        microsoft365_id=microsoft365_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    microsoft365_id: int,
    *,
    client: AuthenticatedClient,
    body: Microsoft365SubscriptionQuantityRequest,
) -> ApiError | OrderResponse | None:
    """Upgrade Microsoft 365 subscription quantity

     Increase the Microsoft 365 seats quantity. Returns the generated Order to pay the additional seats.

    Args:
        microsoft365_id (int):
        body (Microsoft365SubscriptionQuantityRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | OrderResponse
    """

    return (
        await asyncio_detailed(
            microsoft365_id=microsoft365_id,
            client=client,
            body=body,
        )
    ).parsed
