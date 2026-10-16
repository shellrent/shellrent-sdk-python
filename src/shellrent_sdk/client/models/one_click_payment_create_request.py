from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="OneClickPaymentCreateRequest")


@_attrs_define
class OneClickPaymentCreateRequest:
    """Pays one or more orders together with a One-Click payment method, in a single attempt"""

    order_ids: list[int]
    """ IDs of the orders to pay together """
    one_click_id: int | Unset = UNSET
    """ The One-Click payment method to use. Without it, the default one: the first active method, in the order
    chosen by the customer. Only that method is tried """

    def to_dict(self) -> dict[str, Any]:
        order_ids = self.order_ids

        one_click_id = self.one_click_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "order_ids": order_ids,
            }
        )
        if one_click_id is not UNSET:
            field_dict["one_click_id"] = one_click_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        order_ids = cast(list[int], d.pop("order_ids"))

        one_click_id = d.pop("one_click_id", UNSET)

        one_click_payment_create_request = cls(
            order_ids=order_ids,
            one_click_id=one_click_id,
        )

        return one_click_payment_create_request
