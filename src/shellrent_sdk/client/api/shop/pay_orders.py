from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.order_pay_request import OrderPayRequest
from ...models.pay_orders_response_200 import PayOrdersResponse200
from ...types import Response


def _get_kwargs(
    *,
    body: OrderPayRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v3/orders/pay",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | PayOrdersResponse200 | None:
    if response.status_code == 200:
        response_200 = PayOrdersResponse200.from_dict(response.json())

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
) -> Response[ApiError | PayOrdersResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: OrderPayRequest,
) -> Response[ApiError | PayOrdersResponse200]:
    """Pay Orders

     Pay one or more Orders. The response data is the payment, or null when there is nothing to pay
    (total amount to pay = 0.00).

    Args:
        body (OrderPayRequest): Pays one or more orders. The payment mode is chosen by three
            fields, evaluated in this order: 1) use_prepaid_credit set to true: pays with the
            available Prepaid Credit; 2) use_one_click set to true: tries the saved One-Click payment
            methods in priority order until one is successfully authorized; 3) one_click_id: pays with
            that specific One-Click payment method. Provide one of them: if more are provided, only
            the first one in this order is used. If none is provided the request fails, unless the
            amount to pay is zero: in that case no payment mode is needed.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | PayOrdersResponse200]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: OrderPayRequest,
) -> ApiError | PayOrdersResponse200 | None:
    """Pay Orders

     Pay one or more Orders. The response data is the payment, or null when there is nothing to pay
    (total amount to pay = 0.00).

    Args:
        body (OrderPayRequest): Pays one or more orders. The payment mode is chosen by three
            fields, evaluated in this order: 1) use_prepaid_credit set to true: pays with the
            available Prepaid Credit; 2) use_one_click set to true: tries the saved One-Click payment
            methods in priority order until one is successfully authorized; 3) one_click_id: pays with
            that specific One-Click payment method. Provide one of them: if more are provided, only
            the first one in this order is used. If none is provided the request fails, unless the
            amount to pay is zero: in that case no payment mode is needed.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | PayOrdersResponse200
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: OrderPayRequest,
) -> Response[ApiError | PayOrdersResponse200]:
    """Pay Orders

     Pay one or more Orders. The response data is the payment, or null when there is nothing to pay
    (total amount to pay = 0.00).

    Args:
        body (OrderPayRequest): Pays one or more orders. The payment mode is chosen by three
            fields, evaluated in this order: 1) use_prepaid_credit set to true: pays with the
            available Prepaid Credit; 2) use_one_click set to true: tries the saved One-Click payment
            methods in priority order until one is successfully authorized; 3) one_click_id: pays with
            that specific One-Click payment method. Provide one of them: if more are provided, only
            the first one in this order is used. If none is provided the request fails, unless the
            amount to pay is zero: in that case no payment mode is needed.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | PayOrdersResponse200]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: OrderPayRequest,
) -> ApiError | PayOrdersResponse200 | None:
    """Pay Orders

     Pay one or more Orders. The response data is the payment, or null when there is nothing to pay
    (total amount to pay = 0.00).

    Args:
        body (OrderPayRequest): Pays one or more orders. The payment mode is chosen by three
            fields, evaluated in this order: 1) use_prepaid_credit set to true: pays with the
            available Prepaid Credit; 2) use_one_click set to true: tries the saved One-Click payment
            methods in priority order until one is successfully authorized; 3) one_click_id: pays with
            that specific One-Click payment method. Provide one of them: if more are provided, only
            the first one in this order is used. If none is provided the request fails, unless the
            amount to pay is zero: in that case no payment mode is needed.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | PayOrdersResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
