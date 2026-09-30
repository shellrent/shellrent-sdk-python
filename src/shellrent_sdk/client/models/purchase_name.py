from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PurchaseName")


@_attrs_define
class PurchaseName:
    name: str
    """ Service name """
    full_name: str
    """ Complete name (Service and object name) """
    object_name: str
    """ Name of the purchase object (ie. domain name, server hostname, etc.) """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        full_name = self.full_name

        object_name = self.object_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "full_name": full_name,
                "object_name": object_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name")

        full_name = d.pop("full_name")

        object_name = d.pop("object_name")

        purchase_name = cls(
            name=name,
            full_name=full_name,
            object_name=object_name,
        )

        purchase_name.additional_properties = d
        return purchase_name

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
