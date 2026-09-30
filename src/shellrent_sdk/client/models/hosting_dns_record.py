from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="HostingDnsRecord")


@_attrs_define
class HostingDnsRecord:
    dns_record_id: int
    type_: str
    host: str
    destination: str
    priority: int | None
    weight: int | None
    port: int | None
    service: None | str
    protocol: None | str
    caa_flag: int | None
    caa_tag: None | str
    caa_can_sign_http_exchanges: bool | None
    tlsa_usage: None | str
    tlsa_selector: None | str
    tlsa_matching_type: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dns_record_id = self.dns_record_id

        type_ = self.type_

        host = self.host

        destination = self.destination

        priority: int | None
        priority = self.priority

        weight: int | None
        weight = self.weight

        port: int | None
        port = self.port

        service: None | str
        service = self.service

        protocol: None | str
        protocol = self.protocol

        caa_flag: int | None
        caa_flag = self.caa_flag

        caa_tag: None | str
        caa_tag = self.caa_tag

        caa_can_sign_http_exchanges: bool | None
        caa_can_sign_http_exchanges = self.caa_can_sign_http_exchanges

        tlsa_usage: None | str
        tlsa_usage = self.tlsa_usage

        tlsa_selector: None | str
        tlsa_selector = self.tlsa_selector

        tlsa_matching_type: None | str
        tlsa_matching_type = self.tlsa_matching_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dns_record_id": dns_record_id,
                "type": type_,
                "host": host,
                "destination": destination,
                "priority": priority,
                "weight": weight,
                "port": port,
                "service": service,
                "protocol": protocol,
                "caa_flag": caa_flag,
                "caa_tag": caa_tag,
                "caa_can_sign_http_exchanges": caa_can_sign_http_exchanges,
                "tlsa_usage": tlsa_usage,
                "tlsa_selector": tlsa_selector,
                "tlsa_matching_type": tlsa_matching_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        dns_record_id = d.pop("dns_record_id")

        type_ = d.pop("type")

        host = d.pop("host")

        destination = d.pop("destination")

        def _parse_priority(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        priority = _parse_priority(d.pop("priority"))

        def _parse_weight(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        weight = _parse_weight(d.pop("weight"))

        def _parse_port(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        port = _parse_port(d.pop("port"))

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

        def _parse_caa_flag(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        caa_flag = _parse_caa_flag(d.pop("caa_flag"))

        def _parse_caa_tag(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        caa_tag = _parse_caa_tag(d.pop("caa_tag"))

        def _parse_caa_can_sign_http_exchanges(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        caa_can_sign_http_exchanges = _parse_caa_can_sign_http_exchanges(
            d.pop("caa_can_sign_http_exchanges")
        )

        def _parse_tlsa_usage(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        tlsa_usage = _parse_tlsa_usage(d.pop("tlsa_usage"))

        def _parse_tlsa_selector(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        tlsa_selector = _parse_tlsa_selector(d.pop("tlsa_selector"))

        def _parse_tlsa_matching_type(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        tlsa_matching_type = _parse_tlsa_matching_type(d.pop("tlsa_matching_type"))

        hosting_dns_record = cls(
            dns_record_id=dns_record_id,
            type_=type_,
            host=host,
            destination=destination,
            priority=priority,
            weight=weight,
            port=port,
            service=service,
            protocol=protocol,
            caa_flag=caa_flag,
            caa_tag=caa_tag,
            caa_can_sign_http_exchanges=caa_can_sign_http_exchanges,
            tlsa_usage=tlsa_usage,
            tlsa_selector=tlsa_selector,
            tlsa_matching_type=tlsa_matching_type,
        )

        hosting_dns_record.additional_properties = d
        return hosting_dns_record

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
