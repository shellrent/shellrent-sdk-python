from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.creditnote_response import CreditnoteResponse
from ...types import Response


def _get_kwargs(
    credit_note_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v3/credit-notes/{credit_note_id}".format(
            credit_note_id=quote(str(credit_note_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | CreditnoteResponse | None:
    if response.status_code == 200:
        response_200 = CreditnoteResponse.from_dict(response.json())

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
) -> Response[ApiError | CreditnoteResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    credit_note_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[ApiError | CreditnoteResponse]:
    """Get a Credit note

     Get details of a credit note

    Not available to sub-accounts: the response is 403 (error 1601).

    Args:
        credit_note_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | CreditnoteResponse]
    """

    kwargs = _get_kwargs(
        credit_note_id=credit_note_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    credit_note_id: int,
    *,
    client: AuthenticatedClient,
) -> ApiError | CreditnoteResponse | None:
    """Get a Credit note

     Get details of a credit note

    Not available to sub-accounts: the response is 403 (error 1601).

    Args:
        credit_note_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | CreditnoteResponse
    """

    return sync_detailed(
        credit_note_id=credit_note_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    credit_note_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[ApiError | CreditnoteResponse]:
    """Get a Credit note

     Get details of a credit note

    Not available to sub-accounts: the response is 403 (error 1601).

    Args:
        credit_note_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | CreditnoteResponse]
    """

    kwargs = _get_kwargs(
        credit_note_id=credit_note_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    credit_note_id: int,
    *,
    client: AuthenticatedClient,
) -> ApiError | CreditnoteResponse | None:
    """Get a Credit note

     Get details of a credit note

    Not available to sub-accounts: the response is 403 (error 1601).

    Args:
        credit_note_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | CreditnoteResponse
    """

    return (
        await asyncio_detailed(
            credit_note_id=credit_note_id,
            client=client,
        )
    ).parsed
