from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="HostingEmailAliasCreateRequest")


@_attrs_define
class HostingEmailAliasCreateRequest:
    alias_name: str
    """ Alias local-part without domain. """
    goto: list[str]
    """ Destination addresses of the alias, at least one """

    def to_dict(self) -> dict[str, Any]:
        alias_name = self.alias_name

        goto = self.goto

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "alias_name": alias_name,
                "goto": goto,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        alias_name = d.pop("alias_name")

        goto = cast(list[str], d.pop("goto"))

        hosting_email_alias_create_request = cls(
            alias_name=alias_name,
            goto=goto,
        )

        return hosting_email_alias_create_request
