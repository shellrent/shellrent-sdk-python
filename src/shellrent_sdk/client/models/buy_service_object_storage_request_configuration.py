from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.buy_service_object_storage_request_configuration_tb_size import (
    BuyServiceObjectStorageRequestConfigurationTbSize,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="BuyServiceObjectStorageRequestConfiguration")


@_attrs_define
class BuyServiceObjectStorageRequestConfiguration:
    """Object Storage configuration options"""

    tb_size: BuyServiceObjectStorageRequestConfigurationTbSize | Unset = (
        BuyServiceObjectStorageRequestConfigurationTbSize.VALUE_1
    )
    """ Number of TB to allocate """

    def to_dict(self) -> dict[str, Any]:
        tb_size: int | Unset = UNSET
        if not isinstance(self.tb_size, Unset):
            tb_size = self.tb_size.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if tb_size is not UNSET:
            field_dict["tb_size"] = tb_size

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _tb_size = d.pop("tb_size", UNSET)
        tb_size: BuyServiceObjectStorageRequestConfigurationTbSize | Unset
        if isinstance(_tb_size, Unset):
            tb_size = UNSET
        else:
            tb_size = BuyServiceObjectStorageRequestConfigurationTbSize(_tb_size)

        buy_service_object_storage_request_configuration = cls(
            tb_size=tb_size,
        )

        return buy_service_object_storage_request_configuration
