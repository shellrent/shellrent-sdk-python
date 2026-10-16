from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sms_phonebook_create_request_phone_numbers_item import (
        SmsPhonebookCreateRequestPhoneNumbersItem,
    )


T = TypeVar("T", bound="SmsPhonebookCreateRequest")


@_attrs_define
class SmsPhonebookCreateRequest:
    name: str
    """ Name of the Phonebook. """
    phone_numbers: list[SmsPhonebookCreateRequestPhoneNumbersItem] | Unset = UNSET
    """ Collection of one or more phone numbers to create contacts in the Phonebook """

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        phone_numbers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.phone_numbers, Unset):
            phone_numbers = []
            for phone_numbers_item_data in self.phone_numbers:
                phone_numbers_item = phone_numbers_item_data.to_dict()
                phone_numbers.append(phone_numbers_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
            }
        )
        if phone_numbers is not UNSET:
            field_dict["phone_numbers"] = phone_numbers

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.sms_phonebook_create_request_phone_numbers_item import (
            SmsPhonebookCreateRequestPhoneNumbersItem,
        )

        d = dict(src_dict)
        name = d.pop("name")

        _phone_numbers = d.pop("phone_numbers", UNSET)
        phone_numbers: list[SmsPhonebookCreateRequestPhoneNumbersItem] | Unset = UNSET
        if _phone_numbers is not UNSET:
            phone_numbers = []
            for phone_numbers_item_data in _phone_numbers:
                phone_numbers_item = SmsPhonebookCreateRequestPhoneNumbersItem.from_dict(
                    phone_numbers_item_data
                )

                phone_numbers.append(phone_numbers_item)

        sms_phonebook_create_request = cls(
            name=name,
            phone_numbers=phone_numbers,
        )

        return sms_phonebook_create_request
