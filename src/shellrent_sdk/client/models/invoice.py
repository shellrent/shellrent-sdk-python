from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.account_billing import AccountBilling
    from ..models.amount import Amount
    from ..models.sdi_document_status import SdiDocumentStatus
    from ..models.sdi_document_type import SdiDocumentType


T = TypeVar("T", bound="Invoice")


@_attrs_define
class Invoice:
    invoice_id: int
    billing: AccountBilling
    type_: None | str
    sdi_document_status: None | SdiDocumentStatus
    sdi_document_type: None | SdiDocumentType
    date_emitted: datetime.date
    invoice_year: int
    invoice_number: str
    invoice_caption: None | str
    invoice_caption_additional: None | str
    payed: bool
    sdi_identifier: None | str
    sdi_filename: None | str
    total_amount: Amount
    amount_no_balance: Amount
    payment_amount: Amount
    orders: list[int]
    rows_count: int
    date_created: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.sdi_document_status import SdiDocumentStatus
        from ..models.sdi_document_type import SdiDocumentType

        invoice_id = self.invoice_id

        billing = self.billing.to_dict()

        type_: None | str
        type_ = self.type_

        sdi_document_status: dict[str, Any] | None
        if isinstance(self.sdi_document_status, SdiDocumentStatus):
            sdi_document_status = self.sdi_document_status.to_dict()
        else:
            sdi_document_status = self.sdi_document_status

        sdi_document_type: dict[str, Any] | None
        if isinstance(self.sdi_document_type, SdiDocumentType):
            sdi_document_type = self.sdi_document_type.to_dict()
        else:
            sdi_document_type = self.sdi_document_type

        date_emitted = self.date_emitted.isoformat()

        invoice_year = self.invoice_year

        invoice_number = self.invoice_number

        invoice_caption: None | str
        invoice_caption = self.invoice_caption

        invoice_caption_additional: None | str
        invoice_caption_additional = self.invoice_caption_additional

        payed = self.payed

        sdi_identifier: None | str
        sdi_identifier = self.sdi_identifier

        sdi_filename: None | str
        sdi_filename = self.sdi_filename

        total_amount = self.total_amount.to_dict()

        amount_no_balance = self.amount_no_balance.to_dict()

        payment_amount = self.payment_amount.to_dict()

        orders = self.orders

        rows_count = self.rows_count

        date_created = self.date_created.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "invoice_id": invoice_id,
                "billing": billing,
                "type": type_,
                "sdi_document_status": sdi_document_status,
                "sdi_document_type": sdi_document_type,
                "date_emitted": date_emitted,
                "invoice_year": invoice_year,
                "invoice_number": invoice_number,
                "invoice_caption": invoice_caption,
                "invoice_caption_additional": invoice_caption_additional,
                "payed": payed,
                "sdi_identifier": sdi_identifier,
                "sdi_filename": sdi_filename,
                "total_amount": total_amount,
                "amount_no_balance": amount_no_balance,
                "payment_amount": payment_amount,
                "orders": orders,
                "rows_count": rows_count,
                "date_created": date_created,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.account_billing import AccountBilling
        from ..models.amount import Amount
        from ..models.sdi_document_status import SdiDocumentStatus
        from ..models.sdi_document_type import SdiDocumentType

        d = dict(src_dict)
        invoice_id = d.pop("invoice_id")

        billing = AccountBilling.from_dict(d.pop("billing"))

        def _parse_type_(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        type_ = _parse_type_(d.pop("type"))

        def _parse_sdi_document_status(data: object) -> None | SdiDocumentStatus:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                sdi_document_status_type_0 = SdiDocumentStatus.from_dict(data)

                return sdi_document_status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SdiDocumentStatus, data)

        sdi_document_status = _parse_sdi_document_status(d.pop("sdi_document_status"))

        def _parse_sdi_document_type(data: object) -> None | SdiDocumentType:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                sdi_document_type_type_0 = SdiDocumentType.from_dict(data)

                return sdi_document_type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SdiDocumentType, data)

        sdi_document_type = _parse_sdi_document_type(d.pop("sdi_document_type"))

        date_emitted = datetime.date.fromisoformat(d.pop("date_emitted"))

        invoice_year = d.pop("invoice_year")

        invoice_number = d.pop("invoice_number")

        def _parse_invoice_caption(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        invoice_caption = _parse_invoice_caption(d.pop("invoice_caption"))

        def _parse_invoice_caption_additional(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        invoice_caption_additional = _parse_invoice_caption_additional(
            d.pop("invoice_caption_additional")
        )

        payed = d.pop("payed")

        def _parse_sdi_identifier(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        sdi_identifier = _parse_sdi_identifier(d.pop("sdi_identifier"))

        def _parse_sdi_filename(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        sdi_filename = _parse_sdi_filename(d.pop("sdi_filename"))

        total_amount = Amount.from_dict(d.pop("total_amount"))

        amount_no_balance = Amount.from_dict(d.pop("amount_no_balance"))

        payment_amount = Amount.from_dict(d.pop("payment_amount"))

        orders = cast(list[int], d.pop("orders"))

        rows_count = d.pop("rows_count")

        date_created = datetime.datetime.fromisoformat(d.pop("date_created"))

        invoice = cls(
            invoice_id=invoice_id,
            billing=billing,
            type_=type_,
            sdi_document_status=sdi_document_status,
            sdi_document_type=sdi_document_type,
            date_emitted=date_emitted,
            invoice_year=invoice_year,
            invoice_number=invoice_number,
            invoice_caption=invoice_caption,
            invoice_caption_additional=invoice_caption_additional,
            payed=payed,
            sdi_identifier=sdi_identifier,
            sdi_filename=sdi_filename,
            total_amount=total_amount,
            amount_no_balance=amount_no_balance,
            payment_amount=payment_amount,
            orders=orders,
            rows_count=rows_count,
            date_created=date_created,
        )

        invoice.additional_properties = d
        return invoice

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
