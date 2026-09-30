from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SubAccountCreateRequest")


@_attrs_define
class SubAccountCreateRequest:
    person_password: str
    administrative_person_name: str
    administrative_person_surname: str
    administrative_address: str
    administrative_city: str
    administrative_state: str
    """ State or province """
    administrative_country: str
    """ Country ISO code with 2 letters, ie. "IT" for Italy, "ES" for Spain, etc. """
    administrative_postal_code: str
    administrative_phone: str
    """ Phone number without international phone code """
    administrative_email: str
    administrative_phone_prefix: str | Unset = UNSET
    """ International phone code (prefix) for "Phone", ie. "39" for Italy, "44" for United Kingdom """
    administrative_mobile_prefix: str | Unset = UNSET
    """ International phone code (prefix) for "Phone", ie. "39" for Italy, "44" for United Kingdom """
    administrative_mobile: str | Unset = UNSET
    """ Mobile phone number without international phone code """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        person_password = self.person_password

        administrative_person_name = self.administrative_person_name

        administrative_person_surname = self.administrative_person_surname

        administrative_address = self.administrative_address

        administrative_city = self.administrative_city

        administrative_state = self.administrative_state

        administrative_country = self.administrative_country

        administrative_postal_code = self.administrative_postal_code

        administrative_phone = self.administrative_phone

        administrative_email = self.administrative_email

        administrative_phone_prefix = self.administrative_phone_prefix

        administrative_mobile_prefix = self.administrative_mobile_prefix

        administrative_mobile = self.administrative_mobile

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "person_password": person_password,
                "administrative_person_name": administrative_person_name,
                "administrative_person_surname": administrative_person_surname,
                "administrative_address": administrative_address,
                "administrative_city": administrative_city,
                "administrative_state": administrative_state,
                "administrative_country": administrative_country,
                "administrative_postal_code": administrative_postal_code,
                "administrative_phone": administrative_phone,
                "administrative_email": administrative_email,
            }
        )
        if administrative_phone_prefix is not UNSET:
            field_dict["administrative_phone_prefix"] = administrative_phone_prefix
        if administrative_mobile_prefix is not UNSET:
            field_dict["administrative_mobile_prefix"] = administrative_mobile_prefix
        if administrative_mobile is not UNSET:
            field_dict["administrative_mobile"] = administrative_mobile

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        person_password = d.pop("person_password")

        administrative_person_name = d.pop("administrative_person_name")

        administrative_person_surname = d.pop("administrative_person_surname")

        administrative_address = d.pop("administrative_address")

        administrative_city = d.pop("administrative_city")

        administrative_state = d.pop("administrative_state")

        administrative_country = d.pop("administrative_country")

        administrative_postal_code = d.pop("administrative_postal_code")

        administrative_phone = d.pop("administrative_phone")

        administrative_email = d.pop("administrative_email")

        administrative_phone_prefix = d.pop("administrative_phone_prefix", UNSET)

        administrative_mobile_prefix = d.pop("administrative_mobile_prefix", UNSET)

        administrative_mobile = d.pop("administrative_mobile", UNSET)

        sub_account_create_request = cls(
            person_password=person_password,
            administrative_person_name=administrative_person_name,
            administrative_person_surname=administrative_person_surname,
            administrative_address=administrative_address,
            administrative_city=administrative_city,
            administrative_state=administrative_state,
            administrative_country=administrative_country,
            administrative_postal_code=administrative_postal_code,
            administrative_phone=administrative_phone,
            administrative_email=administrative_email,
            administrative_phone_prefix=administrative_phone_prefix,
            administrative_mobile_prefix=administrative_mobile_prefix,
            administrative_mobile=administrative_mobile,
        )

        sub_account_create_request.additional_properties = d
        return sub_account_create_request

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
