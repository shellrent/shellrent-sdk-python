from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..models.buy_service_ssl_certificate_request_data_admin_role import (
    BuyServiceSslCertificateRequestDataAdminRole,
)
from ..models.buy_service_ssl_certificate_request_data_admin_title import (
    BuyServiceSslCertificateRequestDataAdminTitle,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="BuyServiceSslCertificateRequestData")


@_attrs_define
class BuyServiceSslCertificateRequestData:
    """Details required to issue the SSL/TLS Certificate"""

    domain: str
    """ Main domain for the SSL Certificate """
    approver_email: str
    """ One of the email addresses accepted as "approver" email for the SSL Certificate validation """
    admin_role: BuyServiceSslCertificateRequestDataAdminRole
    admin_title: BuyServiceSslCertificateRequestDataAdminTitle
    admin_first_name: str
    admin_last_name: str
    admin_email: str
    admin_organization: str
    admin_phone_cc: str
    """ Country code phone prefix without leading "0" and without leading "+" sign; ie. "44" for UK or "39" for
    Italy """
    admin_phone_n: str
    """ Phone number without country code phone prefix """
    admin_address: str
    admin_city: str
    admin_state: str
    """ State/Province """
    admin_postcode: str
    admin_country: str
    """ ISO country code with 2 letters; ie. "IT" for Italy, "ES" for Spain """
    csr: None | str | Unset = UNSET
    """ Use this only if you wish to provide your custom-generated CSR. If you specify your own generated CSR, you
    must provide the Private Key as well. """
    private_key: None | str | Unset = UNSET
    """ Use this only if you wish to provide your custom-generated Private Key. If you specify your own generated
    Private Key, you must provide the CSR as well. """

    def to_dict(self) -> dict[str, Any]:
        domain = self.domain

        approver_email = self.approver_email

        admin_role = self.admin_role.value

        admin_title = self.admin_title.value

        admin_first_name = self.admin_first_name

        admin_last_name = self.admin_last_name

        admin_email = self.admin_email

        admin_organization = self.admin_organization

        admin_phone_cc = self.admin_phone_cc

        admin_phone_n = self.admin_phone_n

        admin_address = self.admin_address

        admin_city = self.admin_city

        admin_state = self.admin_state

        admin_postcode = self.admin_postcode

        admin_country = self.admin_country

        csr: None | str | Unset
        if isinstance(self.csr, Unset):
            csr = UNSET
        else:
            csr = self.csr

        private_key: None | str | Unset
        if isinstance(self.private_key, Unset):
            private_key = UNSET
        else:
            private_key = self.private_key

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "domain": domain,
                "approver_email": approver_email,
                "admin_role": admin_role,
                "admin_title": admin_title,
                "admin_first_name": admin_first_name,
                "admin_last_name": admin_last_name,
                "admin_email": admin_email,
                "admin_organization": admin_organization,
                "admin_phone_cc": admin_phone_cc,
                "admin_phone_n": admin_phone_n,
                "admin_address": admin_address,
                "admin_city": admin_city,
                "admin_state": admin_state,
                "admin_postcode": admin_postcode,
                "admin_country": admin_country,
            }
        )
        if csr is not UNSET:
            field_dict["csr"] = csr
        if private_key is not UNSET:
            field_dict["private_key"] = private_key

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        domain = d.pop("domain")

        approver_email = d.pop("approver_email")

        admin_role = BuyServiceSslCertificateRequestDataAdminRole(d.pop("admin_role"))

        admin_title = BuyServiceSslCertificateRequestDataAdminTitle(d.pop("admin_title"))

        admin_first_name = d.pop("admin_first_name")

        admin_last_name = d.pop("admin_last_name")

        admin_email = d.pop("admin_email")

        admin_organization = d.pop("admin_organization")

        admin_phone_cc = d.pop("admin_phone_cc")

        admin_phone_n = d.pop("admin_phone_n")

        admin_address = d.pop("admin_address")

        admin_city = d.pop("admin_city")

        admin_state = d.pop("admin_state")

        admin_postcode = d.pop("admin_postcode")

        admin_country = d.pop("admin_country")

        def _parse_csr(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        csr = _parse_csr(d.pop("csr", UNSET))

        def _parse_private_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        private_key = _parse_private_key(d.pop("private_key", UNSET))

        buy_service_ssl_certificate_request_data = cls(
            domain=domain,
            approver_email=approver_email,
            admin_role=admin_role,
            admin_title=admin_title,
            admin_first_name=admin_first_name,
            admin_last_name=admin_last_name,
            admin_email=admin_email,
            admin_organization=admin_organization,
            admin_phone_cc=admin_phone_cc,
            admin_phone_n=admin_phone_n,
            admin_address=admin_address,
            admin_city=admin_city,
            admin_state=admin_state,
            admin_postcode=admin_postcode,
            admin_country=admin_country,
            csr=csr,
            private_key=private_key,
        )

        return buy_service_ssl_certificate_request_data
