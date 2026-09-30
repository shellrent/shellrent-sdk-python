from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.amount_simple import AmountSimple
    from ..models.payment_provider_data_type_0 import PaymentProviderDataType0
    from ..models.prepaid_credit_operation import PrepaidCreditOperation


T = TypeVar("T", bound="Payment")


@_attrs_define
class Payment:
    payment_id: int
    payment_method: str
    payment_code: str
    amount_total: AmountSimple
    amount_payed: AmountSimple
    date_payment: datetime.datetime | None
    payed: bool
    prepaid_credit_operations: list[PrepaidCreditOperation]
    provider_data: None | PaymentProviderDataType0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.payment_provider_data_type_0 import PaymentProviderDataType0

        payment_id = self.payment_id

        payment_method = self.payment_method

        payment_code = self.payment_code

        amount_total = self.amount_total.to_dict()

        amount_payed = self.amount_payed.to_dict()

        date_payment: None | str
        if isinstance(self.date_payment, datetime.datetime):
            date_payment = self.date_payment.isoformat()
        else:
            date_payment = self.date_payment

        payed = self.payed

        prepaid_credit_operations = []
        for prepaid_credit_operations_item_data in self.prepaid_credit_operations:
            prepaid_credit_operations_item = prepaid_credit_operations_item_data.to_dict()
            prepaid_credit_operations.append(prepaid_credit_operations_item)

        provider_data: dict[str, Any] | None
        if isinstance(self.provider_data, PaymentProviderDataType0):
            provider_data = self.provider_data.to_dict()
        else:
            provider_data = self.provider_data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "payment_id": payment_id,
                "payment_method": payment_method,
                "payment_code": payment_code,
                "amount_total": amount_total,
                "amount_payed": amount_payed,
                "date_payment": date_payment,
                "payed": payed,
                "prepaid_credit_operations": prepaid_credit_operations,
                "provider_data": provider_data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.amount_simple import AmountSimple
        from ..models.payment_provider_data_type_0 import PaymentProviderDataType0
        from ..models.prepaid_credit_operation import PrepaidCreditOperation

        d = dict(src_dict)
        payment_id = d.pop("payment_id")

        payment_method = d.pop("payment_method")

        payment_code = d.pop("payment_code")

        amount_total = AmountSimple.from_dict(d.pop("amount_total"))

        amount_payed = AmountSimple.from_dict(d.pop("amount_payed"))

        def _parse_date_payment(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_payment_type_0 = datetime.datetime.fromisoformat(data)

                return date_payment_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        date_payment = _parse_date_payment(d.pop("date_payment"))

        payed = d.pop("payed")

        prepaid_credit_operations = []
        _prepaid_credit_operations = d.pop("prepaid_credit_operations")
        for prepaid_credit_operations_item_data in _prepaid_credit_operations:
            prepaid_credit_operations_item = PrepaidCreditOperation.from_dict(
                prepaid_credit_operations_item_data
            )

            prepaid_credit_operations.append(prepaid_credit_operations_item)

        def _parse_provider_data(data: object) -> None | PaymentProviderDataType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                provider_data_type_0 = PaymentProviderDataType0.from_dict(data)

                return provider_data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PaymentProviderDataType0, data)

        provider_data = _parse_provider_data(d.pop("provider_data"))

        payment = cls(
            payment_id=payment_id,
            payment_method=payment_method,
            payment_code=payment_code,
            amount_total=amount_total,
            amount_payed=amount_payed,
            date_payment=date_payment,
            payed=payed,
            prepaid_credit_operations=prepaid_credit_operations,
            provider_data=provider_data,
        )

        payment.additional_properties = d
        return payment

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
