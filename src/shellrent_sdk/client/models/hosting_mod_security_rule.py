from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="HostingModSecurityRule")


@_attrs_define
class HostingModSecurityRule:
    rule_id: int
    hosting_id: int
    rule_number: str
    description: None | str
    included: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rule_id = self.rule_id

        hosting_id = self.hosting_id

        rule_number = self.rule_number

        description: None | str
        description = self.description

        included = self.included

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rule_id": rule_id,
                "hosting_id": hosting_id,
                "rule_number": rule_number,
                "description": description,
                "included": included,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        rule_id = d.pop("rule_id")

        hosting_id = d.pop("hosting_id")

        rule_number = d.pop("rule_number")

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        included = d.pop("included")

        hosting_mod_security_rule = cls(
            rule_id=rule_id,
            hosting_id=hosting_id,
            rule_number=rule_number,
            description=description,
            included=included,
        )

        hosting_mod_security_rule.additional_properties = d
        return hosting_mod_security_rule

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
