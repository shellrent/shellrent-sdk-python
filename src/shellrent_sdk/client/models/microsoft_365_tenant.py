from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Microsoft365Tenant")


@_attrs_define
class Microsoft365Tenant:
    tenant_id: int
    microsoft_uuid: None | str
    domain_prefix: None | str
    microsoft_domain: None | str
    imported: bool
    first_name: None | str
    last_name: None | str
    country: None | str
    company_name: None | str
    address: None | str
    city: None | str
    state: None | str
    postal_code: None | str
    email_address: None | str
    phone_prefix: None | str
    phone_number: None | str
    locale: None | str
    account_login: None | str
    mca_compliant: bool
    mca_sign_date: datetime.datetime | None
    mca_template_id: None | str
    mca_error: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tenant_id = self.tenant_id

        microsoft_uuid: None | str
        microsoft_uuid = self.microsoft_uuid

        domain_prefix: None | str
        domain_prefix = self.domain_prefix

        microsoft_domain: None | str
        microsoft_domain = self.microsoft_domain

        imported = self.imported

        first_name: None | str
        first_name = self.first_name

        last_name: None | str
        last_name = self.last_name

        country: None | str
        country = self.country

        company_name: None | str
        company_name = self.company_name

        address: None | str
        address = self.address

        city: None | str
        city = self.city

        state: None | str
        state = self.state

        postal_code: None | str
        postal_code = self.postal_code

        email_address: None | str
        email_address = self.email_address

        phone_prefix: None | str
        phone_prefix = self.phone_prefix

        phone_number: None | str
        phone_number = self.phone_number

        locale: None | str
        locale = self.locale

        account_login: None | str
        account_login = self.account_login

        mca_compliant = self.mca_compliant

        mca_sign_date: None | str
        if isinstance(self.mca_sign_date, datetime.datetime):
            mca_sign_date = self.mca_sign_date.isoformat()
        else:
            mca_sign_date = self.mca_sign_date

        mca_template_id: None | str
        mca_template_id = self.mca_template_id

        mca_error: None | str
        mca_error = self.mca_error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tenant_id": tenant_id,
                "microsoft_uuid": microsoft_uuid,
                "domain_prefix": domain_prefix,
                "microsoft_domain": microsoft_domain,
                "imported": imported,
                "first_name": first_name,
                "last_name": last_name,
                "country": country,
                "company_name": company_name,
                "address": address,
                "city": city,
                "state": state,
                "postal_code": postal_code,
                "email_address": email_address,
                "phone_prefix": phone_prefix,
                "phone_number": phone_number,
                "locale": locale,
                "account_login": account_login,
                "mca_compliant": mca_compliant,
                "mca_sign_date": mca_sign_date,
                "mca_template_id": mca_template_id,
                "mca_error": mca_error,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        tenant_id = d.pop("tenant_id")

        def _parse_microsoft_uuid(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        microsoft_uuid = _parse_microsoft_uuid(d.pop("microsoft_uuid"))

        def _parse_domain_prefix(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        domain_prefix = _parse_domain_prefix(d.pop("domain_prefix"))

        def _parse_microsoft_domain(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        microsoft_domain = _parse_microsoft_domain(d.pop("microsoft_domain"))

        imported = d.pop("imported")

        def _parse_first_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        first_name = _parse_first_name(d.pop("first_name"))

        def _parse_last_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        last_name = _parse_last_name(d.pop("last_name"))

        def _parse_country(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        country = _parse_country(d.pop("country"))

        def _parse_company_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        company_name = _parse_company_name(d.pop("company_name"))

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

        def _parse_email_address(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        email_address = _parse_email_address(d.pop("email_address"))

        def _parse_phone_prefix(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        phone_prefix = _parse_phone_prefix(d.pop("phone_prefix"))

        def _parse_phone_number(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        phone_number = _parse_phone_number(d.pop("phone_number"))

        def _parse_locale(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        locale = _parse_locale(d.pop("locale"))

        def _parse_account_login(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        account_login = _parse_account_login(d.pop("account_login"))

        mca_compliant = d.pop("mca_compliant")

        def _parse_mca_sign_date(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                mca_sign_date_type_0 = datetime.datetime.fromisoformat(data)

                return mca_sign_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        mca_sign_date = _parse_mca_sign_date(d.pop("mca_sign_date"))

        def _parse_mca_template_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        mca_template_id = _parse_mca_template_id(d.pop("mca_template_id"))

        def _parse_mca_error(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        mca_error = _parse_mca_error(d.pop("mca_error"))

        microsoft_365_tenant = cls(
            tenant_id=tenant_id,
            microsoft_uuid=microsoft_uuid,
            domain_prefix=domain_prefix,
            microsoft_domain=microsoft_domain,
            imported=imported,
            first_name=first_name,
            last_name=last_name,
            country=country,
            company_name=company_name,
            address=address,
            city=city,
            state=state,
            postal_code=postal_code,
            email_address=email_address,
            phone_prefix=phone_prefix,
            phone_number=phone_number,
            locale=locale,
            account_login=account_login,
            mca_compliant=mca_compliant,
            mca_sign_date=mca_sign_date,
            mca_template_id=mca_template_id,
            mca_error=mca_error,
        )

        microsoft_365_tenant.additional_properties = d
        return microsoft_365_tenant

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
