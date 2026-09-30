from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.web_monitoring_response_time_chart_response import (
    WebMonitoringResponseTimeChartResponse,
)
from ...types import Response


def _get_kwargs(
    web_monitoring_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v3/web-monitorings/{web_monitoring_id}/charts/response-time".format(
            web_monitoring_id=quote(str(web_monitoring_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | WebMonitoringResponseTimeChartResponse | None:
    if response.status_code == 200:
        response_200 = WebMonitoringResponseTimeChartResponse.from_dict(response.json())

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
) -> Response[ApiError | WebMonitoringResponseTimeChartResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    web_monitoring_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[ApiError | WebMonitoringResponseTimeChartResponse]:
    """Get web monitoring response time chart

     Get response time chart points for a web monitoring service

    Args:
        web_monitoring_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | WebMonitoringResponseTimeChartResponse]
    """

    kwargs = _get_kwargs(
        web_monitoring_id=web_monitoring_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    web_monitoring_id: int,
    *,
    client: AuthenticatedClient,
) -> ApiError | WebMonitoringResponseTimeChartResponse | None:
    """Get web monitoring response time chart

     Get response time chart points for a web monitoring service

    Args:
        web_monitoring_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | WebMonitoringResponseTimeChartResponse
    """

    return sync_detailed(
        web_monitoring_id=web_monitoring_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    web_monitoring_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[ApiError | WebMonitoringResponseTimeChartResponse]:
    """Get web monitoring response time chart

     Get response time chart points for a web monitoring service

    Args:
        web_monitoring_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | WebMonitoringResponseTimeChartResponse]
    """

    kwargs = _get_kwargs(
        web_monitoring_id=web_monitoring_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    web_monitoring_id: int,
    *,
    client: AuthenticatedClient,
) -> ApiError | WebMonitoringResponseTimeChartResponse | None:
    """Get web monitoring response time chart

     Get response time chart points for a web monitoring service

    Args:
        web_monitoring_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | WebMonitoringResponseTimeChartResponse
    """

    return (
        await asyncio_detailed(
            web_monitoring_id=web_monitoring_id,
            client=client,
        )
    ).parsed
