from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.buy_service_private_cloud_sv_request_data_additionalbackupdiskservicequantity import (
    BuyServicePrivateCloudSvRequestDataADDITIONALBACKUPDISKSERVICEQUANTITY,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="BuyServicePrivateCloudSvRequestData")


@_attrs_define
class BuyServicePrivateCloudSvRequestData:
    """Private Cloud SV configuration options"""

    additional_backup_disk_service_quantity: (
        BuyServicePrivateCloudSvRequestDataADDITIONALBACKUPDISKSERVICEQUANTITY | Unset
    ) = BuyServicePrivateCloudSvRequestDataADDITIONALBACKUPDISKSERVICEQUANTITY.VALUE_1
    """ Choose to configure the Private Cloud with or without additional backup disk """

    def to_dict(self) -> dict[str, Any]:
        additional_backup_disk_service_quantity: int | Unset = UNSET
        if not isinstance(self.additional_backup_disk_service_quantity, Unset):
            additional_backup_disk_service_quantity = (
                self.additional_backup_disk_service_quantity.value
            )

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if additional_backup_disk_service_quantity is not UNSET:
            field_dict["ADDITIONAL_BACKUP_DISK_SERVICE_QUANTITY"] = (
                additional_backup_disk_service_quantity
            )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _additional_backup_disk_service_quantity = d.pop(
            "ADDITIONAL_BACKUP_DISK_SERVICE_QUANTITY", UNSET
        )
        additional_backup_disk_service_quantity: (
            BuyServicePrivateCloudSvRequestDataADDITIONALBACKUPDISKSERVICEQUANTITY | Unset
        )
        if isinstance(_additional_backup_disk_service_quantity, Unset):
            additional_backup_disk_service_quantity = UNSET
        else:
            additional_backup_disk_service_quantity = (
                BuyServicePrivateCloudSvRequestDataADDITIONALBACKUPDISKSERVICEQUANTITY(
                    _additional_backup_disk_service_quantity
                )
            )

        buy_service_private_cloud_sv_request_data = cls(
            additional_backup_disk_service_quantity=additional_backup_disk_service_quantity,
        )

        return buy_service_private_cloud_sv_request_data
