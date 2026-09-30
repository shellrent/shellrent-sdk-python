from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="HostingEmailAlias")


@_attrs_define
class HostingEmailAlias:
    alias_id: str
    address: str
    address_idna: str
    goto: None | str
    goto_idna: None | str
    domain: str
    domain_idna: str
    is_active: bool
    does_exist: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alias_id = self.alias_id

        address = self.address

        address_idna = self.address_idna

        goto: None | str
        goto = self.goto

        goto_idna: None | str
        goto_idna = self.goto_idna

        domain = self.domain

        domain_idna = self.domain_idna

        is_active = self.is_active

        does_exist = self.does_exist

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "alias_id": alias_id,
                "address": address,
                "address_idna": address_idna,
                "goto": goto,
                "goto_idna": goto_idna,
                "domain": domain,
                "domain_idna": domain_idna,
                "is_active": is_active,
                "does_exist": does_exist,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        alias_id = d.pop("alias_id")

        address = d.pop("address")

        address_idna = d.pop("address_idna")

        def _parse_goto(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        goto = _parse_goto(d.pop("goto"))

        def _parse_goto_idna(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        goto_idna = _parse_goto_idna(d.pop("goto_idna"))

        domain = d.pop("domain")

        domain_idna = d.pop("domain_idna")

        is_active = d.pop("is_active")

        does_exist = d.pop("does_exist")

        hosting_email_alias = cls(
            alias_id=alias_id,
            address=address,
            address_idna=address_idna,
            goto=goto,
            goto_idna=goto_idna,
            domain=domain,
            domain_idna=domain_idna,
            is_active=is_active,
            does_exist=does_exist,
        )

        hosting_email_alias.additional_properties = d
        return hosting_email_alias

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
