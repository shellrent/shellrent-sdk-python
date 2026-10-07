from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="DomainDnsNameserversChangeRequest")


@_attrs_define
class DomainDnsNameserversChangeRequest:
    ns_1_hostname: str
    """ Hostname of the first nameserver. It cannot be a Shellrent nameserver nor a host of the domain itself """
    ns_2_hostname: str
    """ Hostname of the second nameserver. It cannot be a Shellrent nameserver nor a host of the domain itself """
    ns_3_hostname: str | Unset = UNSET
    """ Hostname of the third nameserver (optional). It cannot be a Shellrent nameserver nor a host of the domain
    itself """
    ns_4_hostname: str | Unset = UNSET
    """ Hostname of the fourth nameserver (optional). It cannot be a Shellrent nameserver nor a host of the domain
    itself """

    def to_dict(self) -> dict[str, Any]:
        ns_1_hostname = self.ns_1_hostname

        ns_2_hostname = self.ns_2_hostname

        ns_3_hostname = self.ns_3_hostname

        ns_4_hostname = self.ns_4_hostname

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "ns_1_hostname": ns_1_hostname,
                "ns_2_hostname": ns_2_hostname,
            }
        )
        if ns_3_hostname is not UNSET:
            field_dict["ns_3_hostname"] = ns_3_hostname
        if ns_4_hostname is not UNSET:
            field_dict["ns_4_hostname"] = ns_4_hostname

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        ns_1_hostname = d.pop("ns_1_hostname")

        ns_2_hostname = d.pop("ns_2_hostname")

        ns_3_hostname = d.pop("ns_3_hostname", UNSET)

        ns_4_hostname = d.pop("ns_4_hostname", UNSET)

        domain_dns_nameservers_change_request = cls(
            ns_1_hostname=ns_1_hostname,
            ns_2_hostname=ns_2_hostname,
            ns_3_hostname=ns_3_hostname,
            ns_4_hostname=ns_4_hostname,
        )

        return domain_dns_nameservers_change_request
