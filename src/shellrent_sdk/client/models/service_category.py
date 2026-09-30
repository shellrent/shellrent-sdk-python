from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ServiceCategory")


@_attrs_define
class ServiceCategory:
    category_code: str
    category_name: str
    area_code: str
    area_name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category_code = self.category_code

        category_name = self.category_name

        area_code = self.area_code

        area_name = self.area_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "category_code": category_code,
                "category_name": category_name,
                "area_code": area_code,
                "area_name": area_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        category_code = d.pop("category_code")

        category_name = d.pop("category_name")

        area_code = d.pop("area_code")

        area_name = d.pop("area_name")

        service_category = cls(
            category_code=category_code,
            category_name=category_name,
            area_code=area_code,
            area_name=area_name,
        )

        service_category.additional_properties = d
        return service_category

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
