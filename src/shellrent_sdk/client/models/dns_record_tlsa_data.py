from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DnsRecordTlsaData")


@_attrs_define
class DnsRecordTlsaData:
    usage: None | str
    selector: None | str
    matching_type: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        usage: None | str
        usage = self.usage

        selector: None | str
        selector = self.selector

        matching_type: None | str
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

        def _parse_usage(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        usage = _parse_usage(d.pop("usage"))

        def _parse_selector(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        selector = _parse_selector(d.pop("selector"))

        def _parse_matching_type(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        matching_type = _parse_matching_type(d.pop("matching_type"))

        dns_record_tlsa_data = cls(
            usage=usage,
            selector=selector,
            matching_type=matching_type,
        )

        dns_record_tlsa_data.additional_properties = d
        return dns_record_tlsa_data

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
