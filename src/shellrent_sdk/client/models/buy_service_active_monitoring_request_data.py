from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="BuyServiceActiveMonitoringRequestData")


@_attrs_define
class BuyServiceActiveMonitoringRequestData:
    """Target to monitor with the Active Monitoring service"""

    purchase_id_server: int | Unset = UNSET
    """ Use this to activate Active Monitoring on an already active Server by specifying the server_id """
    ip_address: str | Unset = UNSET
    """ Use this to activate Active Monitoring on an additional IP address of an already active Server """
    vswitch_ip_addess: str | Unset = UNSET
    """ Use this to activate Active Monitoring on an IP address of an already active vSwitch service """
    external_hostname: str | Unset = UNSET
    """ Specify the hostname of an external host or server """
    external_ip_address: str | Unset = UNSET
    """ Specify the IP address of an external host or server to monitor """
    external_ip_address_description: str | Unset = UNSET
    """ Specify a description for the external IP address (e.g. the corresponding hostname) """

    def to_dict(self) -> dict[str, Any]:
        purchase_id_server = self.purchase_id_server

        ip_address = self.ip_address

        vswitch_ip_addess = self.vswitch_ip_addess

        external_hostname = self.external_hostname

        external_ip_address = self.external_ip_address

        external_ip_address_description = self.external_ip_address_description

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if purchase_id_server is not UNSET:
            field_dict["purchase_id_server"] = purchase_id_server
        if ip_address is not UNSET:
            field_dict["ip_address"] = ip_address
        if vswitch_ip_addess is not UNSET:
            field_dict["vswitch_ip_addess"] = vswitch_ip_addess
        if external_hostname is not UNSET:
            field_dict["external_hostname"] = external_hostname
        if external_ip_address is not UNSET:
            field_dict["external_ip_address"] = external_ip_address
        if external_ip_address_description is not UNSET:
            field_dict["external_ip_address_description"] = external_ip_address_description

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        purchase_id_server = d.pop("purchase_id_server", UNSET)

        ip_address = d.pop("ip_address", UNSET)

        vswitch_ip_addess = d.pop("vswitch_ip_addess", UNSET)

        external_hostname = d.pop("external_hostname", UNSET)

        external_ip_address = d.pop("external_ip_address", UNSET)

        external_ip_address_description = d.pop("external_ip_address_description", UNSET)

        buy_service_active_monitoring_request_data = cls(
            purchase_id_server=purchase_id_server,
            ip_address=ip_address,
            vswitch_ip_addess=vswitch_ip_addess,
            external_hostname=external_hostname,
            external_ip_address=external_ip_address,
            external_ip_address_description=external_ip_address_description,
        )

        return buy_service_active_monitoring_request_data
