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
    from ..models.tax_regime import TaxRegime


T = TypeVar("T", bound="Creditnote")


@_attrs_define
class Creditnote:
    """Credit note of the account, with its total and electronic invoicing data"""

    creditnote_id: int
    invoice_id: int | None
    """ Id of the invoice the credit note refers to (`GET /api/v3/invoices/{invoice_id}`); null when it refers to
    none """
    billing: AccountBilling
    """ Billing profile: the holder the documents are made out to, with its tax and electronic invoicing data """
    sdi_document_status: None | SdiDocumentStatus
    """ Status of the credit note on SDI, the Italian e-invoicing exchange system; null for the credit notes not
    sent through SDI, issued before electronic invoicing """
    sdi_document_type: SdiDocumentType
    """ Type of an electronic document on SDI, the Italian e-invoicing exchange system (`TipoDocumento`) """
    tax_regime: None | TaxRegime
    """ Tax regime set on the credit note; null when it uses the one of the billing profile (`billing.tax_regime`)
    """
    date_emitted: datetime.date
    """ Date of issue of the credit note """
    creditnote_year: int | None
    """ Year of the numbering of the credit note """
    creditnote_number: str
    """ Complete number of the credit note: the year followed by the number on 6 digits, for example `2025000123`
    """
    creditnote_caption: None | str
    """ Legal note of the tax regime printed on the credit note, in Italian, such as the law under which VAT is not
    applied; null when the regime has none """
    sdi_identifier: None | str
    """ Identifier assigned by SDI to the credit note; null when it has not been sent to SDI """
    sdi_filename: None | str
    """ Name of the file sent to SDI; null when not sent, and for the credit notes issued before November 2024 """
    total_amount: Amount
    """ Amount in euros: the taxable amount and, when computed with a tax regime, the VAT rate, the VAT and the
    total, which are null otherwise """
    rows_count: int
    """ Number of rows of the credit note (`GET /api/v3/credit-notes/{credit_note_id}/rows`) """
    date_created: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.sdi_document_status import SdiDocumentStatus
        from ..models.tax_regime import TaxRegime

        creditnote_id = self.creditnote_id

        invoice_id: int | None
        invoice_id = self.invoice_id

        billing = self.billing.to_dict()

        sdi_document_status: dict[str, Any] | None
        if isinstance(self.sdi_document_status, SdiDocumentStatus):
            sdi_document_status = self.sdi_document_status.to_dict()
        else:
            sdi_document_status = self.sdi_document_status

        sdi_document_type = self.sdi_document_type.to_dict()

        tax_regime: dict[str, Any] | None
        if isinstance(self.tax_regime, TaxRegime):
            tax_regime = self.tax_regime.to_dict()
        else:
            tax_regime = self.tax_regime

        date_emitted = self.date_emitted.isoformat()

        creditnote_year: int | None
        creditnote_year = self.creditnote_year

        creditnote_number = self.creditnote_number

        creditnote_caption: None | str
        creditnote_caption = self.creditnote_caption

        sdi_identifier: None | str
        sdi_identifier = self.sdi_identifier

        sdi_filename: None | str
        sdi_filename = self.sdi_filename

        total_amount = self.total_amount.to_dict()

        rows_count = self.rows_count

        date_created = self.date_created.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "creditnote_id": creditnote_id,
                "invoice_id": invoice_id,
                "billing": billing,
                "sdi_document_status": sdi_document_status,
                "sdi_document_type": sdi_document_type,
                "tax_regime": tax_regime,
                "date_emitted": date_emitted,
                "creditnote_year": creditnote_year,
                "creditnote_number": creditnote_number,
                "creditnote_caption": creditnote_caption,
                "sdi_identifier": sdi_identifier,
                "sdi_filename": sdi_filename,
                "total_amount": total_amount,
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
        from ..models.tax_regime import TaxRegime

        d = dict(src_dict)
        creditnote_id = d.pop("creditnote_id")

        def _parse_invoice_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        invoice_id = _parse_invoice_id(d.pop("invoice_id"))

        billing = AccountBilling.from_dict(d.pop("billing"))

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

        sdi_document_type = SdiDocumentType.from_dict(d.pop("sdi_document_type"))

        def _parse_tax_regime(data: object) -> None | TaxRegime:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                tax_regime_type_0 = TaxRegime.from_dict(data)

                return tax_regime_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TaxRegime, data)

        tax_regime = _parse_tax_regime(d.pop("tax_regime"))

        date_emitted = datetime.date.fromisoformat(d.pop("date_emitted"))

        def _parse_creditnote_year(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        creditnote_year = _parse_creditnote_year(d.pop("creditnote_year"))

        creditnote_number = d.pop("creditnote_number")

        def _parse_creditnote_caption(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        creditnote_caption = _parse_creditnote_caption(d.pop("creditnote_caption"))

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

        rows_count = d.pop("rows_count")

        date_created = datetime.datetime.fromisoformat(d.pop("date_created"))

        creditnote = cls(
            creditnote_id=creditnote_id,
            invoice_id=invoice_id,
            billing=billing,
            sdi_document_status=sdi_document_status,
            sdi_document_type=sdi_document_type,
            tax_regime=tax_regime,
            date_emitted=date_emitted,
            creditnote_year=creditnote_year,
            creditnote_number=creditnote_number,
            creditnote_caption=creditnote_caption,
            sdi_identifier=sdi_identifier,
            sdi_filename=sdi_filename,
            total_amount=total_amount,
            rows_count=rows_count,
            date_created=date_created,
        )

        creditnote.additional_properties = d
        return creditnote

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
