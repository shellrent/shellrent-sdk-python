from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.amount_simple import AmountSimple


T = TypeVar("T", bound="PrepaidCredit")


@_attrs_define
class PrepaidCredit:
    credit_amount: AmountSimple
    credit_threshold: AmountSimple | None
    threshold_exceeded: bool | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.amount_simple import AmountSimple

        credit_amount = self.credit_amount.to_dict()

        credit_threshold: dict[str, Any] | None
        if isinstance(self.credit_threshold, AmountSimple):
            credit_threshold = self.credit_threshold.to_dict()
        else:
            credit_threshold = self.credit_threshold

        threshold_exceeded: bool | None
        threshold_exceeded = self.threshold_exceeded

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "credit_amount": credit_amount,
                "credit_threshold": credit_threshold,
                "threshold_exceeded": threshold_exceeded,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.amount_simple import AmountSimple

        d = dict(src_dict)
        credit_amount = AmountSimple.from_dict(d.pop("credit_amount"))

        def _parse_credit_threshold(data: object) -> AmountSimple | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                credit_threshold_type_0 = AmountSimple.from_dict(data)

                return credit_threshold_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AmountSimple | None, data)

        credit_threshold = _parse_credit_threshold(d.pop("credit_threshold"))

        def _parse_threshold_exceeded(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        threshold_exceeded = _parse_threshold_exceeded(d.pop("threshold_exceeded"))

        prepaid_credit = cls(
            credit_amount=credit_amount,
            credit_threshold=credit_threshold,
            threshold_exceeded=threshold_exceeded,
        )

        prepaid_credit.additional_properties = d
        return prepaid_credit

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
