from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Amount")


@_attrs_define
class Amount:
    amount: float | None
    """ Taxable amount """
    currency: str
    """ Currency (EUR, USD, GBP, ...) """
    tax_rate: float | None
    """ VAT rate in cents (iva/vat) """
    tax: float | None
    """ VAT (tax) amount """
    total: float | None
    """ Total amount """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount: float | None
        amount = self.amount

        currency = self.currency

        tax_rate: float | None
        tax_rate = self.tax_rate

        tax: float | None
        tax = self.tax

        total: float | None
        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "amount": amount,
                "currency": currency,
                "tax_rate": tax_rate,
                "tax": tax,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_amount(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        amount = _parse_amount(d.pop("amount"))

        currency = d.pop("currency")

        def _parse_tax_rate(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        tax_rate = _parse_tax_rate(d.pop("tax_rate"))

        def _parse_tax(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        tax = _parse_tax(d.pop("tax"))

        def _parse_total(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        total = _parse_total(d.pop("total"))

        amount = cls(
            amount=amount,
            currency=currency,
            tax_rate=tax_rate,
            tax=tax,
            total=total,
        )

        amount.additional_properties = d
        return amount

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
