from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.amount import Amount


T = TypeVar("T", bound="OrderRow")


@_attrs_define
class OrderRow:
    order_row_id: int
    order_id: int
    service: int | None
    purchase: int | None
    recurrence: int | None
    price: Amount
    base_price: Amount
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        order_row_id = self.order_row_id

        order_id = self.order_id

        service: int | None
        service = self.service

        purchase: int | None
        purchase = self.purchase

        recurrence: int | None
        recurrence = self.recurrence

        price = self.price.to_dict()

        base_price = self.base_price.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "order_row_id": order_row_id,
                "order_id": order_id,
                "service": service,
                "purchase": purchase,
                "recurrence": recurrence,
                "price": price,
                "base_price": base_price,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.amount import Amount

        d = dict(src_dict)
        order_row_id = d.pop("order_row_id")

        order_id = d.pop("order_id")

        def _parse_service(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        service = _parse_service(d.pop("service"))

        def _parse_purchase(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        purchase = _parse_purchase(d.pop("purchase"))

        def _parse_recurrence(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        recurrence = _parse_recurrence(d.pop("recurrence"))

        price = Amount.from_dict(d.pop("price"))

        base_price = Amount.from_dict(d.pop("base_price"))

        order_row = cls(
            order_row_id=order_row_id,
            order_id=order_id,
            service=service,
            purchase=purchase,
            recurrence=recurrence,
            price=price,
            base_price=base_price,
        )

        order_row.additional_properties = d
        return order_row

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
