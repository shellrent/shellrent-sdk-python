from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="Microsoft365SubscriptionQuantityRequest")


@_attrs_define
class Microsoft365SubscriptionQuantityRequest:
    quantity: int
    """ Final number of seats for the Microsoft 365 subscription """

    def to_dict(self) -> dict[str, Any]:
        quantity = self.quantity

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "quantity": quantity,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        quantity = d.pop("quantity")

        microsoft_365_subscription_quantity_request = cls(
            quantity=quantity,
        )

        return microsoft_365_subscription_quantity_request
