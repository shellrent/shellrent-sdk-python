from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DomainDnsNameserversChangeRequest")


@_attrs_define
class DomainDnsNameserversChangeRequest:
    ns_1_hostname: str
    """ Hostname of first nameserver """
    ns_2_hostname: str
    """ Hostname of second nameserver """
    ns_1_ip: str | Unset = UNSET
    """ IP address of first nameserver """
    ns_2_ip: str | Unset = UNSET
    """ IP address of second nameserver """
    ns_3_hostname: str | Unset = UNSET
    """ Hostname of third nameserver """
    ns_3_ip: str | Unset = UNSET
    """ IP address of third nameserver """
    ns_4_hostname: str | Unset = UNSET
    """ Hostname of fourth nameserver """
    ns_4_ip: str | Unset = UNSET
    """ IP address of fourth nameserver """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ns_1_hostname = self.ns_1_hostname

        ns_2_hostname = self.ns_2_hostname

        ns_1_ip = self.ns_1_ip

        ns_2_ip = self.ns_2_ip

        ns_3_hostname = self.ns_3_hostname

        ns_3_ip = self.ns_3_ip

        ns_4_hostname = self.ns_4_hostname

        ns_4_ip = self.ns_4_ip

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ns_1_hostname": ns_1_hostname,
                "ns_2_hostname": ns_2_hostname,
            }
        )
        if ns_1_ip is not UNSET:
            field_dict["ns_1_ip"] = ns_1_ip
        if ns_2_ip is not UNSET:
            field_dict["ns_2_ip"] = ns_2_ip
        if ns_3_hostname is not UNSET:
            field_dict["ns_3_hostname"] = ns_3_hostname
        if ns_3_ip is not UNSET:
            field_dict["ns_3_ip"] = ns_3_ip
        if ns_4_hostname is not UNSET:
            field_dict["ns_4_hostname"] = ns_4_hostname
        if ns_4_ip is not UNSET:
            field_dict["ns_4_ip"] = ns_4_ip

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        ns_1_hostname = d.pop("ns_1_hostname")

        ns_2_hostname = d.pop("ns_2_hostname")

        ns_1_ip = d.pop("ns_1_ip", UNSET)

        ns_2_ip = d.pop("ns_2_ip", UNSET)

        ns_3_hostname = d.pop("ns_3_hostname", UNSET)

        ns_3_ip = d.pop("ns_3_ip", UNSET)

        ns_4_hostname = d.pop("ns_4_hostname", UNSET)

        ns_4_ip = d.pop("ns_4_ip", UNSET)

        domain_dns_nameservers_change_request = cls(
            ns_1_hostname=ns_1_hostname,
            ns_2_hostname=ns_2_hostname,
            ns_1_ip=ns_1_ip,
            ns_2_ip=ns_2_ip,
            ns_3_hostname=ns_3_hostname,
            ns_3_ip=ns_3_ip,
            ns_4_hostname=ns_4_hostname,
            ns_4_ip=ns_4_ip,
        )

        domain_dns_nameservers_change_request.additional_properties = d
        return domain_dns_nameservers_change_request

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
