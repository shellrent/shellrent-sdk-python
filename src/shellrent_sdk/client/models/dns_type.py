from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DnsType")


@_attrs_define
class DnsType:
    """Nameserver type of a domain, which decides where its DNS zone is managed"""

    type_code: str
    """ Code of the nameserver type: `INTERNAL` (our "standard" nameservers), `EXTERNAL` (nameservers of a third
    party) or `CLOUDFLARE` (Cloudflare nameservers, with a Cloudflare account) """
    type_name: str
    """ Name of the nameserver type, in Italian: `Standard`, `Esterna` or `Cloudflare` """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_code = self.type_code

        type_name = self.type_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type_code": type_code,
                "type_name": type_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        type_code = d.pop("type_code")

        type_name = d.pop("type_name")

        dns_type = cls(
            type_code=type_code,
            type_name=type_name,
        )

        dns_type.additional_properties = d
        return dns_type

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
