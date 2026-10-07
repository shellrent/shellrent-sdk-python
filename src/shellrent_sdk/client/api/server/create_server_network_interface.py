from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.server_network_interface_create_request import ServerNetworkInterfaceCreateRequest
from ...models.task_response import TaskResponse
from ...types import Response


def _get_kwargs(
    server_id: int,
    *,
    body: ServerNetworkInterfaceCreateRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v3/servers/{server_id}/network-interfaces".format(
            server_id=quote(str(server_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | TaskResponse | None:
    if response.status_code == 202:
        response_202 = TaskResponse.from_dict(response.json())

        return response_202

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
) -> Response[ApiError | TaskResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    server_id: int,
    *,
    client: AuthenticatedClient,
    body: ServerNetworkInterfaceCreateRequest,
) -> Response[ApiError | TaskResponse]:
    """Create server network interface

     Starts the creation of a network interface: local, on an active local network of the cluster where
    the server resides, or public, on an IP address. The creation is asynchronous and is returned as a
    Task.

    Args:
        server_id (int):
        body (ServerNetworkInterfaceCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | TaskResponse]
    """

    kwargs = _get_kwargs(
        server_id=server_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    server_id: int,
    *,
    client: AuthenticatedClient,
    body: ServerNetworkInterfaceCreateRequest,
) -> ApiError | TaskResponse | None:
    """Create server network interface

     Starts the creation of a network interface: local, on an active local network of the cluster where
    the server resides, or public, on an IP address. The creation is asynchronous and is returned as a
    Task.

    Args:
        server_id (int):
        body (ServerNetworkInterfaceCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | TaskResponse
    """

    return sync_detailed(
        server_id=server_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    server_id: int,
    *,
    client: AuthenticatedClient,
    body: ServerNetworkInterfaceCreateRequest,
) -> Response[ApiError | TaskResponse]:
    """Create server network interface

     Starts the creation of a network interface: local, on an active local network of the cluster where
    the server resides, or public, on an IP address. The creation is asynchronous and is returned as a
    Task.

    Args:
        server_id (int):
        body (ServerNetworkInterfaceCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | TaskResponse]
    """

    kwargs = _get_kwargs(
        server_id=server_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    server_id: int,
    *,
    client: AuthenticatedClient,
    body: ServerNetworkInterfaceCreateRequest,
) -> ApiError | TaskResponse | None:
    """Create server network interface

     Starts the creation of a network interface: local, on an active local network of the cluster where
    the server resides, or public, on an IP address. The creation is asynchronous and is returned as a
    Task.

    Args:
        server_id (int):
        body (ServerNetworkInterfaceCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | TaskResponse
    """

    return (
        await asyncio_detailed(
            server_id=server_id,
            client=client,
            body=body,
        )
    ).parsed
