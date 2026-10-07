from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="DomainDnsNameserversCloudflareRequest")


@_attrs_define
class DomainDnsNameserversCloudflareRequest:
    account_email: str
    """ Email of the Cloudflare account that will manage the DNS zone """
    api_token: str
    """ Global API key of the Cloudflare account (not an API token), used together with `account_email` """

    def to_dict(self) -> dict[str, Any]:
        account_email = self.account_email

        api_token = self.api_token

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "account_email": account_email,
                "api_token": api_token,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        account_email = d.pop("account_email")

        api_token = d.pop("api_token")

        domain_dns_nameservers_cloudflare_request = cls(
            account_email=account_email,
            api_token=api_token,
        )

        return domain_dns_nameservers_cloudflare_request
