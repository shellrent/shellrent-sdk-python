from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServerNetworkInterfaceCreateRequest")


@_attrs_define
class ServerNetworkInterfaceCreateRequest:
    network_id: int | Unset = UNSET
    """ For a local network interface: ID of an active local network of the cluster where the server resides (for a
    private cloud VM, a local network of the private cloud). Send either network_id or ip_address_id """
    ip_address_id: int | Unset = UNSET
    """ For a public network interface: ID of an IP address without an active network interface. For a private cloud
    VM it is a free and available IP address of the private cloud, which is assigned to the VM; for the other
    servers an available IP address of the server. Send either network_id or ip_address_id """

    def to_dict(self) -> dict[str, Any]:
        network_id = self.network_id

        ip_address_id = self.ip_address_id

        field_dict: dict[str, Any] = {}

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

        return server_network_interface_create_request
