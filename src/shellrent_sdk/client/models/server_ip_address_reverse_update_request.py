from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServerIpAddressReverseUpdateRequest")


@_attrs_define
class ServerIpAddressReverseUpdateRequest:
    reverse_dns: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reverse_dns: None | str | Unset
        if isinstance(self.reverse_dns, Unset):
            reverse_dns = UNSET
        else:
            reverse_dns = self.reverse_dns

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reverse_dns is not UNSET:
            field_dict["reverse_dns"] = reverse_dns

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_reverse_dns(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reverse_dns = _parse_reverse_dns(d.pop("reverse_dns", UNSET))

        server_ip_address_reverse_update_request = cls(
            reverse_dns=reverse_dns,
        )

        server_ip_address_reverse_update_request.additional_properties = d
        return server_ip_address_reverse_update_request

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
