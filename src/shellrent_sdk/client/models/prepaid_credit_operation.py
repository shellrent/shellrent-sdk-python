from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.amount_simple import AmountSimple
    from ..models.creditnote import Creditnote
    from ..models.prepaid_credit_operation_type import PrepaidCreditOperationType
    from ..models.prepaid_credit_topup import PrepaidCreditTopup


T = TypeVar("T", bound="PrepaidCreditOperation")


@_attrs_define
class PrepaidCreditOperation:
    """Operation on the prepaid credit, such as a top-up or a payment with the credit"""

    operation_id: int
    operation_id_related: int | None
    """ Id of the payment with the credit (`REDEMPTION`) that the operation cancels, for `REDEMPTION_CANCELLATION`
    (`GET /api/v3/prepaid-credit/operations/{operation_id}`); null for the other types """
    prepaid_credit_topup: PrepaidCreditTopup
    """ Top-up of the prepaid credit, with its deposit invoice and the credit left """
    operation_type: PrepaidCreditOperationType
    """ Type of an operation on the prepaid credit """
    creditnote: Creditnote | None
    """ Credit note issued for the operation, for `REFUND` and `CREDIT_CANCELLATION`; null for the other types """
    amount: AmountSimple
    """ Amount in euros, without the VAT details of `Amount` """
    date_created: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.creditnote import Creditnote

        operation_id = self.operation_id

        operation_id_related: int | None
        operation_id_related = self.operation_id_related

        prepaid_credit_topup = self.prepaid_credit_topup.to_dict()

        operation_type = self.operation_type.to_dict()

        creditnote: dict[str, Any] | None
        if isinstance(self.creditnote, Creditnote):
            creditnote = self.creditnote.to_dict()
        else:
            creditnote = self.creditnote

        amount = self.amount.to_dict()

        date_created = self.date_created.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "operation_id": operation_id,
                "operation_id_related": operation_id_related,
                "prepaid_credit_topup": prepaid_credit_topup,
                "operation_type": operation_type,
                "creditnote": creditnote,
                "amount": amount,
                "date_created": date_created,
            }
        )

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

        def _parse_creditnote(data: object) -> Creditnote | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                creditnote_type_0 = Creditnote.from_dict(data)

                return creditnote_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Creditnote | None, data)

        creditnote = _parse_creditnote(d.pop("creditnote"))

        amount = AmountSimple.from_dict(d.pop("amount"))

        date_created = datetime.datetime.fromisoformat(d.pop("date_created"))

        prepaid_credit_operation = cls(
            operation_id=operation_id,
            operation_id_related=operation_id_related,
            prepaid_credit_topup=prepaid_credit_topup,
            operation_type=operation_type,
            creditnote=creditnote,
            amount=amount,
            date_created=date_created,
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
