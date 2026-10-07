from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.order_can_pay_response import OrderCanPayResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    order_id: int,
    *,
    one_click_id: int | Unset = UNSET,
    prepaid_credit: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["one_click_id"] = one_click_id

    params["prepaid_credit"] = prepaid_credit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v3/orders/{order_id}/can-pay".format(
            order_id=quote(str(order_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | OrderCanPayResponse | None:
    if response.status_code == 200:
        response_200 = OrderCanPayResponse.from_dict(response.json())

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

    if response.status_code == 500:
        response_500 = ApiError.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ApiError | OrderCanPayResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    order_id: int,
    *,
    client: AuthenticatedClient,
    one_click_id: int | Unset = UNSET,
    prepaid_credit: bool | Unset = UNSET,
) -> Response[ApiError | OrderCanPayResponse]:
    """Can pay Order

     Whether the order can be paid now with a payment method, with the amount to pay, commission of the
    method included, and the orders paid together with it. Send either `one_click_id` or
    `prepaid_credit=true` (400 otherwise). `can_pay` is false when the order cannot be paid now, when
    the One-Click method is not active or has expired, or when the prepaid credit cannot be used for
    these orders or is not enough. 404 when the One-Click method does not exist or belongs to another
    account

    Not available to sub-accounts: the response is 403 (error 1601).

    Args:
        order_id (int):
        one_click_id (int | Unset):
        prepaid_credit (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | OrderCanPayResponse]
    """

    kwargs = _get_kwargs(
        order_id=order_id,
        one_click_id=one_click_id,
        prepaid_credit=prepaid_credit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    order_id: int,
    *,
    client: AuthenticatedClient,
    one_click_id: int | Unset = UNSET,
    prepaid_credit: bool | Unset = UNSET,
) -> ApiError | OrderCanPayResponse | None:
    """Can pay Order

     Whether the order can be paid now with a payment method, with the amount to pay, commission of the
    method included, and the orders paid together with it. Send either `one_click_id` or
    `prepaid_credit=true` (400 otherwise). `can_pay` is false when the order cannot be paid now, when
    the One-Click method is not active or has expired, or when the prepaid credit cannot be used for
    these orders or is not enough. 404 when the One-Click method does not exist or belongs to another
    account

    Not available to sub-accounts: the response is 403 (error 1601).

    Args:
        order_id (int):
        one_click_id (int | Unset):
        prepaid_credit (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | OrderCanPayResponse
    """

    return sync_detailed(
        order_id=order_id,
        client=client,
        one_click_id=one_click_id,
        prepaid_credit=prepaid_credit,
    ).parsed


async def asyncio_detailed(
    order_id: int,
    *,
    client: AuthenticatedClient,
    one_click_id: int | Unset = UNSET,
    prepaid_credit: bool | Unset = UNSET,
) -> Response[ApiError | OrderCanPayResponse]:
    """Can pay Order

     Whether the order can be paid now with a payment method, with the amount to pay, commission of the
    method included, and the orders paid together with it. Send either `one_click_id` or
    `prepaid_credit=true` (400 otherwise). `can_pay` is false when the order cannot be paid now, when
    the One-Click method is not active or has expired, or when the prepaid credit cannot be used for
    these orders or is not enough. 404 when the One-Click method does not exist or belongs to another
    account

    Not available to sub-accounts: the response is 403 (error 1601).

    Args:
        order_id (int):
        one_click_id (int | Unset):
        prepaid_credit (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | OrderCanPayResponse]
    """

    kwargs = _get_kwargs(
        order_id=order_id,
        one_click_id=one_click_id,
        prepaid_credit=prepaid_credit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    order_id: int,
    *,
    client: AuthenticatedClient,
    one_click_id: int | Unset = UNSET,
    prepaid_credit: bool | Unset = UNSET,
) -> ApiError | OrderCanPayResponse | None:
    """Can pay Order

     Whether the order can be paid now with a payment method, with the amount to pay, commission of the
    method included, and the orders paid together with it. Send either `one_click_id` or
    `prepaid_credit=true` (400 otherwise). `can_pay` is false when the order cannot be paid now, when
    the One-Click method is not active or has expired, or when the prepaid credit cannot be used for
    these orders or is not enough. 404 when the One-Click method does not exist or belongs to another
    account

    Not available to sub-accounts: the response is 403 (error 1601).

    Args:
        order_id (int):
        one_click_id (int | Unset):
        prepaid_credit (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | OrderCanPayResponse
    """

    return (
        await asyncio_detailed(
            order_id=order_id,
            client=client,
            one_click_id=one_click_id,
            prepaid_credit=prepaid_credit,
        )
    ).parsed
