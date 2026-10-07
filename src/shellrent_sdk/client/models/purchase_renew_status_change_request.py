from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="PurchaseRenewStatusChangeRequest")


@_attrs_define
class PurchaseRenewStatusChangeRequest:
    do_not_renew: bool
    """ If true, the purchase will not renew. """

    def to_dict(self) -> dict[str, Any]:
        do_not_renew = self.do_not_renew

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "do_not_renew": do_not_renew,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        do_not_renew = d.pop("do_not_renew")

        purchase_renew_status_change_request = cls(
            do_not_renew=do_not_renew,
        )

        return purchase_renew_status_change_request
