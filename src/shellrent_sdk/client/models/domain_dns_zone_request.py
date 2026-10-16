from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.domain_dns_zone_request_zone_ttl import DomainDnsZoneRequestZoneTtl

T = TypeVar("T", bound="DomainDnsZoneRequest")


@_attrs_define
class DomainDnsZoneRequest:
    zone_ttl: DomainDnsZoneRequestZoneTtl
    """ TTL of the zone, in seconds, which is also the TTL of every record: one of the values of the control panel,
    from 1 to 24 hours. Only the zones on our nameservers (standard and external types) have one: with Cloudflare
    the response is 409 """

    def to_dict(self) -> dict[str, Any]:
        zone_ttl = self.zone_ttl.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "zone_ttl": zone_ttl,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        zone_ttl = DomainDnsZoneRequestZoneTtl(d.pop("zone_ttl"))

        domain_dns_zone_request = cls(
            zone_ttl=zone_ttl,
        )

        return domain_dns_zone_request
