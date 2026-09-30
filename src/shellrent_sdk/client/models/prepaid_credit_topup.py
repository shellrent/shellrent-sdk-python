from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.amount_simple import AmountSimple
    from ..models.invoice import Invoice


T = TypeVar("T", bound="PrepaidCreditTopup")


@_attrs_define
class PrepaidCreditTopup:
    topup_id: int
    invoice: Invoice | None
    initial_credit: AmountSimple
    current_credit: AmountSimple
    refund_expiry: datetime.date | None
    credit_expiry: datetime.date | None
    date_created: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.invoice import Invoice

        topup_id = self.topup_id

        invoice: dict[str, Any] | None
        if isinstance(self.invoice, Invoice):
            invoice = self.invoice.to_dict()
        else:
            invoice = self.invoice

        initial_credit = self.initial_credit.to_dict()

        current_credit = self.current_credit.to_dict()

        refund_expiry: None | str
        if isinstance(self.refund_expiry, datetime.date):
            refund_expiry = self.refund_expiry.isoformat()
        else:
            refund_expiry = self.refund_expiry

        credit_expiry: None | str
        if isinstance(self.credit_expiry, datetime.date):
            credit_expiry = self.credit_expiry.isoformat()
        else:
            credit_expiry = self.credit_expiry

        date_created = self.date_created.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "topup_id": topup_id,
                "invoice": invoice,
                "initial_credit": initial_credit,
                "current_credit": current_credit,
                "refund_expiry": refund_expiry,
                "credit_expiry": credit_expiry,
                "date_created": date_created,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.amount_simple import AmountSimple
        from ..models.invoice import Invoice

        d = dict(src_dict)
        topup_id = d.pop("topup_id")

        def _parse_invoice(data: object) -> Invoice | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invoice_type_0 = Invoice.from_dict(data)

                return invoice_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Invoice | None, data)

        invoice = _parse_invoice(d.pop("invoice"))

        initial_credit = AmountSimple.from_dict(d.pop("initial_credit"))

        current_credit = AmountSimple.from_dict(d.pop("current_credit"))

        def _parse_refund_expiry(data: object) -> datetime.date | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                refund_expiry_type_0 = datetime.date.fromisoformat(data)

                return refund_expiry_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None, data)

        refund_expiry = _parse_refund_expiry(d.pop("refund_expiry"))

        def _parse_credit_expiry(data: object) -> datetime.date | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                credit_expiry_type_0 = datetime.date.fromisoformat(data)

                return credit_expiry_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None, data)

        credit_expiry = _parse_credit_expiry(d.pop("credit_expiry"))

        date_created = datetime.datetime.fromisoformat(d.pop("date_created"))

        prepaid_credit_topup = cls(
            topup_id=topup_id,
            invoice=invoice,
            initial_credit=initial_credit,
            current_credit=current_credit,
            refund_expiry=refund_expiry,
            credit_expiry=credit_expiry,
            date_created=date_created,
        )

        prepaid_credit_topup.additional_properties = d
        return prepaid_credit_topup

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
