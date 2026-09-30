from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.sms_create_request import SmsCreateRequest
from ...models.sms_response import SmsResponse
from ...types import Response


def _get_kwargs(
    *,
    body: SmsCreateRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v3/sms",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | SmsResponse | None:
    if response.status_code == 200:
        response_200 = SmsResponse.from_dict(response.json())

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
) -> Response[ApiError | SmsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: SmsCreateRequest,
) -> Response[ApiError | SmsResponse]:
    """Send an SMS

     Send a new SMS

    Args:
        body (SmsCreateRequest): Sends an SMS. Recipients: provide exactly one of phone_numbers or
            phonebooks, not both. Sender: required when quality is PREMIUM (from 2 to 11 characters),
            ignored when quality is STANDARD.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | SmsResponse]
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
    body: SmsCreateRequest,
) -> ApiError | SmsResponse | None:
    """Send an SMS

     Send a new SMS

    Args:
        body (SmsCreateRequest): Sends an SMS. Recipients: provide exactly one of phone_numbers or
            phonebooks, not both. Sender: required when quality is PREMIUM (from 2 to 11 characters),
            ignored when quality is STANDARD.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | SmsResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: SmsCreateRequest,
) -> Response[ApiError | SmsResponse]:
    """Send an SMS

     Send a new SMS

    Args:
        body (SmsCreateRequest): Sends an SMS. Recipients: provide exactly one of phone_numbers or
            phonebooks, not both. Sender: required when quality is PREMIUM (from 2 to 11 characters),
            ignored when quality is STANDARD.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | SmsResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: SmsCreateRequest,
) -> ApiError | SmsResponse | None:
    """Send an SMS

     Send a new SMS

    Args:
        body (SmsCreateRequest): Sends an SMS. Recipients: provide exactly one of phone_numbers or
            phonebooks, not both. Sender: required when quality is PREMIUM (from 2 to 11 characters),
            ignored when quality is STANDARD.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | SmsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
