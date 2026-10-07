from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DnsRecordCaaData")


@_attrs_define
class DnsRecordCaaData:
    """Flags and tag of a CAA record; the value of the tag is in `destination` of the record"""

    flag: int | None
    """ Flags of the CAA record; the API writes only `0` """
    tag_value: None | str
    """ Tag of the CAA record, for example `issue` or `issuewild` """
    can_sign_http_exchanges: bool | None
    """ Whether the value of the tag has the parameter `cansignhttpexchanges=yes`; null when the parameter is
    missing """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        flag: int | None
        flag = self.flag

        tag_value: None | str
        tag_value = self.tag_value

        can_sign_http_exchanges: bool | None
        can_sign_http_exchanges = self.can_sign_http_exchanges

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "flag": flag,
                "tag_value": tag_value,
                "can_sign_http_exchanges": can_sign_http_exchanges,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_flag(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        flag = _parse_flag(d.pop("flag"))

        def _parse_tag_value(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        tag_value = _parse_tag_value(d.pop("tag_value"))

        def _parse_can_sign_http_exchanges(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        can_sign_http_exchanges = _parse_can_sign_http_exchanges(d.pop("can_sign_http_exchanges"))

        dns_record_caa_data = cls(
            flag=flag,
            tag_value=tag_value,
            can_sign_http_exchanges=can_sign_http_exchanges,
        )

        dns_record_caa_data.additional_properties = d
        return dns_record_caa_data

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
