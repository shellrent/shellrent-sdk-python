from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SubAccountCreateRequest")


@_attrs_define
class SubAccountCreateRequest:
    person_password: str
    """ Password of the account: at least 13 characters, with at least one uppercase letter, one lowercase letter,
    one number and one symbol """
    administrative_person_name: str
    """ First name of the administrative contact of the account """
    administrative_person_surname: str
    """ Surname of the administrative contact """
    administrative_address: str
    """ Address of the administrative contact """
    administrative_city: str
    """ City of the administrative contact """
    administrative_state: str
    """ Acronym of the Italian province, ie. "VI" for Vicenza, or "EE" for an address outside Italy """
    administrative_country: str
    """ Country ISO code with 2 letters, ie. "IT" for Italy, "ES" for Spain, etc. """
    administrative_postal_code: str
    """ Postal code of the administrative contact """
    administrative_phone: str
    """ Phone number without international phone code """
    administrative_email: str
    """ Email address of the administrative contact """
    administrative_phone_prefix: str | Unset = UNSET
    """ International phone code (prefix) for "Phone", ie. "39" for Italy, "44" for United Kingdom """
    administrative_mobile_prefix: str | Unset = UNSET
    """ International phone code (prefix) for "Mobile", ie. "39" for Italy, "44" for United Kingdom """
    administrative_mobile: str | Unset = UNSET
    """ Mobile phone number without international phone code """

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

        return sub_account_create_request
