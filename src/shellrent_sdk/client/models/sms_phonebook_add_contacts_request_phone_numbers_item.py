from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SmsPhonebookAddContactsRequestPhoneNumbersItem")


@_attrs_define
class SmsPhonebookAddContactsRequestPhoneNumbersItem:
    phone_number: str
    """ Phone number format: international format using the "00" prefix (digits only, no spaces/separators).
    Example: 00393331122444. """
    name: str | Unset = UNSET
    surname: str | Unset = UNSET
    birth_date: datetime.date | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        phone_number = self.phone_number

        name = self.name

        surname = self.surname

        birth_date: str | Unset = UNSET
        if not isinstance(self.birth_date, Unset):
            birth_date = self.birth_date.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "phone_number": phone_number,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if surname is not UNSET:
            field_dict["surname"] = surname
        if birth_date is not UNSET:
            field_dict["birth_date"] = birth_date

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        phone_number = d.pop("phone_number")

        name = d.pop("name", UNSET)

        surname = d.pop("surname", UNSET)

        _birth_date = d.pop("birth_date", UNSET)
        birth_date: datetime.date | Unset
        if isinstance(_birth_date, Unset):
            birth_date = UNSET
        else:
            birth_date = datetime.date.fromisoformat(_birth_date)

        sms_phonebook_add_contacts_request_phone_numbers_item = cls(
            phone_number=phone_number,
            name=name,
            surname=surname,
            birth_date=birth_date,
        )

        sms_phonebook_add_contacts_request_phone_numbers_item.additional_properties = d
        return sms_phonebook_add_contacts_request_phone_numbers_item

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
