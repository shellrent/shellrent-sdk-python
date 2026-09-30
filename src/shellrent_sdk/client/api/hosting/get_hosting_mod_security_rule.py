from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.hosting_mod_security_rule_response import HostingModSecurityRuleResponse
from ...types import Response


def _get_kwargs(
    hosting_id: int,
    rule_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v3/hostings/{hosting_id}/modsecurity/rules/{rule_id}".format(
            hosting_id=quote(str(hosting_id), safe=""),
            rule_id=quote(str(rule_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | HostingModSecurityRuleResponse | None:
    if response.status_code == 200:
        response_200 = HostingModSecurityRuleResponse.from_dict(response.json())

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
) -> Response[ApiError | HostingModSecurityRuleResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    hosting_id: int,
    rule_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[ApiError | HostingModSecurityRuleResponse]:
    """Get ModSecurity rule

     Get a ModSecurity rule details

    Args:
        hosting_id (int):
        rule_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | HostingModSecurityRuleResponse]
    """

    kwargs = _get_kwargs(
        hosting_id=hosting_id,
        rule_id=rule_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    hosting_id: int,
    rule_id: int,
    *,
    client: AuthenticatedClient,
) -> ApiError | HostingModSecurityRuleResponse | None:
    """Get ModSecurity rule

     Get a ModSecurity rule details

    Args:
        hosting_id (int):
        rule_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | HostingModSecurityRuleResponse
    """

    return sync_detailed(
        hosting_id=hosting_id,
        rule_id=rule_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    hosting_id: int,
    rule_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[ApiError | HostingModSecurityRuleResponse]:
    """Get ModSecurity rule

     Get a ModSecurity rule details

    Args:
        hosting_id (int):
        rule_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | HostingModSecurityRuleResponse]
    """

    kwargs = _get_kwargs(
        hosting_id=hosting_id,
        rule_id=rule_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    hosting_id: int,
    rule_id: int,
    *,
    client: AuthenticatedClient,
) -> ApiError | HostingModSecurityRuleResponse | None:
    """Get ModSecurity rule

     Get a ModSecurity rule details

    Args:
        hosting_id (int):
        rule_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | HostingModSecurityRuleResponse
    """

    return (
        await asyncio_detailed(
            hosting_id=hosting_id,
            rule_id=rule_id,
            client=client,
        )
    ).parsed
