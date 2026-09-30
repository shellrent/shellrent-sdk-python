from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="IpAddress")


@_attrs_define
class IpAddress:
    ip_address_id: int
    server_id: int | None
    ip_address: str
    reverse_dns: None | str
    reverse_dns_external: None | str
    mac_address: None | str
    blocked_for_spam: bool
    active: bool
    available: bool
    date_created: datetime.datetime | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ip_address_id = self.ip_address_id

        server_id: int | None
        server_id = self.server_id

        ip_address = self.ip_address

        reverse_dns: None | str
        reverse_dns = self.reverse_dns

        reverse_dns_external: None | str
        reverse_dns_external = self.reverse_dns_external

        mac_address: None | str
        mac_address = self.mac_address

        blocked_for_spam = self.blocked_for_spam

        active = self.active

        available = self.available

        date_created: None | str
        if isinstance(self.date_created, datetime.datetime):
            date_created = self.date_created.isoformat()
        else:
            date_created = self.date_created

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ip_address_id": ip_address_id,
                "server_id": server_id,
                "ip_address": ip_address,
                "reverse_dns": reverse_dns,
                "reverse_dns_external": reverse_dns_external,
                "mac_address": mac_address,
                "blocked_for_spam": blocked_for_spam,
                "active": active,
                "available": available,
                "date_created": date_created,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        ip_address_id = d.pop("ip_address_id")

        def _parse_server_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        server_id = _parse_server_id(d.pop("server_id"))

        ip_address = d.pop("ip_address")

        def _parse_reverse_dns(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        reverse_dns = _parse_reverse_dns(d.pop("reverse_dns"))

        def _parse_reverse_dns_external(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        reverse_dns_external = _parse_reverse_dns_external(d.pop("reverse_dns_external"))

        def _parse_mac_address(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        mac_address = _parse_mac_address(d.pop("mac_address"))

        blocked_for_spam = d.pop("blocked_for_spam")

        active = d.pop("active")

        available = d.pop("available")

        def _parse_date_created(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_created_type_0 = datetime.datetime.fromisoformat(data)

                return date_created_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        date_created = _parse_date_created(d.pop("date_created"))

        ip_address = cls(
            ip_address_id=ip_address_id,
            server_id=server_id,
            ip_address=ip_address,
            reverse_dns=reverse_dns,
            reverse_dns_external=reverse_dns_external,
            mac_address=mac_address,
            blocked_for_spam=blocked_for_spam,
            active=active,
            available=available,
            date_created=date_created,
        )

        ip_address.additional_properties = d
        return ip_address

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
