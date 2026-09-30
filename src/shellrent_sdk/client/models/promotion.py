from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.amount import Amount


T = TypeVar("T", bound="Promotion")


@_attrs_define
class Promotion:
    promocode: None | str
    description: str
    percentage_increase: float | None
    percentage_decrease: float | None
    amount_increase: Amount | None
    amount_decrease: Amount | None
    amount_fixed: Amount | None
    applied_amount: Amount | None
    date_applied: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.amount import Amount

        promocode: None | str
        promocode = self.promocode

        description = self.description

        percentage_increase: float | None
        percentage_increase = self.percentage_increase

        percentage_decrease: float | None
        percentage_decrease = self.percentage_decrease

        amount_increase: dict[str, Any] | None
        if isinstance(self.amount_increase, Amount):
            amount_increase = self.amount_increase.to_dict()
        else:
            amount_increase = self.amount_increase

        amount_decrease: dict[str, Any] | None
        if isinstance(self.amount_decrease, Amount):
            amount_decrease = self.amount_decrease.to_dict()
        else:
            amount_decrease = self.amount_decrease

        amount_fixed: dict[str, Any] | None
        if isinstance(self.amount_fixed, Amount):
            amount_fixed = self.amount_fixed.to_dict()
        else:
            amount_fixed = self.amount_fixed

        applied_amount: dict[str, Any] | None
        if isinstance(self.applied_amount, Amount):
            applied_amount = self.applied_amount.to_dict()
        else:
            applied_amount = self.applied_amount

        date_applied = self.date_applied.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "promocode": promocode,
                "description": description,
                "percentage_increase": percentage_increase,
                "percentage_decrease": percentage_decrease,
                "amount_increase": amount_increase,
                "amount_decrease": amount_decrease,
                "amount_fixed": amount_fixed,
                "applied_amount": applied_amount,
                "date_applied": date_applied,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.amount import Amount

        d = dict(src_dict)

        def _parse_promocode(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        promocode = _parse_promocode(d.pop("promocode"))

        description = d.pop("description")

        def _parse_percentage_increase(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        percentage_increase = _parse_percentage_increase(d.pop("percentage_increase"))

        def _parse_percentage_decrease(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        percentage_decrease = _parse_percentage_decrease(d.pop("percentage_decrease"))

        def _parse_amount_increase(data: object) -> Amount | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                amount_increase_type_0 = Amount.from_dict(data)

                return amount_increase_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Amount | None, data)

        amount_increase = _parse_amount_increase(d.pop("amount_increase"))

        def _parse_amount_decrease(data: object) -> Amount | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                amount_decrease_type_0 = Amount.from_dict(data)

                return amount_decrease_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Amount | None, data)

        amount_decrease = _parse_amount_decrease(d.pop("amount_decrease"))

        def _parse_amount_fixed(data: object) -> Amount | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                amount_fixed_type_0 = Amount.from_dict(data)

                return amount_fixed_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Amount | None, data)

        amount_fixed = _parse_amount_fixed(d.pop("amount_fixed"))

        def _parse_applied_amount(data: object) -> Amount | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                applied_amount_type_0 = Amount.from_dict(data)

                return applied_amount_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Amount | None, data)

        applied_amount = _parse_applied_amount(d.pop("applied_amount"))

        date_applied = datetime.datetime.fromisoformat(d.pop("date_applied"))

        promotion = cls(
            promocode=promocode,
            description=description,
            percentage_increase=percentage_increase,
            percentage_decrease=percentage_decrease,
            amount_increase=amount_increase,
            amount_decrease=amount_decrease,
            amount_fixed=amount_fixed,
            applied_amount=applied_amount,
            date_applied=date_applied,
        )

        promotion.additional_properties = d
        return promotion

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
