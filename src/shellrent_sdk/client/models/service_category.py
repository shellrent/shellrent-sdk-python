from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ServiceCategory")


@_attrs_define
class ServiceCategory:
    category_code: str
    """ Code of the category, for example `PEC` or `CLOUD_STORAGE` """
    category_name: str
    """ Name of the category, in Italian """
    area_code: None | str
    """ Code of the area that groups the category, for example `HOSTING`, `DOMAIN` or `LICENSE` """
    area_name: str
    """ Name of the area, in Italian """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category_code = self.category_code

        category_name = self.category_name

        area_code: None | str
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

        def _parse_area_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        area_code = _parse_area_code(d.pop("area_code"))

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
