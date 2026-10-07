from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.dns_record_caa_data import DnsRecordCaaData
    from ..models.dns_record_tlsa_data import DnsRecordTlsaData


T = TypeVar("T", bound="DnsRecord")


@_attrs_define
class DnsRecord:
    """Record of the DNS zone of a domain"""

    record_id: str
    type_: str
    """ Type of the record, for example `A`, `CNAME`, `MX` or `TXT` """
    host: str
    """ Name of the record relative to the zone, `@` for the domain itself; for SRV and TLSA records, without the
    service and the protocol """
    service: None | str
    """ Service of SRV records (for example `_sip`) and port of TLSA records (for example `_443`), with the
    underscore; null for the other types """
    protocol: None | str
    """ Protocol of SRV and TLSA records: `_tcp`, `_udp` or `_tls`; null for the other types """
    destination: str
    """ Value of the record: the IPv4 address for A, the IPv6 address for AAAA, the target hostname for CNAME, MX,
    NS, PTR and SRV, the text for TXT and SPF, the value of the tag for CAA, the certificate association data for
    TLSA """
    port: None | str
    """ Port of the service, for SRV records; null for the other types """
    weight: int | None
    """ Weight of SRV records; `0` for the other types """
    priority: int | None
    """ Priority of MX and SRV records; null for the other types and, with the standard and external nameservers,
    when it is `0` """
    ttl: int | None
    """ TTL of the record, in seconds: with Cloudflare null means automatic, with the standard and external
    nameservers it is the TTL of the zone (`PATCH /api/v3/domains/{domain_id}/dns`) """
    proxied: bool
    """ Whether the traffic of the record goes through the Cloudflare proxy; always false with the other nameserver
    types """
    caa_data: DnsRecordCaaData | None
    """ Data of CAA records; null for the other types """
    tlsa_data: DnsRecordTlsaData | None
    """ Data of TLSA records; null for the other types """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.dns_record_caa_data import DnsRecordCaaData
        from ..models.dns_record_tlsa_data import DnsRecordTlsaData

        record_id = self.record_id

        type_ = self.type_

        host = self.host

        service: None | str
        service = self.service

        protocol: None | str
        protocol = self.protocol

        destination = self.destination

        port: None | str
        port = self.port

        weight: int | None
        weight = self.weight

        priority: int | None
        priority = self.priority

        ttl: int | None
        ttl = self.ttl

        proxied = self.proxied

        caa_data: dict[str, Any] | None
        if isinstance(self.caa_data, DnsRecordCaaData):
            caa_data = self.caa_data.to_dict()
        else:
            caa_data = self.caa_data

        tlsa_data: dict[str, Any] | None
        if isinstance(self.tlsa_data, DnsRecordTlsaData):
            tlsa_data = self.tlsa_data.to_dict()
        else:
            tlsa_data = self.tlsa_data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "record_id": record_id,
                "type": type_,
                "host": host,
                "service": service,
                "protocol": protocol,
                "destination": destination,
                "port": port,
                "weight": weight,
                "priority": priority,
                "ttl": ttl,
                "proxied": proxied,
                "caa_data": caa_data,
                "tlsa_data": tlsa_data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.dns_record_caa_data import DnsRecordCaaData
        from ..models.dns_record_tlsa_data import DnsRecordTlsaData

        d = dict(src_dict)
        record_id = d.pop("record_id")

        type_ = d.pop("type")

        host = d.pop("host")

        def _parse_service(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        service = _parse_service(d.pop("service"))

        def _parse_protocol(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        protocol = _parse_protocol(d.pop("protocol"))

        destination = d.pop("destination")

        def _parse_port(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        port = _parse_port(d.pop("port"))

        def _parse_weight(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        weight = _parse_weight(d.pop("weight"))

        def _parse_priority(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        priority = _parse_priority(d.pop("priority"))

        def _parse_ttl(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        ttl = _parse_ttl(d.pop("ttl"))

        proxied = d.pop("proxied")

        def _parse_caa_data(data: object) -> DnsRecordCaaData | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                caa_data_type_0 = DnsRecordCaaData.from_dict(data)

                return caa_data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DnsRecordCaaData | None, data)

        caa_data = _parse_caa_data(d.pop("caa_data"))

        def _parse_tlsa_data(data: object) -> DnsRecordTlsaData | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                tlsa_data_type_0 = DnsRecordTlsaData.from_dict(data)

                return tlsa_data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DnsRecordTlsaData | None, data)

        tlsa_data = _parse_tlsa_data(d.pop("tlsa_data"))

        dns_record = cls(
            record_id=record_id,
            type_=type_,
            host=host,
            service=service,
            protocol=protocol,
            destination=destination,
            port=port,
            weight=weight,
            priority=priority,
            ttl=ttl,
            proxied=proxied,
            caa_data=caa_data,
            tlsa_data=tlsa_data,
        )

        dns_record.additional_properties = d
        return dns_record

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
