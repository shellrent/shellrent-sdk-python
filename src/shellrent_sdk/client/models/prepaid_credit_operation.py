from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.amount_simple import AmountSimple
    from ..models.creditnote import Creditnote
    from ..models.prepaid_credit_operation_type import PrepaidCreditOperationType
    from ..models.prepaid_credit_topup import PrepaidCreditTopup


T = TypeVar("T", bound="PrepaidCreditOperation")


@_attrs_define
class PrepaidCreditOperation:
    operation_id: int
    operation_id_related: int | None
    prepaid_credit_topup: PrepaidCreditTopup
    operation_type: PrepaidCreditOperationType
    amount: AmountSimple
    date_created: datetime.datetime
    creditnote: Creditnote | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        operation_id = self.operation_id

        operation_id_related: int | None
        operation_id_related = self.operation_id_related

        prepaid_credit_topup = self.prepaid_credit_topup.to_dict()

        operation_type = self.operation_type.to_dict()

        amount = self.amount.to_dict()

        date_created = self.date_created.isoformat()

        creditnote: dict[str, Any] | Unset = UNSET
        if not isinstance(self.creditnote, Unset):
            creditnote = self.creditnote.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "operation_id": operation_id,
                "operation_id_related": operation_id_related,
                "prepaid_credit_topup": prepaid_credit_topup,
                "operation_type": operation_type,
                "amount": amount,
                "date_created": date_created,
            }
        )
        if creditnote is not UNSET:
            field_dict["creditnote"] = creditnote

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.amount_simple import AmountSimple
        from ..models.creditnote import Creditnote
        from ..models.prepaid_credit_operation_type import (
            PrepaidCreditOperationType,
        )
        from ..models.prepaid_credit_topup import PrepaidCreditTopup

        d = dict(src_dict)
        operation_id = d.pop("operation_id")

        def _parse_operation_id_related(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        operation_id_related = _parse_operation_id_related(d.pop("operation_id_related"))

        prepaid_credit_topup = PrepaidCreditTopup.from_dict(d.pop("prepaid_credit_topup"))

        operation_type = PrepaidCreditOperationType.from_dict(d.pop("operation_type"))

        amount = AmountSimple.from_dict(d.pop("amount"))

        date_created = datetime.datetime.fromisoformat(d.pop("date_created"))

        _creditnote = d.pop("creditnote", UNSET)
        creditnote: Creditnote | Unset
        if isinstance(_creditnote, Unset):
            creditnote = UNSET
        else:
            creditnote = Creditnote.from_dict(_creditnote)

        prepaid_credit_operation = cls(
            operation_id=operation_id,
            operation_id_related=operation_id_related,
            prepaid_credit_topup=prepaid_credit_topup,
            operation_type=operation_type,
            amount=amount,
            date_created=date_created,
            creditnote=creditnote,
        )

        prepaid_credit_operation.additional_properties = d
        return prepaid_credit_operation

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
