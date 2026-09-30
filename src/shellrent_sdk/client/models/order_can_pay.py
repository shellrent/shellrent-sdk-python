from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.amount_simple import AmountSimple
    from ..models.order import Order


T = TypeVar("T", bound="OrderCanPay")


@_attrs_define
class OrderCanPay:
    order_id: int
    can_pay: bool
    amount: AmountSimple | Unset = UNSET
    orders: list[Order] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        order_id = self.order_id

        can_pay = self.can_pay

        amount: dict[str, Any] | Unset = UNSET
        if not isinstance(self.amount, Unset):
            amount = self.amount.to_dict()

        orders: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.orders, Unset):
            orders = []
            for orders_item_data in self.orders:
                orders_item = orders_item_data.to_dict()
                orders.append(orders_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "order_id": order_id,
                "can_pay": can_pay,
            }
        )
        if amount is not UNSET:
            field_dict["amount"] = amount
        if orders is not UNSET:
            field_dict["orders"] = orders

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.amount_simple import AmountSimple
        from ..models.order import Order

        d = dict(src_dict)
        order_id = d.pop("order_id")

        can_pay = d.pop("can_pay")

        _amount = d.pop("amount", UNSET)
        amount: AmountSimple | Unset
        if isinstance(_amount, Unset):
            amount = UNSET
        else:
            amount = AmountSimple.from_dict(_amount)

        _orders = d.pop("orders", UNSET)
        orders: list[Order] | Unset = UNSET
        if _orders is not UNSET:
            orders = []
            for orders_item_data in _orders:
                orders_item = Order.from_dict(orders_item_data)

                orders.append(orders_item)

        order_can_pay = cls(
            order_id=order_id,
            can_pay=can_pay,
            amount=amount,
            orders=orders,
        )

        order_can_pay.additional_properties = d
        return order_can_pay

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
