from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="HostingEmailBlocList")


@_attrs_define
class HostingEmailBlocList:
    block_list_id: int
    hosting_id: int
    sender: str
    domain: None | str
    mailbox: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        block_list_id = self.block_list_id

        hosting_id = self.hosting_id

        sender = self.sender

        domain: None | str
        domain = self.domain

        mailbox: None | str
        mailbox = self.mailbox

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "block_list_id": block_list_id,
                "hosting_id": hosting_id,
                "sender": sender,
                "domain": domain,
                "mailbox": mailbox,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        block_list_id = d.pop("block_list_id")

        hosting_id = d.pop("hosting_id")

        sender = d.pop("sender")

        def _parse_domain(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        domain = _parse_domain(d.pop("domain"))

        def _parse_mailbox(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        mailbox = _parse_mailbox(d.pop("mailbox"))

        hosting_email_bloc_list = cls(
            block_list_id=block_list_id,
            hosting_id=hosting_id,
            sender=sender,
            domain=domain,
            mailbox=mailbox,
        )

        hosting_email_bloc_list.additional_properties = d
        return hosting_email_bloc_list

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
