from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PurchaseBillingInfoChangeRequest")


@_attrs_define
class PurchaseBillingInfoChangeRequest:
    oda: str | Unset = UNSET
    cig: str | Unset = UNSET
    cup: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        oda = self.oda

        cig = self.cig

        cup = self.cup

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
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

        purchase_billing_info_change_request.additional_properties = d
        return purchase_billing_info_change_request

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
