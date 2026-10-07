from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.account_billing import AccountBilling
    from ..models.amount import Amount
    from ..models.invoice import Invoice
    from ..models.order_invoice_status import OrderInvoiceStatus
    from ..models.order_payment_status import OrderPaymentStatus
    from ..models.order_status import OrderStatus
    from ..models.promotion import Promotion


T = TypeVar("T", bound="Order")


@_attrs_define
class Order:
    """Order of the account, with its statuses, amounts and invoice"""

    order_id: int
    type_: str
    """ Type of the order: `P` (purchase), `R` (renewal) or `U` (update) """
    status: OrderStatus
    """ Processing status of an order """
    payment_status: OrderPaymentStatus
    """ Payment status of an order """
    invoice_status: OrderInvoiceStatus
    """ Invoicing status of an order """
    invoice: Invoice | None
    """ Invoice of the order; null while the order is not invoiced """
    billing: AccountBilling
    """ Billing profile: the holder the documents are made out to, with its tax and electronic invoicing data """
    intent_type: str
    """ Intent of the order: `DEFAULT`, `DEPOSIT` (top-up of the prepaid credit) or `BALANCE` (paid with the prepaid
    credit) """
    date_payed: datetime.date | None
    """ Date on which the order was fully paid; null while it is not """
    date_confirmed: datetime.datetime | None
    """ When the order was confirmed with deferred payment, to be paid later; null otherwise """
    payed: bool
    """ Whether the order is fully paid """
    total_amount: Amount
    """ Amount in euros: the taxable amount and, when computed with a tax regime, the VAT rate, the VAT and the
    total, which are null otherwise """
    payment_amount: Amount
    """ Amount in euros: the taxable amount and, when computed with a tax regime, the VAT rate, the VAT and the
    total, which are null otherwise """
    origin: str
    """ Where the order was created: `web` (control panel or cart), `api` (this API), `api2` (API v2) or `cli`
    (automatic procedures, such as the renewals) """
    promotions: list[Promotion]
    """ Promotions applied to the rows of the order; those that increase the price are shown only to administrators
    """
    rows_count: int
    """ Number of rows of the order (`GET /api/v3/orders/{order_id}/rows`) """
    date_created: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.invoice import Invoice

        order_id = self.order_id

        type_ = self.type_

        status = self.status.to_dict()

        payment_status = self.payment_status.to_dict()

        invoice_status = self.invoice_status.to_dict()

        invoice: dict[str, Any] | None
        if isinstance(self.invoice, Invoice):
            invoice = self.invoice.to_dict()
        else:
            invoice = self.invoice

        billing = self.billing.to_dict()

        intent_type = self.intent_type

        date_payed: None | str
        if isinstance(self.date_payed, datetime.date):
            date_payed = self.date_payed.isoformat()
        else:
            date_payed = self.date_payed

        date_confirmed: None | str
        if isinstance(self.date_confirmed, datetime.datetime):
            date_confirmed = self.date_confirmed.isoformat()
        else:
            date_confirmed = self.date_confirmed

        payed = self.payed

        total_amount = self.total_amount.to_dict()

        payment_amount = self.payment_amount.to_dict()

        origin = self.origin

        promotions = []
        for promotions_item_data in self.promotions:
            promotions_item = promotions_item_data.to_dict()
            promotions.append(promotions_item)

        rows_count = self.rows_count

        date_created = self.date_created.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "order_id": order_id,
                "type": type_,
                "status": status,
                "payment_status": payment_status,
                "invoice_status": invoice_status,
                "invoice": invoice,
                "billing": billing,
                "intent_type": intent_type,
                "date_payed": date_payed,
                "date_confirmed": date_confirmed,
                "payed": payed,
                "total_amount": total_amount,
                "payment_amount": payment_amount,
                "origin": origin,
                "promotions": promotions,
                "rows_count": rows_count,
                "date_created": date_created,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.account_billing import AccountBilling
        from ..models.amount import Amount
        from ..models.invoice import Invoice
        from ..models.order_invoice_status import OrderInvoiceStatus
        from ..models.order_payment_status import OrderPaymentStatus
        from ..models.order_status import OrderStatus
        from ..models.promotion import Promotion

        d = dict(src_dict)
        order_id = d.pop("order_id")

        type_ = d.pop("type")

        status = OrderStatus.from_dict(d.pop("status"))

        payment_status = OrderPaymentStatus.from_dict(d.pop("payment_status"))

        invoice_status = OrderInvoiceStatus.from_dict(d.pop("invoice_status"))

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

        billing = AccountBilling.from_dict(d.pop("billing"))

        intent_type = d.pop("intent_type")

        def _parse_date_payed(data: object) -> datetime.date | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_payed_type_0 = datetime.date.fromisoformat(data)

                return date_payed_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None, data)

        date_payed = _parse_date_payed(d.pop("date_payed"))

        def _parse_date_confirmed(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_confirmed_type_0 = datetime.datetime.fromisoformat(data)

                return date_confirmed_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        date_confirmed = _parse_date_confirmed(d.pop("date_confirmed"))

        payed = d.pop("payed")

        total_amount = Amount.from_dict(d.pop("total_amount"))

        payment_amount = Amount.from_dict(d.pop("payment_amount"))

        origin = d.pop("origin")

        promotions = []
        _promotions = d.pop("promotions")
        for promotions_item_data in _promotions:
            promotions_item = Promotion.from_dict(promotions_item_data)

            promotions.append(promotions_item)

        rows_count = d.pop("rows_count")

        date_created = datetime.datetime.fromisoformat(d.pop("date_created"))

        order = cls(
            order_id=order_id,
            type_=type_,
            status=status,
            payment_status=payment_status,
            invoice_status=invoice_status,
            invoice=invoice,
            billing=billing,
            intent_type=intent_type,
            date_payed=date_payed,
            date_confirmed=date_confirmed,
            payed=payed,
            total_amount=total_amount,
            payment_amount=payment_amount,
            origin=origin,
            promotions=promotions,
            rows_count=rows_count,
            date_created=date_created,
        )

        order.additional_properties = d
        return order

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
