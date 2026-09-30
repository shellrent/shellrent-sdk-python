from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DnssecKeyData")


@_attrs_define
class DnssecKeyData:
    zone_ttl: int
    flags: int
    key_protocol: int
    key_algorithm: int
    public_key: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        zone_ttl = self.zone_ttl

        flags = self.flags

        key_protocol = self.key_protocol

        key_algorithm = self.key_algorithm

        public_key = self.public_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "zone_ttl": zone_ttl,
                "flags": flags,
                "key_protocol": key_protocol,
                "key_algorithm": key_algorithm,
                "public_key": public_key,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        zone_ttl = d.pop("zone_ttl")

        flags = d.pop("flags")

        key_protocol = d.pop("key_protocol")

        key_algorithm = d.pop("key_algorithm")

        public_key = d.pop("public_key")

        dnssec_key_data = cls(
            zone_ttl=zone_ttl,
            flags=flags,
            key_protocol=key_protocol,
            key_algorithm=key_algorithm,
            public_key=public_key,
        )

        dnssec_key_data.additional_properties = d
        return dnssec_key_data

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
