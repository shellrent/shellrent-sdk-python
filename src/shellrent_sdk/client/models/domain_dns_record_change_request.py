from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domain_dns_record_change_request_caa_data import (
        DomainDnsRecordChangeRequestCaaData,
    )
    from ..models.domain_dns_record_change_request_tlsa_data import (
        DomainDnsRecordChangeRequestTlsaData,
    )


T = TypeVar("T", bound="DomainDnsRecordChangeRequest")


@_attrs_define
class DomainDnsRecordChangeRequest:
    host: str
    destination: str
    service: str | Unset = UNSET
    protocol: str | Unset = UNSET
    port: str | Unset = UNSET
    weight: str | Unset = UNSET
    priority: str | Unset = UNSET
    ttl: int | Unset = UNSET
    proxied: bool | Unset = UNSET
    caa_data: DomainDnsRecordChangeRequestCaaData | Unset = UNSET
    """ Use this for CAA type record only """
    tlsa_data: DomainDnsRecordChangeRequestTlsaData | Unset = UNSET
    """ Use this for TLSA type record only """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        host = self.host

        destination = self.destination

        service = self.service

        protocol = self.protocol

        port = self.port

        weight = self.weight

        priority = self.priority

        ttl = self.ttl

        proxied = self.proxied

        caa_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.caa_data, Unset):
            caa_data = self.caa_data.to_dict()

        tlsa_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tlsa_data, Unset):
            tlsa_data = self.tlsa_data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "host": host,
                "destination": destination,
            }
        )
        if service is not UNSET:
            field_dict["service"] = service
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
        if port is not UNSET:
            field_dict["port"] = port
        if weight is not UNSET:
            field_dict["weight"] = weight
        if priority is not UNSET:
            field_dict["priority"] = priority
        if ttl is not UNSET:
            field_dict["ttl"] = ttl
        if proxied is not UNSET:
            field_dict["proxied"] = proxied
        if caa_data is not UNSET:
            field_dict["caa_data"] = caa_data
        if tlsa_data is not UNSET:
            field_dict["tlsa_data"] = tlsa_data

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.domain_dns_record_change_request_caa_data import (
            DomainDnsRecordChangeRequestCaaData,
        )
        from ..models.domain_dns_record_change_request_tlsa_data import (
            DomainDnsRecordChangeRequestTlsaData,
        )

        d = dict(src_dict)
        host = d.pop("host")

        destination = d.pop("destination")

        service = d.pop("service", UNSET)

        protocol = d.pop("protocol", UNSET)

        port = d.pop("port", UNSET)

        weight = d.pop("weight", UNSET)

        priority = d.pop("priority", UNSET)

        ttl = d.pop("ttl", UNSET)

        proxied = d.pop("proxied", UNSET)

        _caa_data = d.pop("caa_data", UNSET)
        caa_data: DomainDnsRecordChangeRequestCaaData | Unset
        if isinstance(_caa_data, Unset):
            caa_data = UNSET
        else:
            caa_data = DomainDnsRecordChangeRequestCaaData.from_dict(_caa_data)

        _tlsa_data = d.pop("tlsa_data", UNSET)
        tlsa_data: DomainDnsRecordChangeRequestTlsaData | Unset
        if isinstance(_tlsa_data, Unset):
            tlsa_data = UNSET
        else:
            tlsa_data = DomainDnsRecordChangeRequestTlsaData.from_dict(_tlsa_data)

        domain_dns_record_change_request = cls(
            host=host,
            destination=destination,
            service=service,
            protocol=protocol,
            port=port,
            weight=weight,
            priority=priority,
            ttl=ttl,
            proxied=proxied,
            caa_data=caa_data,
            tlsa_data=tlsa_data,
        )

        domain_dns_record_change_request.additional_properties = d
        return domain_dns_record_change_request

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
