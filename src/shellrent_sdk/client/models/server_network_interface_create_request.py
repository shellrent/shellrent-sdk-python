from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServerNetworkInterfaceCreateRequest")


@_attrs_define
class ServerNetworkInterfaceCreateRequest:
    network_id: int | Unset = UNSET
    """ Local network ID (for local VIF) """
    ip_address_id: int | Unset = UNSET
    """ Server IP address ID (for public VIF) """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        network_id = self.network_id

        ip_address_id = self.ip_address_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if network_id is not UNSET:
            field_dict["network_id"] = network_id
        if ip_address_id is not UNSET:
            field_dict["ip_address_id"] = ip_address_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        network_id = d.pop("network_id", UNSET)

        ip_address_id = d.pop("ip_address_id", UNSET)

        server_network_interface_create_request = cls(
            network_id=network_id,
            ip_address_id=ip_address_id,
        )

        server_network_interface_create_request.additional_properties = d
        return server_network_interface_create_request

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
