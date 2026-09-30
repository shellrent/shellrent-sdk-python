from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="BuyServiceSecuremailForMicrosoft365RequestData")


@_attrs_define
class BuyServiceSecuremailForMicrosoft365RequestData:
    tenant: str
    """ Prefix of the ".onmicrosoft.com" tenant domain """
    email_domain: str
    """ Domain name for the emails to be protected """
    domain_fqn: str
    """ FQDN of the Microsoft destination domain for emails """
    client_id: str
    """ Client ID for the connector generated on admin.microsoft.com """
    client_secret: str
    """ Client secret for the connector generated on admin.microsoft.com """

    def to_dict(self) -> dict[str, Any]:
        tenant = self.tenant

        email_domain = self.email_domain

        domain_fqn = self.domain_fqn

        client_id = self.client_id

        client_secret = self.client_secret

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "tenant": tenant,
                "email_domain": email_domain,
                "domain_fqn": domain_fqn,
                "client_id": client_id,
                "client_secret": client_secret,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        tenant = d.pop("tenant")

        email_domain = d.pop("email_domain")

        domain_fqn = d.pop("domain_fqn")

        client_id = d.pop("client_id")

        client_secret = d.pop("client_secret")

        buy_service_securemail_for_microsoft_365_request_data = cls(
            tenant=tenant,
            email_domain=email_domain,
            domain_fqn=domain_fqn,
            client_id=client_id,
            client_secret=client_secret,
        )

        return buy_service_securemail_for_microsoft_365_request_data
