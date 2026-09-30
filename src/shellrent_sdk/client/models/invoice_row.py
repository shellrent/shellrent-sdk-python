from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.amount import Amount
    from ..models.billing_data import BillingData
    from ..models.purchase import Purchase
    from ..models.service import Service


T = TypeVar("T", bound="InvoiceRow")


@_attrs_define
class InvoiceRow:
    invoice_row_id: int
    invoice_id: int
    invoice_id_deposit: int | None
    service: None | Service
    purchase: None | Purchase
    description: str
    unit_description: None | str
    unit_quantity: float | None
    unit_amount: Amount
    amount: Amount
    billing_data: BillingData
    is_recurring: bool
    date_start: datetime.date | None
    date_end: datetime.date | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.purchase import Purchase
        from ..models.service import Service

        invoice_row_id = self.invoice_row_id

        invoice_id = self.invoice_id

        invoice_id_deposit: int | None
        invoice_id_deposit = self.invoice_id_deposit

        service: dict[str, Any] | None
        if isinstance(self.service, Service):
            service = self.service.to_dict()
        else:
            service = self.service

        purchase: dict[str, Any] | None
        if isinstance(self.purchase, Purchase):
            purchase = self.purchase.to_dict()
        else:
            purchase = self.purchase

        description = self.description

        unit_description: None | str
        unit_description = self.unit_description

        unit_quantity: float | None
        unit_quantity = self.unit_quantity

        unit_amount = self.unit_amount.to_dict()

        amount = self.amount.to_dict()

        billing_data = self.billing_data.to_dict()

        is_recurring = self.is_recurring

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
                "invoice_row_id": invoice_row_id,
                "invoice_id": invoice_id,
                "invoice_id_deposit": invoice_id_deposit,
                "service": service,
                "purchase": purchase,
                "description": description,
                "unit_description": unit_description,
                "unit_quantity": unit_quantity,
                "unit_amount": unit_amount,
                "amount": amount,
                "billing_data": billing_data,
                "is_recurring": is_recurring,
                "date_start": date_start,
                "date_end": date_end,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.amount import Amount
        from ..models.billing_data import BillingData
        from ..models.purchase import Purchase
        from ..models.service import Service

        d = dict(src_dict)
        invoice_row_id = d.pop("invoice_row_id")

        invoice_id = d.pop("invoice_id")

        def _parse_invoice_id_deposit(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        invoice_id_deposit = _parse_invoice_id_deposit(d.pop("invoice_id_deposit"))

        def _parse_service(data: object) -> None | Service:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                service_type_0 = Service.from_dict(data)

                return service_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Service, data)

        service = _parse_service(d.pop("service"))

        def _parse_purchase(data: object) -> None | Purchase:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                purchase_type_0 = Purchase.from_dict(data)

                return purchase_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Purchase, data)

        purchase = _parse_purchase(d.pop("purchase"))

        description = d.pop("description")

        def _parse_unit_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        unit_description = _parse_unit_description(d.pop("unit_description"))

        def _parse_unit_quantity(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        unit_quantity = _parse_unit_quantity(d.pop("unit_quantity"))

        unit_amount = Amount.from_dict(d.pop("unit_amount"))

        amount = Amount.from_dict(d.pop("amount"))

        billing_data = BillingData.from_dict(d.pop("billing_data"))

        is_recurring = d.pop("is_recurring")

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

        invoice_row = cls(
            invoice_row_id=invoice_row_id,
            invoice_id=invoice_id,
            invoice_id_deposit=invoice_id_deposit,
            service=service,
            purchase=purchase,
            description=description,
            unit_description=unit_description,
            unit_quantity=unit_quantity,
            unit_amount=unit_amount,
            amount=amount,
            billing_data=billing_data,
            is_recurring=is_recurring,
            date_start=date_start,
            date_end=date_end,
        )

        invoice_row.additional_properties = d
        return invoice_row

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
