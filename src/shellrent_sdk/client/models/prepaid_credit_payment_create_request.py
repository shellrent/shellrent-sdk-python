from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="PrepaidCreditPaymentCreateRequest")


@_attrs_define
class PrepaidCreditPaymentCreateRequest:
    """Pays one or more orders together with the prepaid credit"""

    order_ids: list[int]
    """ IDs of the orders to pay together """

    def to_dict(self) -> dict[str, Any]:
        order_ids = self.order_ids

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "order_ids": order_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        order_ids = cast(list[int], d.pop("order_ids"))

        prepaid_credit_payment_create_request = cls(
            order_ids=order_ids,
        )

        return prepaid_credit_payment_create_request
