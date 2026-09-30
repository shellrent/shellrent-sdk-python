from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="BillingData")


@_attrs_define
class BillingData:
    cig_value: None | str
    cup_value: None | str
    oda_value: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cig_value: None | str
        cig_value = self.cig_value

        cup_value: None | str
        cup_value = self.cup_value

        oda_value: None | str
        oda_value = self.oda_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cig_value": cig_value,
                "cup_value": cup_value,
                "oda_value": oda_value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_cig_value(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        cig_value = _parse_cig_value(d.pop("cig_value"))

        def _parse_cup_value(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        cup_value = _parse_cup_value(d.pop("cup_value"))

        def _parse_oda_value(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        oda_value = _parse_oda_value(d.pop("oda_value"))

        billing_data = cls(
            cig_value=cig_value,
            cup_value=cup_value,
            oda_value=oda_value,
        )

        billing_data.additional_properties = d
        return billing_data

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
