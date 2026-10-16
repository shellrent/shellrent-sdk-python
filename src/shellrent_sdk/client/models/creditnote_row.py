from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.amount import Amount
    from ..models.billing_data import BillingData


T = TypeVar("T", bound="CreditnoteRow")


@_attrs_define
class CreditnoteRow:
    """Row of a credit note"""

    creditnote_row_id: int
    creditnote_id: int
    """ Id of the credit note (`GET /api/v3/credit-notes/{credit_note_id}`) """
    invoice_row_id: int | None
    """ Id of the invoice row that the credit note row refers to (`GET
    /api/v3/invoices/{invoice_id}/rows/{row_id}`); null when it refers to none """
    reason: None | str
    """ Reason of the row, in Italian, for example `Errato Addebito` (wrong charge) or `Servizio non Erogato`
    (service not provided) """
    description: str
    amount: Amount
    """ Amount in euros: the taxable amount and, when computed with a tax regime, the VAT rate, the VAT and the
    total, which are null otherwise """
    billing_data: BillingData
    """ Italian public administration codes of a document row: CIG, CUP and ODA """
    date_start: datetime.date | None
    """ Start of the period the row refers to; null when the row has no period """
    date_end: datetime.date | None
    """ End of the period the row refers to; null when the row has no period """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        creditnote_row_id = self.creditnote_row_id

        creditnote_id = self.creditnote_id

        invoice_row_id: int | None
        invoice_row_id = self.invoice_row_id

        reason: None | str
        reason = self.reason

        description = self.description

        amount = self.amount.to_dict()

        billing_data = self.billing_data.to_dict()

        date_start: None | str
        if isinstance(self.date_start, datetime.date):
            date_start = self.date_start.isoformat()
        else:
            date_start = self.date_start

        date_end: None | str
        if isinstance(self.date_end, datetime.date):
            date_end = self.date_end.isoformat()
        else:
            date_end = self.date_end

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "creditnote_row_id": creditnote_row_id,
                "creditnote_id": creditnote_id,
                "invoice_row_id": invoice_row_id,
                "reason": reason,
                "description": description,
                "amount": amount,
                "billing_data": billing_data,
                "date_start": date_start,
                "date_end": date_end,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.amount import Amount
        from ..models.billing_data import BillingData

        d = dict(src_dict)
        creditnote_row_id = d.pop("creditnote_row_id")

        creditnote_id = d.pop("creditnote_id")

        def _parse_invoice_row_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        invoice_row_id = _parse_invoice_row_id(d.pop("invoice_row_id"))

        def _parse_reason(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        reason = _parse_reason(d.pop("reason"))

        description = d.pop("description")

        amount = Amount.from_dict(d.pop("amount"))

        billing_data = BillingData.from_dict(d.pop("billing_data"))

        def _parse_date_start(data: object) -> datetime.date | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_start_type_0 = datetime.date.fromisoformat(data)

                return date_start_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None, data)

        date_start = _parse_date_start(d.pop("date_start"))

        def _parse_date_end(data: object) -> datetime.date | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_end_type_0 = datetime.date.fromisoformat(data)

                return date_end_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None, data)

        date_end = _parse_date_end(d.pop("date_end"))

        creditnote_row = cls(
            creditnote_row_id=creditnote_row_id,
            creditnote_id=creditnote_id,
            invoice_row_id=invoice_row_id,
            reason=reason,
            description=description,
            amount=amount,
            billing_data=billing_data,
            date_start=date_start,
            date_end=date_end,
        )

        creditnote_row.additional_properties = d
        return creditnote_row

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
