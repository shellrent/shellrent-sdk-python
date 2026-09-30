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
    creditnote_id: int
    invoice_id: int
    billing: AccountBilling
    sdi_document_status: None | SdiDocumentStatus
    sdi_document_type: SdiDocumentType
    tax_regime: None | TaxRegime
    date_emitted: datetime.date
    creditnote_year: str
    creditnote_number: str
    creditnote_caption: None | str
    sdi_identifier: str
    sdi_filename: str
    total_amount: Amount
    rows_count: int
    date_created: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.sdi_document_status import SdiDocumentStatus
        from ..models.tax_regime import TaxRegime

        creditnote_id = self.creditnote_id

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

        creditnote_year = self.creditnote_year

        creditnote_number = self.creditnote_number

        creditnote_caption: None | str
        creditnote_caption = self.creditnote_caption

        sdi_identifier = self.sdi_identifier

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

        invoice_id = d.pop("invoice_id")

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

        creditnote_year = d.pop("creditnote_year")

        creditnote_number = d.pop("creditnote_number")

        def _parse_creditnote_caption(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        creditnote_caption = _parse_creditnote_caption(d.pop("creditnote_caption"))

        sdi_identifier = d.pop("sdi_identifier")

        sdi_filename = d.pop("sdi_filename")

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
