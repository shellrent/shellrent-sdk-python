from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HostingEmailAliasCreateRequest")


@_attrs_define
class HostingEmailAliasCreateRequest:
    alias_name: str | Unset = UNSET
    """ Alias local-part without domain. """
    goto: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alias_name = self.alias_name

        goto: list[str] | Unset = UNSET
        if not isinstance(self.goto, Unset):
            goto = self.goto

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if alias_name is not UNSET:
            field_dict["alias_name"] = alias_name
        if goto is not UNSET:
            field_dict["goto"] = goto

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        alias_name = d.pop("alias_name", UNSET)

        goto = cast(list[str], d.pop("goto", UNSET))

        hosting_email_alias_create_request = cls(
            alias_name=alias_name,
            goto=goto,
        )

        hosting_email_alias_create_request.additional_properties = d
        return hosting_email_alias_create_request

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
