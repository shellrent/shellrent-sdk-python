from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...types import Response


def _get_kwargs(
    server_monitoring_id: int,
    probe_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/v3/server-monitorings/{server_monitoring_id}/probes/{probe_id}".format(
            server_monitoring_id=quote(str(server_monitoring_id), safe=""),
            probe_id=quote(str(probe_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ApiError | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

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
) -> Response[Any | ApiError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    server_monitoring_id: int,
    probe_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | ApiError]:
    """Delete server monitoring probe

     Delete a probe associated with a server monitoring

    Args:
        server_monitoring_id (int):
        probe_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ApiError]
    """

    kwargs = _get_kwargs(
        server_monitoring_id=server_monitoring_id,
        probe_id=probe_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    server_monitoring_id: int,
    probe_id: int,
    *,
    client: AuthenticatedClient,
) -> Any | ApiError | None:
    """Delete server monitoring probe

     Delete a probe associated with a server monitoring

    Args:
        server_monitoring_id (int):
        probe_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ApiError
    """

    return sync_detailed(
        server_monitoring_id=server_monitoring_id,
        probe_id=probe_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    server_monitoring_id: int,
    probe_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | ApiError]:
    """Delete server monitoring probe

     Delete a probe associated with a server monitoring

    Args:
        server_monitoring_id (int):
        probe_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ApiError]
    """

    kwargs = _get_kwargs(
        server_monitoring_id=server_monitoring_id,
        probe_id=probe_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    server_monitoring_id: int,
    probe_id: int,
    *,
    client: AuthenticatedClient,
) -> Any | ApiError | None:
    """Delete server monitoring probe

     Delete a probe associated with a server monitoring

    Args:
        server_monitoring_id (int):
        probe_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ApiError
    """

    return (
        await asyncio_detailed(
            server_monitoring_id=server_monitoring_id,
            probe_id=probe_id,
            client=client,
        )
    ).parsed
