from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.buy_prepaid_credit_topup_request_amount import BuyPrepaidCreditTopupRequestAmount

T = TypeVar("T", bound="BuyPrepaidCreditTopupRequest")


@_attrs_define
class BuyPrepaidCreditTopupRequest:
    amount: BuyPrepaidCreditTopupRequestAmount
    """ Amount of the top-up in euros, before VAT: the order adds the VAT, and the credit loaded is the total with
    VAT """

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "amount": amount,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        amount = BuyPrepaidCreditTopupRequestAmount(d.pop("amount"))

        buy_prepaid_credit_topup_request = cls(
            amount=amount,
        )

        return buy_prepaid_credit_topup_request
