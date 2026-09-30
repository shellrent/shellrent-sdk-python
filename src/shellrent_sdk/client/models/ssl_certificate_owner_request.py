from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SslCertificateOwnerRequest")


@_attrs_define
class SslCertificateOwnerRequest:
    admin_title: None | str | Unset = UNSET
    admin_role: None | str | Unset = UNSET
    admin_first_name: None | str | Unset = UNSET
    admin_last_name: None | str | Unset = UNSET
    admin_email: None | str | Unset = UNSET
    admin_organization: None | str | Unset = UNSET
    admin_phone_cc: None | str | Unset = UNSET
    admin_phone_number: None | str | Unset = UNSET
    admin_address: None | str | Unset = UNSET
    admin_city: None | str | Unset = UNSET
    admin_state: None | str | Unset = UNSET
    admin_postal_code: None | str | Unset = UNSET
    admin_country: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        admin_title: None | str | Unset
        if isinstance(self.admin_title, Unset):
            admin_title = UNSET
        else:
            admin_title = self.admin_title

        admin_role: None | str | Unset
        if isinstance(self.admin_role, Unset):
            admin_role = UNSET
        else:
            admin_role = self.admin_role

        admin_first_name: None | str | Unset
        if isinstance(self.admin_first_name, Unset):
            admin_first_name = UNSET
        else:
            admin_first_name = self.admin_first_name

        admin_last_name: None | str | Unset
        if isinstance(self.admin_last_name, Unset):
            admin_last_name = UNSET
        else:
            admin_last_name = self.admin_last_name

        admin_email: None | str | Unset
        if isinstance(self.admin_email, Unset):
            admin_email = UNSET
        else:
            admin_email = self.admin_email

        admin_organization: None | str | Unset
        if isinstance(self.admin_organization, Unset):
            admin_organization = UNSET
        else:
            admin_organization = self.admin_organization

        admin_phone_cc: None | str | Unset
        if isinstance(self.admin_phone_cc, Unset):
            admin_phone_cc = UNSET
        else:
            admin_phone_cc = self.admin_phone_cc

        admin_phone_number: None | str | Unset
        if isinstance(self.admin_phone_number, Unset):
            admin_phone_number = UNSET
        else:
            admin_phone_number = self.admin_phone_number

        admin_address: None | str | Unset
        if isinstance(self.admin_address, Unset):
            admin_address = UNSET
        else:
            admin_address = self.admin_address

        admin_city: None | str | Unset
        if isinstance(self.admin_city, Unset):
            admin_city = UNSET
        else:
            admin_city = self.admin_city

        admin_state: None | str | Unset
        if isinstance(self.admin_state, Unset):
            admin_state = UNSET
        else:
            admin_state = self.admin_state

        admin_postal_code: None | str | Unset
        if isinstance(self.admin_postal_code, Unset):
            admin_postal_code = UNSET
        else:
            admin_postal_code = self.admin_postal_code

        admin_country: None | str | Unset
        if isinstance(self.admin_country, Unset):
            admin_country = UNSET
        else:
            admin_country = self.admin_country

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if admin_title is not UNSET:
            field_dict["admin_title"] = admin_title
        if admin_role is not UNSET:
            field_dict["admin_role"] = admin_role
        if admin_first_name is not UNSET:
            field_dict["admin_first_name"] = admin_first_name
        if admin_last_name is not UNSET:
            field_dict["admin_last_name"] = admin_last_name
        if admin_email is not UNSET:
            field_dict["admin_email"] = admin_email
        if admin_organization is not UNSET:
            field_dict["admin_organization"] = admin_organization
        if admin_phone_cc is not UNSET:
            field_dict["admin_phone_cc"] = admin_phone_cc
        if admin_phone_number is not UNSET:
            field_dict["admin_phone_number"] = admin_phone_number
        if admin_address is not UNSET:
            field_dict["admin_address"] = admin_address
        if admin_city is not UNSET:
            field_dict["admin_city"] = admin_city
        if admin_state is not UNSET:
            field_dict["admin_state"] = admin_state
        if admin_postal_code is not UNSET:
            field_dict["admin_postal_code"] = admin_postal_code
        if admin_country is not UNSET:
            field_dict["admin_country"] = admin_country

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_admin_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        admin_title = _parse_admin_title(d.pop("admin_title", UNSET))

        def _parse_admin_role(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        admin_role = _parse_admin_role(d.pop("admin_role", UNSET))

        def _parse_admin_first_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        admin_first_name = _parse_admin_first_name(d.pop("admin_first_name", UNSET))

        def _parse_admin_last_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        admin_last_name = _parse_admin_last_name(d.pop("admin_last_name", UNSET))

        def _parse_admin_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        admin_email = _parse_admin_email(d.pop("admin_email", UNSET))

        def _parse_admin_organization(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        admin_organization = _parse_admin_organization(d.pop("admin_organization", UNSET))

        def _parse_admin_phone_cc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        admin_phone_cc = _parse_admin_phone_cc(d.pop("admin_phone_cc", UNSET))

        def _parse_admin_phone_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        admin_phone_number = _parse_admin_phone_number(d.pop("admin_phone_number", UNSET))

        def _parse_admin_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        admin_address = _parse_admin_address(d.pop("admin_address", UNSET))

        def _parse_admin_city(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        admin_city = _parse_admin_city(d.pop("admin_city", UNSET))

        def _parse_admin_state(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        admin_state = _parse_admin_state(d.pop("admin_state", UNSET))

        def _parse_admin_postal_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        admin_postal_code = _parse_admin_postal_code(d.pop("admin_postal_code", UNSET))

        def _parse_admin_country(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        admin_country = _parse_admin_country(d.pop("admin_country", UNSET))

        ssl_certificate_owner_request = cls(
            admin_title=admin_title,
            admin_role=admin_role,
            admin_first_name=admin_first_name,
            admin_last_name=admin_last_name,
            admin_email=admin_email,
            admin_organization=admin_organization,
            admin_phone_cc=admin_phone_cc,
            admin_phone_number=admin_phone_number,
            admin_address=admin_address,
            admin_city=admin_city,
            admin_state=admin_state,
            admin_postal_code=admin_postal_code,
            admin_country=admin_country,
        )

        ssl_certificate_owner_request.additional_properties = d
        return ssl_certificate_owner_request

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
