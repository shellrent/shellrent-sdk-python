from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.sms_phonebook_add_contacts_request_phone_numbers_item import (
        SmsPhonebookAddContactsRequestPhoneNumbersItem,
    )


T = TypeVar("T", bound="SmsPhonebookAddContactsRequest")


@_attrs_define
class SmsPhonebookAddContactsRequest:
    phone_numbers: list[SmsPhonebookAddContactsRequestPhoneNumbersItem]
    """ Collection of one or more phone numbers to create contacts in the Phonebook """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        phone_numbers = []
        for phone_numbers_item_data in self.phone_numbers:
            phone_numbers_item = phone_numbers_item_data.to_dict()
            phone_numbers.append(phone_numbers_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
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

        sms_phonebook_add_contacts_request.additional_properties = d
        return sms_phonebook_add_contacts_request

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
