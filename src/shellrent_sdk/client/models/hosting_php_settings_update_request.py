from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HostingPhpSettingsUpdateRequest")


@_attrs_define
class HostingPhpSettingsUpdateRequest:
    setting: str | Unset = UNSET
    """ PHP setting key. """
    value: str | Unset = UNSET
    """ PHP setting value. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        setting = self.setting

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if setting is not UNSET:
            field_dict["setting"] = setting
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        setting = d.pop("setting", UNSET)

        value = d.pop("value", UNSET)

        hosting_php_settings_update_request = cls(
            setting=setting,
            value=value,
        )

        hosting_php_settings_update_request.additional_properties = d
        return hosting_php_settings_update_request

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
