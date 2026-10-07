from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DnsZone")


@_attrs_define
class DnsZone:
    """DNS zone of a domain, on our nameservers or at Cloudflare"""

    zone_id: str
    """ Id of the zone on our nameservers or at Cloudflare """
    zone_name: str
    """ Name of the zone: the domain name in punycode """
    nameservers: list[str]
    """ Hostnames of the nameservers of the zone; with Cloudflare, the ones that Cloudflare assigned to it """
    ttl: int | None
    """ TTL of the zone, in seconds, which with the standard and external nameservers is also the TTL of every
    record; null with Cloudflare, whose zones have no TTL """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        zone_id = self.zone_id

        zone_name = self.zone_name

        nameservers = self.nameservers

        ttl: int | None
        ttl = self.ttl

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "zone_id": zone_id,
                "zone_name": zone_name,
                "nameservers": nameservers,
                "ttl": ttl,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        zone_id = d.pop("zone_id")

        zone_name = d.pop("zone_name")

        nameservers = cast(list[str], d.pop("nameservers"))

        def _parse_ttl(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        ttl = _parse_ttl(d.pop("ttl"))

        dns_zone = cls(
            zone_id=zone_id,
            zone_name=zone_name,
            nameservers=nameservers,
            ttl=ttl,
        )

        dns_zone.additional_properties = d
        return dns_zone

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
