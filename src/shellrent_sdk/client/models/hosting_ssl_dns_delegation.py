from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="HostingSslDnsDelegation")


@_attrs_define
class HostingSslDnsDelegation:
    """CNAME record that delegates the DNS validation of the Let's Encrypt certificate"""

    managed_dns: bool
    """ Whether the DNS zone of the domain is on our nameservers: the installation creates the CNAME record by
    itself. When false the record must be created on the nameservers of the domain before the installation """
    host: str
    """ Name of the CNAME record, in punycode """
    target: None | str
    """ Target of the CNAME record; null when no delegation is required """
    present: bool | None
    """ Whether the public DNS resolvers return the CNAME record with `target`; null when the DNS zone is on our
    nameservers, where it is not checked, or when no delegation is required """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        managed_dns = self.managed_dns

        host = self.host

        target: None | str
        target = self.target

        present: bool | None
        present = self.present

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "managed_dns": managed_dns,
                "host": host,
                "target": target,
                "present": present,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        managed_dns = d.pop("managed_dns")

        host = d.pop("host")

        def _parse_target(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        target = _parse_target(d.pop("target"))

        def _parse_present(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        present = _parse_present(d.pop("present"))

        hosting_ssl_dns_delegation = cls(
            managed_dns=managed_dns,
            host=host,
            target=target,
            present=present,
        )

        hosting_ssl_dns_delegation.additional_properties = d
        return hosting_ssl_dns_delegation

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
