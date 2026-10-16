from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DomainNameserver")


@_attrs_define
class DomainNameserver:
    hostname: str
    address_ipv4: None | str
    """ IPv4 address of the nameserver, saved when the nameservers were set; null when not known """
    address_ipv6: None | str
    """ IPv6 address of the nameserver; not filled in for now, always null """
    sort: int
    """ Position of the nameserver, from `1` """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hostname = self.hostname

        address_ipv4: None | str
        address_ipv4 = self.address_ipv4

        address_ipv6: None | str
        address_ipv6 = self.address_ipv6

        sort = self.sort

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hostname": hostname,
                "address_ipv4": address_ipv4,
                "address_ipv6": address_ipv6,
                "sort": sort,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        hostname = d.pop("hostname")

        def _parse_address_ipv4(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        address_ipv4 = _parse_address_ipv4(d.pop("address_ipv4"))

        def _parse_address_ipv6(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        address_ipv6 = _parse_address_ipv6(d.pop("address_ipv6"))

        sort = d.pop("sort")

        domain_nameserver = cls(
            hostname=hostname,
            address_ipv4=address_ipv4,
            address_ipv6=address_ipv6,
            sort=sort,
        )

        domain_nameserver.additional_properties = d
        return domain_nameserver

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
