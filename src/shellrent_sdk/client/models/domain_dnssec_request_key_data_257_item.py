from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domain_dnssec_request_key_data_257_item_algorithm import (
    DomainDnssecRequestKeyData257ItemAlgorithm,
)

T = TypeVar("T", bound="DomainDnssecRequestKeyData257Item")


@_attrs_define
class DomainDnssecRequestKeyData257Item:
    protocol: int
    algorithm: DomainDnssecRequestKeyData257ItemAlgorithm
    public_key: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        protocol = self.protocol

        algorithm = self.algorithm.value

        public_key = self.public_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "protocol": protocol,
                "algorithm": algorithm,
                "public_key": public_key,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        protocol = d.pop("protocol")

        algorithm = DomainDnssecRequestKeyData257ItemAlgorithm(d.pop("algorithm"))

        public_key = d.pop("public_key")

        domain_dnssec_request_key_data_257_item = cls(
            protocol=protocol,
            algorithm=algorithm,
            public_key=public_key,
        )

        domain_dnssec_request_key_data_257_item.additional_properties = d
        return domain_dnssec_request_key_data_257_item

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
