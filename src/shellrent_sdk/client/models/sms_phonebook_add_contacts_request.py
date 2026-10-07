from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.sms_phonebook_add_contacts_request_phone_numbers_item import (
        SmsPhonebookAddContactsRequestPhoneNumbersItem,
    )


T = TypeVar("T", bound="SmsPhonebookAddContactsRequest")


@_attrs_define
class SmsPhonebookAddContactsRequest:
    phone_numbers: list[SmsPhonebookAddContactsRequestPhoneNumbersItem]
    """ Collection of one or more phone numbers to create contacts in the Phonebook """

    def to_dict(self) -> dict[str, Any]:
        phone_numbers = []
        for phone_numbers_item_data in self.phone_numbers:
            phone_numbers_item = phone_numbers_item_data.to_dict()
            phone_numbers.append(phone_numbers_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "phone_numbers": phone_numbers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.sms_phonebook_add_contacts_request_phone_numbers_item import (
            SmsPhonebookAddContactsRequestPhoneNumbersItem,
        )

        d = dict(src_dict)
        phone_numbers = []
        _phone_numbers = d.pop("phone_numbers")
        for phone_numbers_item_data in _phone_numbers:
            phone_numbers_item = SmsPhonebookAddContactsRequestPhoneNumbersItem.from_dict(
                phone_numbers_item_data
            )

            phone_numbers.append(phone_numbers_item)

        sms_phonebook_add_contacts_request = cls(
            phone_numbers=phone_numbers,
        )

        return sms_phonebook_add_contacts_request
