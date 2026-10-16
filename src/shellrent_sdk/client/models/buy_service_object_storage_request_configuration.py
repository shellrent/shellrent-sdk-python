from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="BuyServiceObjectStorageRequestConfiguration")


@_attrs_define
class BuyServiceObjectStorageRequestConfiguration:
    """Object Storage configuration. If omitted, the smallest size allowed by the service is used."""

    tb_size: int | Unset = UNSET
    """ Storage size, in TB. The allowed sizes depend on the Object Storage service: from its minimum to its maximum
    quantity, in steps of 1 TB up to 5 TB and of 5 TB above (for example 1, 2, 3, 4, 5, 10, 15, 20). Any other value
    is rejected with a validation error that lists the allowed sizes. If omitted, the smallest allowed size is used.
    """

    def to_dict(self) -> dict[str, Any]:
        tb_size = self.tb_size

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if tb_size is not UNSET:
            field_dict["tb_size"] = tb_size

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        tb_size = d.pop("tb_size", UNSET)

        buy_service_object_storage_request_configuration = cls(
            tb_size=tb_size,
        )

        return buy_service_object_storage_request_configuration
