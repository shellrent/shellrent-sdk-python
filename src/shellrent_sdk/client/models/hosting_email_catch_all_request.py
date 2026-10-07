from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="HostingEmailCatchAllRequest")


@_attrs_define
class HostingEmailCatchAllRequest:
    goto: list[str]
    """ Destination addresses of the catch-all, at least one: they replace the current ones """

    def to_dict(self) -> dict[str, Any]:
        goto = self.goto

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "goto": goto,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        goto = cast(list[str], d.pop("goto"))

        hosting_email_catch_all_request = cls(
            goto=goto,
        )

        return hosting_email_catch_all_request
