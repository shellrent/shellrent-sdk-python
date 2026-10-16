from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PurchaseCanChangeRenewStatus")


@_attrs_define
class PurchaseCanChangeRenewStatus:
    """Whether the renew status of the purchase can be changed (`PATCH /api/v3/purchases/{purchase_id}/renew-status`)"""

    purchase_id: int
    """ Id of the purchase (`GET /api/v3/purchases/{purchase_id}`) """
    can_change_renew_status: bool
    """ Whether the renew status can be set to the one in the `status` query parameter """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        purchase_id = self.purchase_id

        can_change_renew_status = self.can_change_renew_status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "purchase_id": purchase_id,
                "can_change_renew_status": can_change_renew_status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        purchase_id = d.pop("purchase_id")

        can_change_renew_status = d.pop("can_change_renew_status")

        purchase_can_change_renew_status = cls(
            purchase_id=purchase_id,
            can_change_renew_status=can_change_renew_status,
        )

        purchase_can_change_renew_status.additional_properties = d
        return purchase_can_change_renew_status

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
