from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

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
    """Microsoft 365 tenant of the subscription. All the data is checked before the order is created: with "select" the
    tenant must be one of the account (409 if it already has 2 active subscriptions of the same service); with
    "transfer" and "new" no tenant can have the domain prefix already, and at Microsoft the ".onmicrosoft.com" domain
    must exist ("transfer") or be available ("new"), otherwise 409. Send only the fields of the chosen option.

    """

    tenant_choice: BuyServiceMicrosoft365RequestDataTenantChoice
    """ Select whether to choose an existing tenant ("select"), transfer one ("transfer") or create a new tenant
    ("new"). When transferring a tenant, approve the Microsoft Partner Relationship before sending API requests """
    tenant_select: int | Unset = UNSET
    """ ID of the tenant to which to assign the subscription, as listed by `GET /api/v3/shop/microsoft-365/tenants`.
    Required with "select", not allowed otherwise """
    domain_prefix: str | Unset = UNSET
    """ Prefix of the ".onmicrosoft.com" tenant domain: lowercase letters and digits, at most 27 characters.
    Required with "transfer" and "new", not allowed otherwise """
    first_name: str | Unset = UNSET
    """ Contact first name for the tenant: letters, spaces and hyphens. Required with "transfer" and "new", not
    allowed otherwise """
    last_name: str | Unset = UNSET
    """ Contact last name for the tenant: letters, spaces and hyphens. Required with "transfer" and "new", not
    allowed otherwise """
    company_name: str | Unset = UNSET
    """ Company name for the tenant: letters, digits and spaces. Required with "transfer" and "new", not allowed
    otherwise """
    address: str | Unset = UNSET
    """ Address for the tenant. Required with "transfer" and "new", not allowed otherwise """
    city: str | Unset = UNSET
    """ City for the tenant address: letters, spaces and hyphens. Required with "transfer" and "new", not allowed
    otherwise """
    state: str | Unset = UNSET
    """ State/Province for the tenant address: letters, spaces and hyphens. Required with "transfer" and "new", not
    allowed otherwise """
    postal_code: str | Unset = UNSET
    """ Postal code for the tenant address: letters, digits and spaces. Required with "transfer" and "new", not
    allowed otherwise """
    country: str | Unset = UNSET
    """ ISO country code with 2 letters (e.g. "IT" or "ES"). Required with "transfer" and "new", not allowed
    otherwise """
    email_address: str | Unset = UNSET
    """ Administrative email address for the tenant. Required with "transfer" and "new", not allowed otherwise """
    phone_prefix: str | Unset = UNSET
    """ International phone prefix of a country, with the leading "+" sign (e.g. "+44" for UK or "+39" for Italy).
    Required with "transfer" and "new", not allowed otherwise """
    phone_number: str | Unset = UNSET
    """ Phone number for the tenant contact: from 3 to 25 digits, spaces, dots, hyphens and parentheses. Required
    with "transfer" and "new", not allowed otherwise """
    locale: BuyServiceMicrosoft365RequestDataLocale | Unset = UNSET
    """ Locale to use for the tenant. Required with "transfer" and "new", not allowed otherwise """

    def to_dict(self) -> dict[str, Any]:
        tenant_choice = self.tenant_choice.value

        tenant_select = self.tenant_select

        domain_prefix = self.domain_prefix

        first_name = self.first_name

        last_name = self.last_name

        company_name = self.company_name

        address = self.address

        city = self.city

        state = self.state

        postal_code = self.postal_code

        country = self.country

        email_address = self.email_address

        phone_prefix = self.phone_prefix

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

        tenant_select = d.pop("tenant_select", UNSET)

        domain_prefix = d.pop("domain_prefix", UNSET)

        first_name = d.pop("first_name", UNSET)

        last_name = d.pop("last_name", UNSET)

        company_name = d.pop("company_name", UNSET)

        address = d.pop("address", UNSET)

        city = d.pop("city", UNSET)

        state = d.pop("state", UNSET)

        postal_code = d.pop("postal_code", UNSET)

        country = d.pop("country", UNSET)

        email_address = d.pop("email_address", UNSET)

        phone_prefix = d.pop("phone_prefix", UNSET)

        phone_number = d.pop("phone_number", UNSET)

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
