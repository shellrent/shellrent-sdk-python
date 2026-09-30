from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.buy_service_cloud_vps_request_data_diskquantity import (
    BuyServiceCloudVpsRequestDataDISKQUANTITY,
)

T = TypeVar("T", bound="BuyServiceCloudVpsRequestData")


@_attrs_define
class BuyServiceCloudVpsRequestData:
    """Cloud VPS configuration details"""

    server_configuration_code: str
    """ One of the server Templates compatible with the "Cloud VPS Server" service to buy """
    server_template_code: str
    """ One of the server Operative Systems (OS) compatible with the "Cloud VPS Server" service to buy and with the
    chosen server Template """
    ram_quantity: int
    """ RAM in GB. Min value may change depending on chosen server configuration or template. """
    disk_quantity: BuyServiceCloudVpsRequestDataDISKQUANTITY
    """ Disk size in GB. Min value may change depending on chosen server configuration or template. """
    vcpu_quantity: int
    """ Number of vCPU. Min value may change depending on chosen server configuration or template. """

    def to_dict(self) -> dict[str, Any]:
        server_configuration_code = self.server_configuration_code

        server_template_code = self.server_template_code

        ram_quantity = self.ram_quantity

        disk_quantity = self.disk_quantity.value

        vcpu_quantity = self.vcpu_quantity

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "SERVER_CONFIGURATION_CODE": server_configuration_code,
                "SERVER_TEMPLATE_CODE": server_template_code,
                "RAM_QUANTITY": ram_quantity,
                "DISK_QUANTITY": disk_quantity,
                "VCPU_QUANTITY": vcpu_quantity,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        server_configuration_code = d.pop("SERVER_CONFIGURATION_CODE")

        server_template_code = d.pop("SERVER_TEMPLATE_CODE")

        ram_quantity = d.pop("RAM_QUANTITY")

        disk_quantity = BuyServiceCloudVpsRequestDataDISKQUANTITY(d.pop("DISK_QUANTITY"))

        vcpu_quantity = d.pop("VCPU_QUANTITY")

        buy_service_cloud_vps_request_data = cls(
            server_configuration_code=server_configuration_code,
            server_template_code=server_template_code,
            ram_quantity=ram_quantity,
            disk_quantity=disk_quantity,
            vcpu_quantity=vcpu_quantity,
        )

        return buy_service_cloud_vps_request_data
