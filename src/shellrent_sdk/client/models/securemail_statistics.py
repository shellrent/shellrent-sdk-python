from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SecuremailStatistics")


@_attrs_define
class SecuremailStatistics:
    quantity: int
    protected_mailboxes: int
    not_protected_mailboxes: int
    weekly_elaborated_messages: int
    weekly_spam_messages: int
    weekly_blocked_spam_percentage: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        quantity = self.quantity

        protected_mailboxes = self.protected_mailboxes

        not_protected_mailboxes = self.not_protected_mailboxes

        weekly_elaborated_messages = self.weekly_elaborated_messages

        weekly_spam_messages = self.weekly_spam_messages

        weekly_blocked_spam_percentage = self.weekly_blocked_spam_percentage

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "quantity": quantity,
                "protected_mailboxes": protected_mailboxes,
                "not_protected_mailboxes": not_protected_mailboxes,
                "weekly_elaborated_messages": weekly_elaborated_messages,
                "weekly_spam_messages": weekly_spam_messages,
                "weekly_blocked_spam_percentage": weekly_blocked_spam_percentage,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        quantity = d.pop("quantity")

        protected_mailboxes = d.pop("protected_mailboxes")

        not_protected_mailboxes = d.pop("not_protected_mailboxes")

        weekly_elaborated_messages = d.pop("weekly_elaborated_messages")

        weekly_spam_messages = d.pop("weekly_spam_messages")

        weekly_blocked_spam_percentage = d.pop("weekly_blocked_spam_percentage")

        securemail_statistics = cls(
            quantity=quantity,
            protected_mailboxes=protected_mailboxes,
            not_protected_mailboxes=not_protected_mailboxes,
            weekly_elaborated_messages=weekly_elaborated_messages,
            weekly_spam_messages=weekly_spam_messages,
            weekly_blocked_spam_percentage=weekly_blocked_spam_percentage,
        )

        securemail_statistics.additional_properties = d
        return securemail_statistics

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
