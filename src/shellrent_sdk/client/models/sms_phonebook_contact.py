from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.country import Country


T = TypeVar("T", bound="SmsPhonebookContact")


@_attrs_define
class SmsPhonebookContact:
    id: int
    phonebooks: list[int]
    country: Country
    phone_number: str
    name: None | str
    surname: None | str
    birth_date: datetime.date | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        phonebooks = self.phonebooks

        country = self.country.to_dict()

        phone_number = self.phone_number

        name: None | str
        name = self.name

        surname: None | str
        surname = self.surname

        birth_date: None | str
        if isinstance(self.birth_date, datetime.date):
            birth_date = self.birth_date.isoformat()
        else:
            birth_date = self.birth_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "phonebooks": phonebooks,
                "country": country,
                "phone_number": phone_number,
                "name": name,
                "surname": surname,
                "birth_date": birth_date,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.country import Country

        d = dict(src_dict)
        id = d.pop("id")

        phonebooks = cast(list[int], d.pop("phonebooks"))

        country = Country.from_dict(d.pop("country"))

        phone_number = d.pop("phone_number")

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        def _parse_surname(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        surname = _parse_surname(d.pop("surname"))

        def _parse_birth_date(data: object) -> datetime.date | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                birth_date_type_0 = datetime.date.fromisoformat(data)

                return birth_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None, data)

        birth_date = _parse_birth_date(d.pop("birth_date"))

        sms_phonebook_contact = cls(
            id=id,
            phonebooks=phonebooks,
            country=country,
            phone_number=phone_number,
            name=name,
            surname=surname,
            birth_date=birth_date,
        )

        sms_phonebook_contact.additional_properties = d
        return sms_phonebook_contact

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
