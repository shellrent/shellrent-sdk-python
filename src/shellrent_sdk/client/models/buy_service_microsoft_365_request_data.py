from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..models.buy_service_microsoft_365_request_data_locale import (
    BuyServiceMicrosoft365RequestDataLocale,
)
from ..models.buy_service_microsoft_365_request_data_tenant_choice import (
    BuyServiceMicrosoft365RequestDataTenantChoice,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="BuyServiceMicrosoft365RequestData")


@_attrs_define
class BuyServiceMicrosoft365RequestData:
    """Information about the Microsoft 365 tenant to associate to the subscription"""

    tenant_choice: BuyServiceMicrosoft365RequestDataTenantChoice
    """ Select whether to choose an existing tenant ("select"), transfer one ("transfer") or create a new tenant
    ("new"). When transferring a tenant, approve the Microsoft Partner Relationship before sending API requests """
    tenant_select: int | None | Unset = UNSET
    """ Tenant ID to which to assign the subscription when selecting an existing tenant """
    domain_prefix: None | str | Unset = UNSET
    """ Prefix of the ".onmicrosoft.com" tenant domain when creating or transferring a tenant """
    first_name: None | str | Unset = UNSET
    """ Contact first name for the tenant when not selecting an existing tenant """
    last_name: None | str | Unset = UNSET
    """ Contact last name for the tenant when not selecting an existing tenant """
    company_name: None | str | Unset = UNSET
    """ Company name for the tenant when not selecting an existing tenant """
    address: None | str | Unset = UNSET
    """ Address for the tenant when not selecting an existing tenant """
    city: None | str | Unset = UNSET
    """ City for the tenant when not selecting an existing tenant """
    state: None | str | Unset = UNSET
    """ State/Province for the tenant address when not selecting an existing tenant """
    postal_code: None | str | Unset = UNSET
    """ Postal code for the tenant address when not selecting an existing tenant """
    country: None | str | Unset = UNSET
    """ ISO country code with 2 letters (e.g. "IT" or "ES") when not selecting an existing tenant """
    email_address: None | str | Unset = UNSET
    """ Administrative email address for the tenant when not selecting an existing tenant """
    phone_prefix: None | str | Unset = UNSET
    """ Country code phone prefix with leading "+" sign when not selecting an existing tenant """
    phone_number: None | str | Unset = UNSET
    """ Phone number for the tenant contact when not selecting an existing tenant """
    locale: BuyServiceMicrosoft365RequestDataLocale | Unset = UNSET
    """ Locale to use for the tenant when not selecting an existing tenant """

    def to_dict(self) -> dict[str, Any]:
        tenant_choice = self.tenant_choice.value

        tenant_select: int | None | Unset
        if isinstance(self.tenant_select, Unset):
            tenant_select = UNSET
        else:
            tenant_select = self.tenant_select

        domain_prefix: None | str | Unset
        if isinstance(self.domain_prefix, Unset):
            domain_prefix = UNSET
        else:
            domain_prefix = self.domain_prefix

        first_name: None | str | Unset
        if isinstance(self.first_name, Unset):
            first_name = UNSET
        else:
            first_name = self.first_name

        last_name: None | str | Unset
        if isinstance(self.last_name, Unset):
            last_name = UNSET
        else:
            last_name = self.last_name

        company_name: None | str | Unset
        if isinstance(self.company_name, Unset):
            company_name = UNSET
        else:
            company_name = self.company_name

        address: None | str | Unset
        if isinstance(self.address, Unset):
            address = UNSET
        else:
            address = self.address

        city: None | str | Unset
        if isinstance(self.city, Unset):
            city = UNSET
        else:
            city = self.city

        state: None | str | Unset
        if isinstance(self.state, Unset):
            state = UNSET
        else:
            state = self.state

        postal_code: None | str | Unset
        if isinstance(self.postal_code, Unset):
            postal_code = UNSET
        else:
            postal_code = self.postal_code

        country: None | str | Unset
        if isinstance(self.country, Unset):
            country = UNSET
        else:
            country = self.country

        email_address: None | str | Unset
        if isinstance(self.email_address, Unset):
            email_address = UNSET
        else:
            email_address = self.email_address

        phone_prefix: None | str | Unset
        if isinstance(self.phone_prefix, Unset):
            phone_prefix = UNSET
        else:
            phone_prefix = self.phone_prefix

        phone_number: None | str | Unset
        if isinstance(self.phone_number, Unset):
            phone_number = UNSET
        else:
            phone_number = self.phone_number

        locale: str | Unset = UNSET
        if not isinstance(self.locale, Unset):
            locale = self.locale.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "tenant_choice": tenant_choice,
            }
        )
        if tenant_select is not UNSET:
            field_dict["tenant_select"] = tenant_select
        if domain_prefix is not UNSET:
            field_dict["domain_prefix"] = domain_prefix
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if company_name is not UNSET:
            field_dict["company_name"] = company_name
        if address is not UNSET:
            field_dict["address"] = address
        if city is not UNSET:
            field_dict["city"] = city
        if state is not UNSET:
            field_dict["state"] = state
        if postal_code is not UNSET:
            field_dict["postal_code"] = postal_code
        if country is not UNSET:
            field_dict["country"] = country
        if email_address is not UNSET:
            field_dict["email_address"] = email_address
        if phone_prefix is not UNSET:
            field_dict["phone_prefix"] = phone_prefix
        if phone_number is not UNSET:
            field_dict["phone_number"] = phone_number
        if locale is not UNSET:
            field_dict["locale"] = locale

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        tenant_choice = BuyServiceMicrosoft365RequestDataTenantChoice(d.pop("tenant_choice"))

        def _parse_tenant_select(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        tenant_select = _parse_tenant_select(d.pop("tenant_select", UNSET))

        def _parse_domain_prefix(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        domain_prefix = _parse_domain_prefix(d.pop("domain_prefix", UNSET))

        def _parse_first_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        first_name = _parse_first_name(d.pop("first_name", UNSET))

        def _parse_last_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_name = _parse_last_name(d.pop("last_name", UNSET))

        def _parse_company_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_name = _parse_company_name(d.pop("company_name", UNSET))

        def _parse_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address = _parse_address(d.pop("address", UNSET))

        def _parse_city(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        city = _parse_city(d.pop("city", UNSET))

        def _parse_state(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        state = _parse_state(d.pop("state", UNSET))

        def _parse_postal_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        postal_code = _parse_postal_code(d.pop("postal_code", UNSET))

        def _parse_country(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country = _parse_country(d.pop("country", UNSET))

        def _parse_email_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email_address = _parse_email_address(d.pop("email_address", UNSET))

        def _parse_phone_prefix(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        phone_prefix = _parse_phone_prefix(d.pop("phone_prefix", UNSET))

        def _parse_phone_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        phone_number = _parse_phone_number(d.pop("phone_number", UNSET))

        _locale = d.pop("locale", UNSET)
        locale: BuyServiceMicrosoft365RequestDataLocale | Unset
        if isinstance(_locale, Unset):
            locale = UNSET
        else:
            locale = BuyServiceMicrosoft365RequestDataLocale(_locale)

        buy_service_microsoft_365_request_data = cls(
            tenant_choice=tenant_choice,
            tenant_select=tenant_select,
            domain_prefix=domain_prefix,
            first_name=first_name,
            last_name=last_name,
            company_name=company_name,
            address=address,
            city=city,
            state=state,
            postal_code=postal_code,
            country=country,
            email_address=email_address,
            phone_prefix=phone_prefix,
            phone_number=phone_number,
            locale=locale,
        )

        return buy_service_microsoft_365_request_data
