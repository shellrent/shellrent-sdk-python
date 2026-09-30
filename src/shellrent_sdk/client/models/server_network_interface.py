from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ServerNetworkInterface")


@_attrs_define
class ServerNetworkInterface:
    network_interface_id: int
    server_id: int
    network_id: int | None
    ip_address_id: int | None
    vif_uuid: None | str
    device_name: None | str
    mac_address: None | str
    is_default: bool | None
    is_active: bool | None
    network_type: None | str
    network_label: None | str
    network_bridge: None | str
    ip_address: None | str
    date_created: datetime.datetime | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        network_interface_id = self.network_interface_id

        server_id = self.server_id

        network_id: int | None
        network_id = self.network_id

        ip_address_id: int | None
        ip_address_id = self.ip_address_id

        vif_uuid: None | str
        vif_uuid = self.vif_uuid

        device_name: None | str
        device_name = self.device_name

        mac_address: None | str
        mac_address = self.mac_address

        is_default: bool | None
        is_default = self.is_default

        is_active: bool | None
        is_active = self.is_active

        network_type: None | str
        network_type = self.network_type

        network_label: None | str
        network_label = self.network_label

        network_bridge: None | str
        network_bridge = self.network_bridge

        ip_address: None | str
        ip_address = self.ip_address

        date_created: None | str
        if isinstance(self.date_created, datetime.datetime):
            date_created = self.date_created.isoformat()
        else:
            date_created = self.date_created

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "network_interface_id": network_interface_id,
                "server_id": server_id,
                "network_id": network_id,
                "ip_address_id": ip_address_id,
                "vif_uuid": vif_uuid,
                "device_name": device_name,
                "mac_address": mac_address,
                "is_default": is_default,
                "is_active": is_active,
                "network_type": network_type,
                "network_label": network_label,
                "network_bridge": network_bridge,
                "ip_address": ip_address,
                "date_created": date_created,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        network_interface_id = d.pop("network_interface_id")

        server_id = d.pop("server_id")

        def _parse_network_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        network_id = _parse_network_id(d.pop("network_id"))

        def _parse_ip_address_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        ip_address_id = _parse_ip_address_id(d.pop("ip_address_id"))

        def _parse_vif_uuid(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        vif_uuid = _parse_vif_uuid(d.pop("vif_uuid"))

        def _parse_device_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        device_name = _parse_device_name(d.pop("device_name"))

        def _parse_mac_address(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        mac_address = _parse_mac_address(d.pop("mac_address"))

        def _parse_is_default(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        is_default = _parse_is_default(d.pop("is_default"))

        def _parse_is_active(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        is_active = _parse_is_active(d.pop("is_active"))

        def _parse_network_type(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        network_type = _parse_network_type(d.pop("network_type"))

        def _parse_network_label(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        network_label = _parse_network_label(d.pop("network_label"))

        def _parse_network_bridge(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        network_bridge = _parse_network_bridge(d.pop("network_bridge"))

        def _parse_ip_address(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        ip_address = _parse_ip_address(d.pop("ip_address"))

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

        server_network_interface = cls(
            network_interface_id=network_interface_id,
            server_id=server_id,
            network_id=network_id,
            ip_address_id=ip_address_id,
            vif_uuid=vif_uuid,
            device_name=device_name,
            mac_address=mac_address,
            is_default=is_default,
            is_active=is_active,
            network_type=network_type,
            network_label=network_label,
            network_bridge=network_bridge,
            ip_address=ip_address,
            date_created=date_created,
        )

        server_network_interface.additional_properties = d
        return server_network_interface

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
