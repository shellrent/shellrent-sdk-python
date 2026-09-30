from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.pec_owner_change_response import PecOwnerChangeResponse
from ...types import Response


def _get_kwargs(
    pec_domain_id: int,
    owner_change_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v3/pec-domains/{pec_domain_id}/owner-changes/{owner_change_id}".format(
            pec_domain_id=quote(str(pec_domain_id), safe=""),
            owner_change_id=quote(str(owner_change_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | PecOwnerChangeResponse | None:
    if response.status_code == 200:
        response_200 = PecOwnerChangeResponse.from_dict(response.json())

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
) -> Response[ApiError | PecOwnerChangeResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    pec_domain_id: int,
    owner_change_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[ApiError | PecOwnerChangeResponse]:
    """Get PEC domain owner change

     Get details of a specific owner change request for a PEC domain

    Args:
        pec_domain_id (int):
        owner_change_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | PecOwnerChangeResponse]
    """

    kwargs = _get_kwargs(
        pec_domain_id=pec_domain_id,
        owner_change_id=owner_change_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    pec_domain_id: int,
    owner_change_id: int,
    *,
    client: AuthenticatedClient,
) -> ApiError | PecOwnerChangeResponse | None:
    """Get PEC domain owner change

     Get details of a specific owner change request for a PEC domain

    Args:
        pec_domain_id (int):
        owner_change_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | PecOwnerChangeResponse
    """

    return sync_detailed(
        pec_domain_id=pec_domain_id,
        owner_change_id=owner_change_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    pec_domain_id: int,
    owner_change_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[ApiError | PecOwnerChangeResponse]:
    """Get PEC domain owner change

     Get details of a specific owner change request for a PEC domain

    Args:
        pec_domain_id (int):
        owner_change_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | PecOwnerChangeResponse]
    """

    kwargs = _get_kwargs(
        pec_domain_id=pec_domain_id,
        owner_change_id=owner_change_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    pec_domain_id: int,
    owner_change_id: int,
    *,
    client: AuthenticatedClient,
) -> ApiError | PecOwnerChangeResponse | None:
    """Get PEC domain owner change

     Get details of a specific owner change request for a PEC domain

    Args:
        pec_domain_id (int):
        owner_change_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | PecOwnerChangeResponse
    """

    return (
        await asyncio_detailed(
            pec_domain_id=pec_domain_id,
            owner_change_id=owner_change_id,
            client=client,
        )
    ).parsed
