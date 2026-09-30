from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.server_monitoring_probe_response import ServerMonitoringProbeResponse
from ...models.server_monitoring_probe_update_request import ServerMonitoringProbeUpdateRequest
from ...types import Response


def _get_kwargs(
    server_monitoring_id: int,
    probe_id: int,
    *,
    body: ServerMonitoringProbeUpdateRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v3/server-monitorings/{server_monitoring_id}/probes/{probe_id}".format(
            server_monitoring_id=quote(str(server_monitoring_id), safe=""),
            probe_id=quote(str(probe_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | ServerMonitoringProbeResponse | None:
    if response.status_code == 200:
        response_200 = ServerMonitoringProbeResponse.from_dict(response.json())

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
) -> Response[ApiError | ServerMonitoringProbeResponse]:
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
    body: ServerMonitoringProbeUpdateRequest,
) -> Response[ApiError | ServerMonitoringProbeResponse]:
    """Update server monitoring probe

     Update a probe associated with a server monitoring

    Args:
        server_monitoring_id (int):
        probe_id (int):
        body (ServerMonitoringProbeUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | ServerMonitoringProbeResponse]
    """

    kwargs = _get_kwargs(
        server_monitoring_id=server_monitoring_id,
        probe_id=probe_id,
        body=body,
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
    body: ServerMonitoringProbeUpdateRequest,
) -> ApiError | ServerMonitoringProbeResponse | None:
    """Update server monitoring probe

     Update a probe associated with a server monitoring

    Args:
        server_monitoring_id (int):
        probe_id (int):
        body (ServerMonitoringProbeUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | ServerMonitoringProbeResponse
    """

    return sync_detailed(
        server_monitoring_id=server_monitoring_id,
        probe_id=probe_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    server_monitoring_id: int,
    probe_id: int,
    *,
    client: AuthenticatedClient,
    body: ServerMonitoringProbeUpdateRequest,
) -> Response[ApiError | ServerMonitoringProbeResponse]:
    """Update server monitoring probe

     Update a probe associated with a server monitoring

    Args:
        server_monitoring_id (int):
        probe_id (int):
        body (ServerMonitoringProbeUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | ServerMonitoringProbeResponse]
    """

    kwargs = _get_kwargs(
        server_monitoring_id=server_monitoring_id,
        probe_id=probe_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    server_monitoring_id: int,
    probe_id: int,
    *,
    client: AuthenticatedClient,
    body: ServerMonitoringProbeUpdateRequest,
) -> ApiError | ServerMonitoringProbeResponse | None:
    """Update server monitoring probe

     Update a probe associated with a server monitoring

    Args:
        server_monitoring_id (int):
        probe_id (int):
        body (ServerMonitoringProbeUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | ServerMonitoringProbeResponse
    """

    return (
        await asyncio_detailed(
            server_monitoring_id=server_monitoring_id,
            probe_id=probe_id,
            client=client,
            body=body,
        )
    ).parsed
