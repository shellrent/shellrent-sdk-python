from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Server")


@_attrs_define
class Server:
    server_id: int
    purchase_id: int | None
    hostname: None | str
    server_type: None | str
    active: bool
    consolidated: bool
    ip_address_id: int | None
    ip_address: None | str
    service_category_code: None | str
    date_created: datetime.datetime | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        server_id = self.server_id

        purchase_id: int | None
        purchase_id = self.purchase_id

        hostname: None | str
        hostname = self.hostname

        server_type: None | str
        server_type = self.server_type

        active = self.active

        consolidated = self.consolidated

        ip_address_id: int | None
        ip_address_id = self.ip_address_id

        ip_address: None | str
        ip_address = self.ip_address

        service_category_code: None | str
        service_category_code = self.service_category_code

        date_created: None | str
        if isinstance(self.date_created, datetime.datetime):
            date_created = self.date_created.isoformat()
        else:
            date_created = self.date_created

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "server_id": server_id,
                "purchase_id": purchase_id,
                "hostname": hostname,
                "server_type": server_type,
                "active": active,
                "consolidated": consolidated,
                "ip_address_id": ip_address_id,
                "ip_address": ip_address,
                "service_category_code": service_category_code,
                "date_created": date_created,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        server_id = d.pop("server_id")

        def _parse_purchase_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        purchase_id = _parse_purchase_id(d.pop("purchase_id"))

        def _parse_hostname(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        hostname = _parse_hostname(d.pop("hostname"))

        def _parse_server_type(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        server_type = _parse_server_type(d.pop("server_type"))

        active = d.pop("active")

        consolidated = d.pop("consolidated")

        def _parse_ip_address_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        ip_address_id = _parse_ip_address_id(d.pop("ip_address_id"))

        def _parse_ip_address(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        ip_address = _parse_ip_address(d.pop("ip_address"))

        def _parse_service_category_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        service_category_code = _parse_service_category_code(d.pop("service_category_code"))

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

        server = cls(
            server_id=server_id,
            purchase_id=purchase_id,
            hostname=hostname,
            server_type=server_type,
            active=active,
            consolidated=consolidated,
            ip_address_id=ip_address_id,
            ip_address=ip_address,
            service_category_code=service_category_code,
            date_created=date_created,
        )

        server.additional_properties = d
        return server

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
