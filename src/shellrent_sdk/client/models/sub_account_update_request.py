from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SubAccountUpdateRequest")


@_attrs_define
class SubAccountUpdateRequest:
    person_password: str | Unset = UNSET
    username_alias: None | str | Unset = UNSET
    administrative_person_name: str | Unset = UNSET
    administrative_person_surname: str | Unset = UNSET
    administrative_address: str | Unset = UNSET
    administrative_city: str | Unset = UNSET
    administrative_state: str | Unset = UNSET
    """ State or province """
    administrative_country: str | Unset = UNSET
    """ Country ISO code with 2 letters """
    administrative_postal_code: str | Unset = UNSET
    administrative_phone_prefix: str | Unset = UNSET
    administrative_phone: str | Unset = UNSET
    administrative_mobile_prefix: str | Unset = UNSET
    administrative_mobile: str | Unset = UNSET
    administrative_email: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        person_password = self.person_password

        username_alias: None | str | Unset
        if isinstance(self.username_alias, Unset):
            username_alias = UNSET
        else:
            username_alias = self.username_alias

        administrative_person_name = self.administrative_person_name

        administrative_person_surname = self.administrative_person_surname

        administrative_address = self.administrative_address

        administrative_city = self.administrative_city

        administrative_state = self.administrative_state

        administrative_country = self.administrative_country

        administrative_postal_code = self.administrative_postal_code

        administrative_phone_prefix = self.administrative_phone_prefix

        administrative_phone = self.administrative_phone

        administrative_mobile_prefix = self.administrative_mobile_prefix

        administrative_mobile = self.administrative_mobile

        administrative_email = self.administrative_email

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if person_password is not UNSET:
            field_dict["person_password"] = person_password
        if username_alias is not UNSET:
            field_dict["username_alias"] = username_alias
        if administrative_person_name is not UNSET:
            field_dict["administrative_person_name"] = administrative_person_name
        if administrative_person_surname is not UNSET:
            field_dict["administrative_person_surname"] = administrative_person_surname
        if administrative_address is not UNSET:
            field_dict["administrative_address"] = administrative_address
        if administrative_city is not UNSET:
            field_dict["administrative_city"] = administrative_city
        if administrative_state is not UNSET:
            field_dict["administrative_state"] = administrative_state
        if administrative_country is not UNSET:
            field_dict["administrative_country"] = administrative_country
        if administrative_postal_code is not UNSET:
            field_dict["administrative_postal_code"] = administrative_postal_code
        if administrative_phone_prefix is not UNSET:
            field_dict["administrative_phone_prefix"] = administrative_phone_prefix
        if administrative_phone is not UNSET:
            field_dict["administrative_phone"] = administrative_phone
        if administrative_mobile_prefix is not UNSET:
            field_dict["administrative_mobile_prefix"] = administrative_mobile_prefix
        if administrative_mobile is not UNSET:
            field_dict["administrative_mobile"] = administrative_mobile
        if administrative_email is not UNSET:
            field_dict["administrative_email"] = administrative_email

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        person_password = d.pop("person_password", UNSET)

        def _parse_username_alias(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        username_alias = _parse_username_alias(d.pop("username_alias", UNSET))

        administrative_person_name = d.pop("administrative_person_name", UNSET)

        administrative_person_surname = d.pop("administrative_person_surname", UNSET)

        administrative_address = d.pop("administrative_address", UNSET)

        administrative_city = d.pop("administrative_city", UNSET)

        administrative_state = d.pop("administrative_state", UNSET)

        administrative_country = d.pop("administrative_country", UNSET)

        administrative_postal_code = d.pop("administrative_postal_code", UNSET)

        administrative_phone_prefix = d.pop("administrative_phone_prefix", UNSET)

        administrative_phone = d.pop("administrative_phone", UNSET)

        administrative_mobile_prefix = d.pop("administrative_mobile_prefix", UNSET)

        administrative_mobile = d.pop("administrative_mobile", UNSET)

        administrative_email = d.pop("administrative_email", UNSET)

        sub_account_update_request = cls(
            person_password=person_password,
            username_alias=username_alias,
            administrative_person_name=administrative_person_name,
            administrative_person_surname=administrative_person_surname,
            administrative_address=administrative_address,
            administrative_city=administrative_city,
            administrative_state=administrative_state,
            administrative_country=administrative_country,
            administrative_postal_code=administrative_postal_code,
            administrative_phone_prefix=administrative_phone_prefix,
            administrative_phone=administrative_phone,
            administrative_mobile_prefix=administrative_mobile_prefix,
            administrative_mobile=administrative_mobile,
            administrative_email=administrative_email,
        )

        sub_account_update_request.additional_properties = d
        return sub_account_update_request

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
