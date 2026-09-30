from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.purchase_can_change_renew_status_response import PurchaseCanChangeRenewStatusResponse
from ...types import Response


def _get_kwargs(
    purchase_id: int,
    status: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v3/purchases/{purchase_id}/can-change-renew-status/{status}".format(
            purchase_id=quote(str(purchase_id), safe=""),
            status=quote(str(status), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | PurchaseCanChangeRenewStatusResponse | None:
    if response.status_code == 200:
        response_200 = PurchaseCanChangeRenewStatusResponse.from_dict(response.json())

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
) -> Response[ApiError | PurchaseCanChangeRenewStatusResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    purchase_id: int,
    status: str,
    *,
    client: AuthenticatedClient,
) -> Response[ApiError | PurchaseCanChangeRenewStatusResponse]:
    """Can change "to renew" status

     Know if it's possible to change the status of "do_not_renew" on purchase

    Args:
        purchase_id (int):
        status (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | PurchaseCanChangeRenewStatusResponse]
    """

    kwargs = _get_kwargs(
        purchase_id=purchase_id,
        status=status,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    purchase_id: int,
    status: str,
    *,
    client: AuthenticatedClient,
) -> ApiError | PurchaseCanChangeRenewStatusResponse | None:
    """Can change "to renew" status

     Know if it's possible to change the status of "do_not_renew" on purchase

    Args:
        purchase_id (int):
        status (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | PurchaseCanChangeRenewStatusResponse
    """

    return sync_detailed(
        purchase_id=purchase_id,
        status=status,
        client=client,
    ).parsed


async def asyncio_detailed(
    purchase_id: int,
    status: str,
    *,
    client: AuthenticatedClient,
) -> Response[ApiError | PurchaseCanChangeRenewStatusResponse]:
    """Can change "to renew" status

     Know if it's possible to change the status of "do_not_renew" on purchase

    Args:
        purchase_id (int):
        status (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | PurchaseCanChangeRenewStatusResponse]
    """

    kwargs = _get_kwargs(
        purchase_id=purchase_id,
        status=status,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    purchase_id: int,
    status: str,
    *,
    client: AuthenticatedClient,
) -> ApiError | PurchaseCanChangeRenewStatusResponse | None:
    """Can change "to renew" status

     Know if it's possible to change the status of "do_not_renew" on purchase

    Args:
        purchase_id (int):
        status (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | PurchaseCanChangeRenewStatusResponse
    """

    return (
        await asyncio_detailed(
            purchase_id=purchase_id,
            status=status,
            client=client,
        )
    ).parsed
