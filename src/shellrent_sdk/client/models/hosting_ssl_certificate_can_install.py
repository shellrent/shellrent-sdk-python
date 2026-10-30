from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.hosting_ssl_certificate_can_install_reason import (
    HostingSslCertificateCanInstallReason,
)

if TYPE_CHECKING:
    from ..models.hosting_ssl_dns_delegation import HostingSslDnsDelegation


T = TypeVar("T", bound="HostingSslCertificateCanInstall")


@_attrs_define
class HostingSslCertificateCanInstall:
    """Whether an SSL certificate can be installed on the hosting now, and why not"""

    hosting_id: int
    """ Id of the hosting (`GET /api/v3/hostings/{hosting_id}`) """
    can_install: bool
    """ Whether the installation can start now with `POST /api/v3/hostings/{hosting_id}/ssl-certificates` and the
    same fields """
    reason: HostingSslCertificateCanInstallReason | None
    """ Why the installation cannot start now; null when it can. `ALREADY_INSTALLED`: a certificate is already
    installed on the destination, remove it first. `CNAME_MISSING`: the DNS of the domain are not on our nameservers
    and the CNAME record in `dns_delegation` is missing. `LIMIT_REACHED`: too many Let's Encrypt installations on
    the hosting in the last days. `MAIL_NOT_SUPPORTED`: the mail server of the hosting does not accept certificates.
    `OPERATION_RUNNING`: another installation or operation is running on the hosting """
    message: None | str
    """ Description of `reason`; null when the installation can start """
    dns_delegation: HostingSslDnsDelegation | None
    """ CNAME record that delegates the validation of the Let's Encrypt certificate; null when installing a
    purchased certificate (`ssl_certificate_id`) """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.hosting_ssl_dns_delegation import HostingSslDnsDelegation

        hosting_id = self.hosting_id

        can_install = self.can_install

        reason: None | str
        if isinstance(self.reason, HostingSslCertificateCanInstallReason):
            reason = self.reason.value
        else:
            reason = self.reason

        message: None | str
        message = self.message

        dns_delegation: dict[str, Any] | None
        if isinstance(self.dns_delegation, HostingSslDnsDelegation):
            dns_delegation = self.dns_delegation.to_dict()
        else:
            dns_delegation = self.dns_delegation

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hosting_id": hosting_id,
                "can_install": can_install,
                "reason": reason,
                "message": message,
                "dns_delegation": dns_delegation,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.hosting_ssl_dns_delegation import HostingSslDnsDelegation

        d = dict(src_dict)
        hosting_id = d.pop("hosting_id")

        can_install = d.pop("can_install")

        def _parse_reason(data: object) -> HostingSslCertificateCanInstallReason | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                reason_type_0 = HostingSslCertificateCanInstallReason(data)

                return reason_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(HostingSslCertificateCanInstallReason | None, data)

        reason = _parse_reason(d.pop("reason"))

        def _parse_message(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        message = _parse_message(d.pop("message"))

        def _parse_dns_delegation(data: object) -> HostingSslDnsDelegation | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                dns_delegation_type_0 = HostingSslDnsDelegation.from_dict(data)

                return dns_delegation_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(HostingSslDnsDelegation | None, data)

        dns_delegation = _parse_dns_delegation(d.pop("dns_delegation"))

        hosting_ssl_certificate_can_install = cls(
            hosting_id=hosting_id,
            can_install=can_install,
            reason=reason,
            message=message,
            dns_delegation=dns_delegation,
        )

        hosting_ssl_certificate_can_install.additional_properties = d
        return hosting_ssl_certificate_can_install

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
