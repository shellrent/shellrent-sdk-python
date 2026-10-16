from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="HostingModSecurityRuleBulkRequest")


@_attrs_define
class HostingModSecurityRuleBulkRequest:
    """Rules of the hosting to disable"""

    rule_ids: list[int]
    """ Ids of the rules (`rule_id`) to add to the disabled rules of the hosting """

    def to_dict(self) -> dict[str, Any]:
        rule_ids = self.rule_ids

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "rule_ids": rule_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        rule_ids = cast(list[int], d.pop("rule_ids"))

        hosting_mod_security_rule_bulk_request = cls(
            rule_ids=rule_ids,
        )

        return hosting_mod_security_rule_bulk_request
