from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="PurchaseBillingInfoChangeRequest")


@_attrs_define
class PurchaseBillingInfoChangeRequest:
    """Billing data of the purchase to change: at least one of `oda`, `cig` and `cup`; the ones omitted stay unchanged"""

    oda: str | Unset = UNSET
    """ Number of the purchase order (ODA, "Ordine di Acquisto") of an Italian public administration, reported on
    the invoices of the purchase """
    cig: str | Unset = UNSET
    """ CIG ("Codice Identificativo Gara"), the Italian code of a public tender, reported on the invoices of the
    purchase """
    cup: str | Unset = UNSET
    """ CUP ("Codice Unico di Progetto"), the Italian code of a public investment project, reported on the invoices
    of the purchase """

    def to_dict(self) -> dict[str, Any]:
        oda = self.oda

        cig = self.cig

        cup = self.cup

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if oda is not UNSET:
            field_dict["oda"] = oda
        if cig is not UNSET:
            field_dict["cig"] = cig
        if cup is not UNSET:
            field_dict["cup"] = cup

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        oda = d.pop("oda", UNSET)

        cig = d.pop("cig", UNSET)

        cup = d.pop("cup", UNSET)

        purchase_billing_info_change_request = cls(
            oda=oda,
            cig=cig,
            cup=cup,
        )

        return purchase_billing_info_change_request
