from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.country import Country


T = TypeVar("T", bound="Account")


@_attrs_define
class Account:
    """User account, with the data of its administrative contact: without one, these data are null and the country is Italy"""

    account_id: int
    username: None | str
    """ Username assigned to the account when it is created, used to log in """
    username_alias: None | str
    """ Alternative username chosen for the account, also valid to log in; null when not set """
    account_name: None | str
    """ Display name of the account: first name and surname of the administrative contact, or its organization, or
    the username; empty when the account has no administrative contact """
    name: None | str
    """ First name of the administrative contact """
    surname: None | str
    """ Surname of the administrative contact """
    email: None | str
    phone: None | str
    """ Phone of the administrative contact, usually in the form `0039.0123456789`: `00` and the international
    prefix, a dot, the number """
    address: None | str
    city: None | str
    state: None | str
    """ Province of the administrative contact: the acronym of the Italian province, for example `VI`, or `EE`
    outside Italy """
    postal_code: None | str
    country: Country
    date_created: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        username: None | str
        username = self.username

        username_alias: None | str
        username_alias = self.username_alias

        account_name: None | str
        account_name = self.account_name

        name: None | str
        name = self.name

        surname: None | str
        surname = self.surname

        email: None | str
        email = self.email

        phone: None | str
        phone = self.phone

        address: None | str
        address = self.address

        city: None | str
        city = self.city

        state: None | str
        state = self.state

        postal_code: None | str
        postal_code = self.postal_code

        country = self.country.to_dict()

        date_created = self.date_created.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "account_id": account_id,
                "username": username,
                "username_alias": username_alias,
                "account_name": account_name,
                "name": name,
                "surname": surname,
                "email": email,
                "phone": phone,
                "address": address,
                "city": city,
                "state": state,
                "postal_code": postal_code,
                "country": country,
                "date_created": date_created,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.country import Country

        d = dict(src_dict)
        account_id = d.pop("account_id")

        def _parse_username(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        username = _parse_username(d.pop("username"))

        def _parse_username_alias(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        username_alias = _parse_username_alias(d.pop("username_alias"))

        def _parse_account_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        account_name = _parse_account_name(d.pop("account_name"))

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

        def _parse_email(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        email = _parse_email(d.pop("email"))

        def _parse_phone(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        phone = _parse_phone(d.pop("phone"))

        def _parse_address(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        address = _parse_address(d.pop("address"))

        def _parse_city(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        city = _parse_city(d.pop("city"))

        def _parse_state(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        state = _parse_state(d.pop("state"))

        def _parse_postal_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        postal_code = _parse_postal_code(d.pop("postal_code"))

        country = Country.from_dict(d.pop("country"))

        date_created = datetime.datetime.fromisoformat(d.pop("date_created"))

        account = cls(
            account_id=account_id,
            username=username,
            username_alias=username_alias,
            account_name=account_name,
            name=name,
            surname=surname,
            email=email,
            phone=phone,
            address=address,
            city=city,
            state=state,
            postal_code=postal_code,
            country=country,
            date_created=date_created,
        )

        account.additional_properties = d
        return account

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
