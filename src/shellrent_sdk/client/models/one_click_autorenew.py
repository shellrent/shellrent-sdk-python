from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.one_click import OneClick


T = TypeVar("T", bound="OneClickAutorenew")


@_attrs_define
class OneClickAutorenew:
    one_click_preference: list[OneClick]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        one_click_preference = []
        for one_click_preference_item_data in self.one_click_preference:
            one_click_preference_item = one_click_preference_item_data.to_dict()
            one_click_preference.append(one_click_preference_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "one_click_preference": one_click_preference,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.one_click import OneClick

        d = dict(src_dict)
        one_click_preference = []
        _one_click_preference = d.pop("one_click_preference")
        for one_click_preference_item_data in _one_click_preference:
            one_click_preference_item = OneClick.from_dict(one_click_preference_item_data)

            one_click_preference.append(one_click_preference_item)

        one_click_autorenew = cls(
            one_click_preference=one_click_preference,
        )

        one_click_autorenew.additional_properties = d
        return one_click_autorenew

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
