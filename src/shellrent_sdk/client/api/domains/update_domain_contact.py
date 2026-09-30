from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.domain_contact_request import DomainContactRequest
from ...models.domain_contact_response import DomainContactResponse
from ...types import Response


def _get_kwargs(
    domain_id: int,
    domain_contact_id: int,
    *,
    body: DomainContactRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v3/domains/{domain_id}/contacts/{domain_contact_id}".format(
            domain_id=quote(str(domain_id), safe=""),
            domain_contact_id=quote(str(domain_contact_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | DomainContactResponse | None:
    if response.status_code == 200:
        response_200 = DomainContactResponse.from_dict(response.json())

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
) -> Response[ApiError | DomainContactResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    domain_id: int,
    domain_contact_id: int,
    *,
    client: AuthenticatedClient,
    body: DomainContactRequest,
) -> Response[ApiError | DomainContactResponse]:
    """Modify contact

     Modify a contact's data

    Args:
        domain_id (int):
        domain_contact_id (int):
        body (DomainContactRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | DomainContactResponse]
    """

    kwargs = _get_kwargs(
        domain_id=domain_id,
        domain_contact_id=domain_contact_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    domain_id: int,
    domain_contact_id: int,
    *,
    client: AuthenticatedClient,
    body: DomainContactRequest,
) -> ApiError | DomainContactResponse | None:
    """Modify contact

     Modify a contact's data

    Args:
        domain_id (int):
        domain_contact_id (int):
        body (DomainContactRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | DomainContactResponse
    """

    return sync_detailed(
        domain_id=domain_id,
        domain_contact_id=domain_contact_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    domain_id: int,
    domain_contact_id: int,
    *,
    client: AuthenticatedClient,
    body: DomainContactRequest,
) -> Response[ApiError | DomainContactResponse]:
    """Modify contact

     Modify a contact's data

    Args:
        domain_id (int):
        domain_contact_id (int):
        body (DomainContactRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | DomainContactResponse]
    """

    kwargs = _get_kwargs(
        domain_id=domain_id,
        domain_contact_id=domain_contact_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    domain_id: int,
    domain_contact_id: int,
    *,
    client: AuthenticatedClient,
    body: DomainContactRequest,
) -> ApiError | DomainContactResponse | None:
    """Modify contact

     Modify a contact's data

    Args:
        domain_id (int):
        domain_contact_id (int):
        body (DomainContactRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | DomainContactResponse
    """

    return (
        await asyncio_detailed(
            domain_id=domain_id,
            domain_contact_id=domain_contact_id,
            client=client,
            body=body,
        )
    ).parsed
