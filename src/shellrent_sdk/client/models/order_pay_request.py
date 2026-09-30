from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OrderPayRequest")


@_attrs_define
class OrderPayRequest:
    """Pays one or more orders. The payment mode is chosen by three fields, evaluated in this order: 1) use_prepaid_credit
    set to true: pays with the available Prepaid Credit; 2) use_one_click set to true: tries the saved One-Click payment
    methods in priority order until one is successfully authorized; 3) one_click_id: pays with that specific One-Click
    payment method. Provide one of them: if more are provided, only the first one in this order is used. If none is
    provided the request fails, unless the amount to pay is zero: in that case no payment mode is needed.

    """

    order_ids: list[int]
    """ IDs of the orders to be paid (1 ID or more order IDs to pay together) """
    use_prepaid_credit: bool | Unset = UNSET
    """ Payment mode 1: set to true to pay with the available Prepaid Credit. Takes precedence over use_one_click
    and one_click_id. """
    use_one_click: bool | Unset = UNSET
    """ Payment mode 2: set to true to use the saved One-Click payment methods. Payment will be attempted using
    saved methods in priority order until one is successfully authorized. Ignored if use_prepaid_credit is true;
    takes precedence over one_click_id. """
    one_click_id: int | Unset = UNSET
    """ Payment mode 3: identifier of the One-Click payment method to use, to pay only with that specific method.
    Ignored if use_prepaid_credit or use_one_click is true. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        order_ids = self.order_ids

        use_prepaid_credit = self.use_prepaid_credit

        use_one_click = self.use_one_click

        one_click_id = self.one_click_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "order_ids": order_ids,
            }
        )
        if use_prepaid_credit is not UNSET:
            field_dict["use_prepaid_credit"] = use_prepaid_credit
        if use_one_click is not UNSET:
            field_dict["use_one_click"] = use_one_click
        if one_click_id is not UNSET:
            field_dict["one_click_id"] = one_click_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        order_ids = cast(list[int], d.pop("order_ids"))

        use_prepaid_credit = d.pop("use_prepaid_credit", UNSET)

        use_one_click = d.pop("use_one_click", UNSET)

        one_click_id = d.pop("one_click_id", UNSET)

        order_pay_request = cls(
            order_ids=order_ids,
            use_prepaid_credit=use_prepaid_credit,
            use_one_click=use_one_click,
            one_click_id=one_click_id,
        )

        order_pay_request.additional_properties = d
        return order_pay_request

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
