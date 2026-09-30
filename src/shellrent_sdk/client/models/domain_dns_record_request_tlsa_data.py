from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DomainDnsRecordRequestTlsaData")


@_attrs_define
class DomainDnsRecordRequestTlsaData:
    """Use this for TLSA type record only"""

    usage: str
    selector: str
    matching_type: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        usage = self.usage

        selector = self.selector

        matching_type = self.matching_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "usage": usage,
                "selector": selector,
                "matching_type": matching_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        usage = d.pop("usage")

        selector = d.pop("selector")

        matching_type = d.pop("matching_type")

        domain_dns_record_request_tlsa_data = cls(
            usage=usage,
            selector=selector,
            matching_type=matching_type,
        )

        domain_dns_record_request_tlsa_data.additional_properties = d
        return domain_dns_record_request_tlsa_data

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
