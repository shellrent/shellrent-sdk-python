from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="HostingEmailCatchAll")


@_attrs_define
class HostingEmailCatchAll:
    is_active: bool
    address: str
    address_idna: str
    destinations: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_active = self.is_active

        address = self.address

        address_idna = self.address_idna

        destinations = self.destinations

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "is_active": is_active,
                "address": address,
                "address_idna": address_idna,
                "destinations": destinations,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        is_active = d.pop("is_active")

        address = d.pop("address")

        address_idna = d.pop("address_idna")

        destinations = cast(list[str], d.pop("destinations"))

        hosting_email_catch_all = cls(
            is_active=is_active,
            address=address,
            address_idna=address_idna,
            destinations=destinations,
        )

        hosting_email_catch_all.additional_properties = d
        return hosting_email_catch_all

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
