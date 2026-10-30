from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.can_install_hosting_ssl_certificate_cn_type import (
    CanInstallHostingSslCertificateCnType,
)
from ...models.can_install_hosting_ssl_certificate_destination_type import (
    CanInstallHostingSslCertificateDestinationType,
)
from ...models.hosting_ssl_certificate_can_install_response import (
    HostingSslCertificateCanInstallResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    hosting_id: int,
    *,
    ssl_certificate_id: int | None | Unset = UNSET,
    destination_type: CanInstallHostingSslCertificateDestinationType | Unset = UNSET,
    cn_type: CanInstallHostingSslCertificateCnType
    | Unset = CanInstallHostingSslCertificateCnType.WILDCARD,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_ssl_certificate_id: int | None | Unset
    if isinstance(ssl_certificate_id, Unset):
        json_ssl_certificate_id = UNSET
    else:
        json_ssl_certificate_id = ssl_certificate_id
    params["ssl_certificate_id"] = json_ssl_certificate_id

    json_destination_type: str | Unset = UNSET
    if not isinstance(destination_type, Unset):
        json_destination_type = destination_type.value

    params["destination_type"] = json_destination_type

    json_cn_type: str | Unset = UNSET
    if not isinstance(cn_type, Unset):
        json_cn_type = cn_type.value

    params["cn_type"] = json_cn_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v3/hostings/{hosting_id}/ssl-certificates/can-install".format(
            hosting_id=quote(str(hosting_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | HostingSslCertificateCanInstallResponse | None:
    if response.status_code == 200:
        response_200 = HostingSslCertificateCanInstallResponse.from_dict(response.json())

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
) -> Response[ApiError | HostingSslCertificateCanInstallResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    hosting_id: int,
    *,
    client: AuthenticatedClient,
    ssl_certificate_id: int | None | Unset = UNSET,
    destination_type: CanInstallHostingSslCertificateDestinationType | Unset = UNSET,
    cn_type: CanInstallHostingSslCertificateCnType
    | Unset = CanInstallHostingSslCertificateCnType.WILDCARD,
) -> Response[ApiError | HostingSslCertificateCanInstallResponse]:
    """Can install SSL certificate on hosting

     Checks, with the rules of the installation (`POST /api/v3/hostings/{hosting_id}/ssl-certificates`)
    and its fields in the query, whether the SSL certificate can be installed on the hosting now, and
    why not: a certificate already installed, the CNAME record that delegates the validation of Let's
    Encrypt missing from DNS that are not on our nameservers (`dns_delegation` has the record to
    create), the limit of Let's Encrypt installations, the hosting not active yet, an operation running.
    With DNS on our nameservers the installation creates the CNAME record by itself. Invalid fields
    respond 400, as in the installation

    Args:
        hosting_id (int):
        ssl_certificate_id (int | None | Unset):
        destination_type (CanInstallHostingSslCertificateDestinationType | Unset):
        cn_type (CanInstallHostingSslCertificateCnType | Unset):  Default:
            CanInstallHostingSslCertificateCnType.WILDCARD.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | HostingSslCertificateCanInstallResponse]
    """

    kwargs = _get_kwargs(
        hosting_id=hosting_id,
        ssl_certificate_id=ssl_certificate_id,
        destination_type=destination_type,
        cn_type=cn_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    hosting_id: int,
    *,
    client: AuthenticatedClient,
    ssl_certificate_id: int | None | Unset = UNSET,
    destination_type: CanInstallHostingSslCertificateDestinationType | Unset = UNSET,
    cn_type: CanInstallHostingSslCertificateCnType
    | Unset = CanInstallHostingSslCertificateCnType.WILDCARD,
) -> ApiError | HostingSslCertificateCanInstallResponse | None:
    """Can install SSL certificate on hosting

     Checks, with the rules of the installation (`POST /api/v3/hostings/{hosting_id}/ssl-certificates`)
    and its fields in the query, whether the SSL certificate can be installed on the hosting now, and
    why not: a certificate already installed, the CNAME record that delegates the validation of Let's
    Encrypt missing from DNS that are not on our nameservers (`dns_delegation` has the record to
    create), the limit of Let's Encrypt installations, the hosting not active yet, an operation running.
    With DNS on our nameservers the installation creates the CNAME record by itself. Invalid fields
    respond 400, as in the installation

    Args:
        hosting_id (int):
        ssl_certificate_id (int | None | Unset):
        destination_type (CanInstallHostingSslCertificateDestinationType | Unset):
        cn_type (CanInstallHostingSslCertificateCnType | Unset):  Default:
            CanInstallHostingSslCertificateCnType.WILDCARD.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | HostingSslCertificateCanInstallResponse
    """

    return sync_detailed(
        hosting_id=hosting_id,
        client=client,
        ssl_certificate_id=ssl_certificate_id,
        destination_type=destination_type,
        cn_type=cn_type,
    ).parsed


async def asyncio_detailed(
    hosting_id: int,
    *,
    client: AuthenticatedClient,
    ssl_certificate_id: int | None | Unset = UNSET,
    destination_type: CanInstallHostingSslCertificateDestinationType | Unset = UNSET,
    cn_type: CanInstallHostingSslCertificateCnType
    | Unset = CanInstallHostingSslCertificateCnType.WILDCARD,
) -> Response[ApiError | HostingSslCertificateCanInstallResponse]:
    """Can install SSL certificate on hosting

     Checks, with the rules of the installation (`POST /api/v3/hostings/{hosting_id}/ssl-certificates`)
    and its fields in the query, whether the SSL certificate can be installed on the hosting now, and
    why not: a certificate already installed, the CNAME record that delegates the validation of Let's
    Encrypt missing from DNS that are not on our nameservers (`dns_delegation` has the record to
    create), the limit of Let's Encrypt installations, the hosting not active yet, an operation running.
    With DNS on our nameservers the installation creates the CNAME record by itself. Invalid fields
    respond 400, as in the installation

    Args:
        hosting_id (int):
        ssl_certificate_id (int | None | Unset):
        destination_type (CanInstallHostingSslCertificateDestinationType | Unset):
        cn_type (CanInstallHostingSslCertificateCnType | Unset):  Default:
            CanInstallHostingSslCertificateCnType.WILDCARD.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | HostingSslCertificateCanInstallResponse]
    """

    kwargs = _get_kwargs(
        hosting_id=hosting_id,
        ssl_certificate_id=ssl_certificate_id,
        destination_type=destination_type,
        cn_type=cn_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    hosting_id: int,
    *,
    client: AuthenticatedClient,
    ssl_certificate_id: int | None | Unset = UNSET,
    destination_type: CanInstallHostingSslCertificateDestinationType | Unset = UNSET,
    cn_type: CanInstallHostingSslCertificateCnType
    | Unset = CanInstallHostingSslCertificateCnType.WILDCARD,
) -> ApiError | HostingSslCertificateCanInstallResponse | None:
    """Can install SSL certificate on hosting

     Checks, with the rules of the installation (`POST /api/v3/hostings/{hosting_id}/ssl-certificates`)
    and its fields in the query, whether the SSL certificate can be installed on the hosting now, and
    why not: a certificate already installed, the CNAME record that delegates the validation of Let's
    Encrypt missing from DNS that are not on our nameservers (`dns_delegation` has the record to
    create), the limit of Let's Encrypt installations, the hosting not active yet, an operation running.
    With DNS on our nameservers the installation creates the CNAME record by itself. Invalid fields
    respond 400, as in the installation

    Args:
        hosting_id (int):
        ssl_certificate_id (int | None | Unset):
        destination_type (CanInstallHostingSslCertificateDestinationType | Unset):
        cn_type (CanInstallHostingSslCertificateCnType | Unset):  Default:
            CanInstallHostingSslCertificateCnType.WILDCARD.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | HostingSslCertificateCanInstallResponse
    """

    return (
        await asyncio_detailed(
            hosting_id=hosting_id,
            client=client,
            ssl_certificate_id=ssl_certificate_id,
            destination_type=destination_type,
            cn_type=cn_type,
        )
    ).parsed
