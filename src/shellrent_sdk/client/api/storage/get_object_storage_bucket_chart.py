from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.object_storage_bucket_chart_response import ObjectStorageBucketChartResponse
from ...types import Response


def _get_kwargs(
    object_storage_id: int,
    bucket_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v3/object-storages/{object_storage_id}/buckets/{bucket_id}/chart".format(
            object_storage_id=quote(str(object_storage_id), safe=""),
            bucket_id=quote(str(bucket_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | ObjectStorageBucketChartResponse | None:
    if response.status_code == 200:
        response_200 = ObjectStorageBucketChartResponse.from_dict(response.json())

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
) -> Response[ApiError | ObjectStorageBucketChartResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    object_storage_id: int,
    bucket_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[ApiError | ObjectStorageBucketChartResponse]:
    """Get object storage bucket chart

     Get object storage bucket chart data

    Args:
        object_storage_id (int):
        bucket_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | ObjectStorageBucketChartResponse]
    """

    kwargs = _get_kwargs(
        object_storage_id=object_storage_id,
        bucket_id=bucket_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    object_storage_id: int,
    bucket_id: int,
    *,
    client: AuthenticatedClient,
) -> ApiError | ObjectStorageBucketChartResponse | None:
    """Get object storage bucket chart

     Get object storage bucket chart data

    Args:
        object_storage_id (int):
        bucket_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | ObjectStorageBucketChartResponse
    """

    return sync_detailed(
        object_storage_id=object_storage_id,
        bucket_id=bucket_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    object_storage_id: int,
    bucket_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[ApiError | ObjectStorageBucketChartResponse]:
    """Get object storage bucket chart

     Get object storage bucket chart data

    Args:
        object_storage_id (int):
        bucket_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | ObjectStorageBucketChartResponse]
    """

    kwargs = _get_kwargs(
        object_storage_id=object_storage_id,
        bucket_id=bucket_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    object_storage_id: int,
    bucket_id: int,
    *,
    client: AuthenticatedClient,
) -> ApiError | ObjectStorageBucketChartResponse | None:
    """Get object storage bucket chart

     Get object storage bucket chart data

    Args:
        object_storage_id (int):
        bucket_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | ObjectStorageBucketChartResponse
    """

    return (
        await asyncio_detailed(
            object_storage_id=object_storage_id,
            bucket_id=bucket_id,
            client=client,
        )
    ).parsed
