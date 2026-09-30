from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.sms_phonebook_add_contacts_request import SmsPhonebookAddContactsRequest
from ...models.sms_phonebook_response import SmsPhonebookResponse
from ...types import Response


def _get_kwargs(
    phonebook_id: int,
    *,
    body: SmsPhonebookAddContactsRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v3/sms/phonebooks/{phonebook_id}/contacts".format(
            phonebook_id=quote(str(phonebook_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | SmsPhonebookResponse | None:
    if response.status_code == 200:
        response_200 = SmsPhonebookResponse.from_dict(response.json())

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
) -> Response[ApiError | SmsPhonebookResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    phonebook_id: int,
    *,
    client: AuthenticatedClient,
    body: SmsPhonebookAddContactsRequest,
) -> Response[ApiError | SmsPhonebookResponse]:
    """Replace all Contacts in Phonebook

     Replaces all the Contacts in a Phonebook

    Args:
        phonebook_id (int):
        body (SmsPhonebookAddContactsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | SmsPhonebookResponse]
    """

    kwargs = _get_kwargs(
        phonebook_id=phonebook_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    phonebook_id: int,
    *,
    client: AuthenticatedClient,
    body: SmsPhonebookAddContactsRequest,
) -> ApiError | SmsPhonebookResponse | None:
    """Replace all Contacts in Phonebook

     Replaces all the Contacts in a Phonebook

    Args:
        phonebook_id (int):
        body (SmsPhonebookAddContactsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | SmsPhonebookResponse
    """

    return sync_detailed(
        phonebook_id=phonebook_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    phonebook_id: int,
    *,
    client: AuthenticatedClient,
    body: SmsPhonebookAddContactsRequest,
) -> Response[ApiError | SmsPhonebookResponse]:
    """Replace all Contacts in Phonebook

     Replaces all the Contacts in a Phonebook

    Args:
        phonebook_id (int):
        body (SmsPhonebookAddContactsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | SmsPhonebookResponse]
    """

    kwargs = _get_kwargs(
        phonebook_id=phonebook_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    phonebook_id: int,
    *,
    client: AuthenticatedClient,
    body: SmsPhonebookAddContactsRequest,
) -> ApiError | SmsPhonebookResponse | None:
    """Replace all Contacts in Phonebook

     Replaces all the Contacts in a Phonebook

    Args:
        phonebook_id (int):
        body (SmsPhonebookAddContactsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | SmsPhonebookResponse
    """

    return (
        await asyncio_detailed(
            phonebook_id=phonebook_id,
            client=client,
            body=body,
        )
    ).parsed
