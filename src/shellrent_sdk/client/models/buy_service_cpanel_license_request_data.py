from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.buy_service_cpanel_license_request_data_installation_type import (
    BuyServiceCpanelLicenseRequestDataInstallationType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="BuyServiceCpanelLicenseRequestData")


@_attrs_define
class BuyServiceCpanelLicenseRequestData:
    """Details about where to install the license"""

    installation_type: BuyServiceCpanelLicenseRequestDataInstallationType
    """ Choose to install the license on an active server or on external IP address """
    purchase_server: int | Unset = UNSET
    """ Id of the purchase of the server where the license will be installed (`purchase_id` of `GET
    /api/v3/servers/{server_id}`), not the id of the server. Required only if "installation_type" has value
    "internal_installation_type" """
    ip_address: str | Unset = UNSET
    """ IP address of the external host where the license will be installed to. Required only if "installation_type"
    has value "external_installation_type" """

    def to_dict(self) -> dict[str, Any]:
        installation_type = self.installation_type.value

        purchase_server = self.purchase_server

        ip_address = self.ip_address

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "installation_type": installation_type,
            }
        )
        if purchase_server is not UNSET:
            field_dict["purchase_server"] = purchase_server
        if ip_address is not UNSET:
            field_dict["ip_address"] = ip_address

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        installation_type = BuyServiceCpanelLicenseRequestDataInstallationType(
            d.pop("installation_type")
        )

        purchase_server = d.pop("purchase_server", UNSET)

        ip_address = d.pop("ip_address", UNSET)

        buy_service_cpanel_license_request_data = cls(
            installation_type=installation_type,
            purchase_server=purchase_server,
            ip_address=ip_address,
        )

        return buy_service_cpanel_license_request_data
