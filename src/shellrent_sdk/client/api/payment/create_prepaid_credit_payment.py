from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.payment_response import PaymentResponse
from ...models.prepaid_credit_payment_create_request import PrepaidCreditPaymentCreateRequest
from ...types import Response


def _get_kwargs(
    *,
    body: PrepaidCreditPaymentCreateRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v3/payments/prepaid-credit",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ApiError | PaymentResponse | None:
    if response.status_code == 201:
        response_201 = PaymentResponse.from_dict(response.json())

        return response_201

    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = ApiError.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ApiError.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = ApiError.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = ApiError.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ApiError.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = ApiError.from_dict(response.json())

        return response_409

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
) -> Response[Any | ApiError | PaymentResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PrepaidCreditPaymentCreateRequest,
) -> Response[Any | ApiError | PaymentResponse]:
    """Pay orders with the prepaid credit

     Pays one or more orders together with the prepaid credit. When there is nothing to pay (total 0.00)
    the orders are confirmed without a payment and the response is 204. The response is 409 when
    payments are not possible at this time, the orders cannot be paid together, the prepaid credit
    cannot be used for them (for example because it is not enough), or the payment exceeds the payment
    limits allowed at this time.

    Not available to sub-accounts: the response is 403 (error 1601).

    Args:
        body (PrepaidCreditPaymentCreateRequest): Pays one or more orders together with the
            prepaid credit

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ApiError | PaymentResponse]
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
    body: PrepaidCreditPaymentCreateRequest,
) -> Any | ApiError | PaymentResponse | None:
    """Pay orders with the prepaid credit

     Pays one or more orders together with the prepaid credit. When there is nothing to pay (total 0.00)
    the orders are confirmed without a payment and the response is 204. The response is 409 when
    payments are not possible at this time, the orders cannot be paid together, the prepaid credit
    cannot be used for them (for example because it is not enough), or the payment exceeds the payment
    limits allowed at this time.

    Not available to sub-accounts: the response is 403 (error 1601).

    Args:
        body (PrepaidCreditPaymentCreateRequest): Pays one or more orders together with the
            prepaid credit

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ApiError | PaymentResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PrepaidCreditPaymentCreateRequest,
) -> Response[Any | ApiError | PaymentResponse]:
    """Pay orders with the prepaid credit

     Pays one or more orders together with the prepaid credit. When there is nothing to pay (total 0.00)
    the orders are confirmed without a payment and the response is 204. The response is 409 when
    payments are not possible at this time, the orders cannot be paid together, the prepaid credit
    cannot be used for them (for example because it is not enough), or the payment exceeds the payment
    limits allowed at this time.

    Not available to sub-accounts: the response is 403 (error 1601).

    Args:
        body (PrepaidCreditPaymentCreateRequest): Pays one or more orders together with the
            prepaid credit

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ApiError | PaymentResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PrepaidCreditPaymentCreateRequest,
) -> Any | ApiError | PaymentResponse | None:
    """Pay orders with the prepaid credit

     Pays one or more orders together with the prepaid credit. When there is nothing to pay (total 0.00)
    the orders are confirmed without a payment and the response is 204. The response is 409 when
    payments are not possible at this time, the orders cannot be paid together, the prepaid credit
    cannot be used for them (for example because it is not enough), or the payment exceeds the payment
    limits allowed at this time.

    Not available to sub-accounts: the response is 403 (error 1601).

    Args:
        body (PrepaidCreditPaymentCreateRequest): Pays one or more orders together with the
            prepaid credit

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ApiError | PaymentResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
