from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="HostingModSecurityRuleCreateRequest")


@_attrs_define
class HostingModSecurityRuleCreateRequest:
    """ModSecurity rule to disable on the hosting"""

    rule_number: int
    """ Number of the ModSecurity rule to disable on the hosting """
    description: str | Unset = UNSET
    """ Description of the rule; used only when the hosting does not have the rule yet """

    def to_dict(self) -> dict[str, Any]:
        rule_number = self.rule_number

        description = self.description

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "rule_number": rule_number,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        rule_number = d.pop("rule_number")

        description = d.pop("description", UNSET)

        hosting_mod_security_rule_create_request = cls(
            rule_number=rule_number,
            description=description,
        )

        return hosting_mod_security_rule_create_request
