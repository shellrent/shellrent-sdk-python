from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.amount_simple import AmountSimple
    from ..models.order import Order


T = TypeVar("T", bound="OrderCanPay")


@_attrs_define
class OrderCanPay:
    """Whether an order can be paid, with the orders to pay together with it"""

    order_id: int
    """ Id of the order (`GET /api/v3/orders/{order_id}`) """
    amount: AmountSimple | None
    """ Amount to pay with the payment method of the request, the commission of the method included; null when the
    order cannot be paid with it """
    orders: list[Order]
    """ Orders paid together with this one; empty when the order cannot be paid """
    can_pay: bool
    """ Whether the order can be paid now with the payment method of the request, together with the orders in
    `orders`: the One-Click method is active and not expired, the prepaid credit can be used for these orders and is
    enough """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.amount_simple import AmountSimple

        order_id = self.order_id

        amount: dict[str, Any] | None
        if isinstance(self.amount, AmountSimple):
            amount = self.amount.to_dict()
        else:
            amount = self.amount

        orders = []
        for orders_item_data in self.orders:
            orders_item = orders_item_data.to_dict()
            orders.append(orders_item)

        can_pay = self.can_pay

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "order_id": order_id,
                "amount": amount,
                "orders": orders,
                "can_pay": can_pay,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.amount_simple import AmountSimple
        from ..models.order import Order

        d = dict(src_dict)
        order_id = d.pop("order_id")

        def _parse_amount(data: object) -> AmountSimple | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                amount_type_0 = AmountSimple.from_dict(data)

                return amount_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AmountSimple | None, data)

        amount = _parse_amount(d.pop("amount"))

        orders = []
        _orders = d.pop("orders")
        for orders_item_data in _orders:
            orders_item = Order.from_dict(orders_item_data)

            orders.append(orders_item)

        can_pay = d.pop("can_pay")

        order_can_pay = cls(
            order_id=order_id,
            amount=amount,
            orders=orders,
            can_pay=can_pay,
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
