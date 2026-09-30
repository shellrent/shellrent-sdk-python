from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DnssecDsData")


@_attrs_define
class DnssecDsData:
    zone_ttl: int
    key_tag: int
    key_algorithm: int
    digest_type: int
    digest_value: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        zone_ttl = self.zone_ttl

        key_tag = self.key_tag

        key_algorithm = self.key_algorithm

        digest_type = self.digest_type

        digest_value = self.digest_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "zone_ttl": zone_ttl,
                "key_tag": key_tag,
                "key_algorithm": key_algorithm,
                "digest_type": digest_type,
                "digest_value": digest_value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        zone_ttl = d.pop("zone_ttl")

        key_tag = d.pop("key_tag")

        key_algorithm = d.pop("key_algorithm")

        digest_type = d.pop("digest_type")

        digest_value = d.pop("digest_value")

        dnssec_ds_data = cls(
            zone_ttl=zone_ttl,
            key_tag=key_tag,
            key_algorithm=key_algorithm,
            digest_type=digest_type,
            digest_value=digest_value,
        )

        dnssec_ds_data.additional_properties = d
        return dnssec_ds_data

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
