from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SslCertificateOwnerRequest")


@_attrs_define
class SslCertificateOwnerRequest:
    admin_title: str | Unset = UNSET
    """ Title of the administrative contact, one of the values of the order: `Mrs`, `Mr`, `Miss`, `Ms`, `Dr` or
    `Rev` """
    admin_role: str | Unset = UNSET
    """ Role of the administrative contact, one of the values of the order: `Business Owner`, `Website Owner`,
    `President` or `Company Director` """
    admin_first_name: str | Unset = UNSET
    """ First name of the administrative contact """
    admin_last_name: str | Unset = UNSET
    """ Last name of the administrative contact """
    admin_email: str | Unset = UNSET
    """ Email of the administrative contact """
    admin_organization: str | Unset = UNSET
    """ Organization of the administrative contact """
    admin_phone_cc: str | Unset = UNSET
    """ International dialling code of the phone of the administrative contact, without `+` (for example `39`) """
    admin_phone_number: str | Unset = UNSET
    """ Phone number of the administrative contact, without the dialling code """
    admin_address: str | Unset = UNSET
    """ Address of the administrative contact """
    admin_city: str | Unset = UNSET
    """ City of the administrative contact """
    admin_state: str | Unset = UNSET
    """ State or province of the administrative contact """
    admin_postal_code: str | Unset = UNSET
    """ Postal code of the administrative contact """
    admin_country: str | Unset = UNSET
    """ Country of the administrative contact, as ISO 3166-1 alpha-2 code (for example `IT`) """

    def to_dict(self) -> dict[str, Any]:
        admin_title = self.admin_title

        admin_role = self.admin_role

        admin_first_name = self.admin_first_name

        admin_last_name = self.admin_last_name

        admin_email = self.admin_email

        admin_organization = self.admin_organization

        admin_phone_cc = self.admin_phone_cc

        admin_phone_number = self.admin_phone_number

        admin_address = self.admin_address

        admin_city = self.admin_city

        admin_state = self.admin_state

        admin_postal_code = self.admin_postal_code

        admin_country = self.admin_country

        field_dict: dict[str, Any] = {}

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
        admin_title = d.pop("admin_title", UNSET)

        admin_role = d.pop("admin_role", UNSET)

        admin_first_name = d.pop("admin_first_name", UNSET)

        admin_last_name = d.pop("admin_last_name", UNSET)

        admin_email = d.pop("admin_email", UNSET)

        admin_organization = d.pop("admin_organization", UNSET)

        admin_phone_cc = d.pop("admin_phone_cc", UNSET)

        admin_phone_number = d.pop("admin_phone_number", UNSET)

        admin_address = d.pop("admin_address", UNSET)

        admin_city = d.pop("admin_city", UNSET)

        admin_state = d.pop("admin_state", UNSET)

        admin_postal_code = d.pop("admin_postal_code", UNSET)

        admin_country = d.pop("admin_country", UNSET)

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

        return ssl_certificate_owner_request
