from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="HostingModSecurity")


@_attrs_define
class HostingModSecurity:
    hosting_id: int
    is_available: bool
    is_active: bool
    firewall_compatible: bool
    full_strict: bool | None
    custom_rules: list[str] | None
    custom_set: list[str] | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hosting_id = self.hosting_id

        is_available = self.is_available

        is_active = self.is_active

        firewall_compatible = self.firewall_compatible

        full_strict: bool | None
        full_strict = self.full_strict

        custom_rules: list[str] | None
        if isinstance(self.custom_rules, list):
            custom_rules = self.custom_rules

        else:
            custom_rules = self.custom_rules

        custom_set: list[str] | None
        if isinstance(self.custom_set, list):
            custom_set = self.custom_set

        else:
            custom_set = self.custom_set

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hosting_id": hosting_id,
                "is_available": is_available,
                "is_active": is_active,
                "firewall_compatible": firewall_compatible,
                "full_strict": full_strict,
                "custom_rules": custom_rules,
                "custom_set": custom_set,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        hosting_id = d.pop("hosting_id")

        is_available = d.pop("is_available")

        is_active = d.pop("is_active")

        firewall_compatible = d.pop("firewall_compatible")

        def _parse_full_strict(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        full_strict = _parse_full_strict(d.pop("full_strict"))

        def _parse_custom_rules(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                custom_rules_type_0 = cast(list[str], data)

                return custom_rules_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        custom_rules = _parse_custom_rules(d.pop("custom_rules"))

        def _parse_custom_set(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                custom_set_type_0 = cast(list[str], data)

                return custom_set_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        custom_set = _parse_custom_set(d.pop("custom_set"))

        hosting_mod_security = cls(
            hosting_id=hosting_id,
            is_available=is_available,
            is_active=is_active,
            firewall_compatible=firewall_compatible,
            full_strict=full_strict,
            custom_rules=custom_rules,
            custom_set=custom_set,
        )

        hosting_mod_security.additional_properties = d
        return hosting_mod_security

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
