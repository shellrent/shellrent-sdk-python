from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SecuremailMailbox")


@_attrs_define
class SecuremailMailbox:
    mailbox_id: int
    email_address: None | str
    status: None | str
    is_primary: bool
    valid_recipient_id: int | None
    aliases_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mailbox_id = self.mailbox_id

        email_address: None | str
        email_address = self.email_address

        status: None | str
        status = self.status

        is_primary = self.is_primary

        valid_recipient_id: int | None
        valid_recipient_id = self.valid_recipient_id

        aliases_count = self.aliases_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mailbox_id": mailbox_id,
                "email_address": email_address,
                "status": status,
                "is_primary": is_primary,
                "valid_recipient_id": valid_recipient_id,
                "aliases_count": aliases_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        mailbox_id = d.pop("mailbox_id")

        def _parse_email_address(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        email_address = _parse_email_address(d.pop("email_address"))

        def _parse_status(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        status = _parse_status(d.pop("status"))

        is_primary = d.pop("is_primary")

        def _parse_valid_recipient_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        valid_recipient_id = _parse_valid_recipient_id(d.pop("valid_recipient_id"))

        aliases_count = d.pop("aliases_count")

        securemail_mailbox = cls(
            mailbox_id=mailbox_id,
            email_address=email_address,
            status=status,
            is_primary=is_primary,
            valid_recipient_id=valid_recipient_id,
            aliases_count=aliases_count,
        )

        securemail_mailbox.additional_properties = d
        return securemail_mailbox

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
