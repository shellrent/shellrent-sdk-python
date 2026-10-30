from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..models.hosting_ssl_certificate_install_request_cn_type import (
    HostingSslCertificateInstallRequestCnType,
)
from ..models.hosting_ssl_certificate_install_request_destination_type import (
    HostingSslCertificateInstallRequestDestinationType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="HostingSslCertificateInstallRequest")


@_attrs_define
class HostingSslCertificateInstallRequest:
    """SSL certificate to install on the hosting; with no body, a wildcard Let's Encrypt certificate for the website and
    the mail of a main hosting, or for the website of a subdomain

    """

    ssl_certificate_id: int | None | Unset = UNSET
    """ Id of a purchased SSL certificate to install (`GET /api/v3/ssl-certificates/{ssl_certificate_id}`): an
    active certificate of the owner of the hosting, a wildcard one or one with SAN to install it also on the mail
    servers. Omit it, or send null, to install a Let's Encrypt certificate, issued if the hosting has none: when the
    DNS of the domain are not on our nameservers, the issue requires the CNAME record that delegates the DNS
    validation (`GET /api/v3/hostings/{hosting_id}/ssl-certificates/can-install`) """
    destination_type: HostingSslCertificateInstallRequestDestinationType | Unset = UNSET
    """ Where to install the certificate: `web` for the website, `mail` for the mail servers, `all` for both. When
    omitted, `all` on a main hosting and `web` on a subdomain, where only `web` is allowed. `mail` and `all` require
    a Let's Encrypt `cn_type` `WILDCARD` """
    cn_type: HostingSslCertificateInstallRequestCnType | Unset = (
        HostingSslCertificateInstallRequestCnType.WILDCARD
    )
    """ Type of the certificate: `NORMAL`, or `WILDCARD` for a wildcard certificate. Without `ssl_certificate_id` it
    chooses the Let's Encrypt certificate to install. Omit this field if you're sending `ssl_certificate_id`. """

    def to_dict(self) -> dict[str, Any]:
        ssl_certificate_id: int | None | Unset
        if isinstance(self.ssl_certificate_id, Unset):
            ssl_certificate_id = UNSET
        else:
            ssl_certificate_id = self.ssl_certificate_id

        destination_type: str | Unset = UNSET
        if not isinstance(self.destination_type, Unset):
            destination_type = self.destination_type.value

        cn_type: str | Unset = UNSET
        if not isinstance(self.cn_type, Unset):
            cn_type = self.cn_type.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if ssl_certificate_id is not UNSET:
            field_dict["ssl_certificate_id"] = ssl_certificate_id
        if destination_type is not UNSET:
            field_dict["destination_type"] = destination_type
        if cn_type is not UNSET:
            field_dict["cn_type"] = cn_type

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_ssl_certificate_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        ssl_certificate_id = _parse_ssl_certificate_id(d.pop("ssl_certificate_id", UNSET))

        _destination_type = d.pop("destination_type", UNSET)
        destination_type: HostingSslCertificateInstallRequestDestinationType | Unset
        if isinstance(_destination_type, Unset):
            destination_type = UNSET
        else:
            destination_type = HostingSslCertificateInstallRequestDestinationType(_destination_type)

        _cn_type = d.pop("cn_type", UNSET)
        cn_type: HostingSslCertificateInstallRequestCnType | Unset
        if isinstance(_cn_type, Unset):
            cn_type = UNSET
        else:
            cn_type = HostingSslCertificateInstallRequestCnType(_cn_type)

        hosting_ssl_certificate_install_request = cls(
            ssl_certificate_id=ssl_certificate_id,
            destination_type=destination_type,
            cn_type=cn_type,
        )

        return hosting_ssl_certificate_install_request
