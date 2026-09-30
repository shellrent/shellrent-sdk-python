from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OneClick")


@_attrs_define
class OneClick:
    one_click_id: int
    payment_method: str
    description: str
    method_type: None | str
    creditcard_pan: None | str
    date_expiry: datetime.date | None
    date_created: datetime.datetime
    one_click_preference: list[OneClick] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        one_click_id = self.one_click_id

        payment_method = self.payment_method

        description = self.description

        method_type: None | str
        method_type = self.method_type

        creditcard_pan: None | str
        creditcard_pan = self.creditcard_pan

        date_expiry: None | str
        if isinstance(self.date_expiry, datetime.date):
            date_expiry = self.date_expiry.isoformat()
        else:
            date_expiry = self.date_expiry

        date_created = self.date_created.isoformat()

        one_click_preference: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.one_click_preference, Unset):
            one_click_preference = []
            for one_click_preference_item_data in self.one_click_preference:
                one_click_preference_item = one_click_preference_item_data.to_dict()
                one_click_preference.append(one_click_preference_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "one_click_id": one_click_id,
                "payment_method": payment_method,
                "description": description,
                "method_type": method_type,
                "creditcard_pan": creditcard_pan,
                "date_expiry": date_expiry,
                "date_created": date_created,
            }
        )
        if one_click_preference is not UNSET:
            field_dict["one_click_preference"] = one_click_preference

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        one_click_id = d.pop("one_click_id")

        payment_method = d.pop("payment_method")

        description = d.pop("description")

        def _parse_method_type(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        method_type = _parse_method_type(d.pop("method_type"))

        def _parse_creditcard_pan(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        creditcard_pan = _parse_creditcard_pan(d.pop("creditcard_pan"))

        def _parse_date_expiry(data: object) -> datetime.date | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_expiry_type_0 = datetime.date.fromisoformat(data)

                return date_expiry_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None, data)

        date_expiry = _parse_date_expiry(d.pop("date_expiry"))

        date_created = datetime.datetime.fromisoformat(d.pop("date_created"))

        _one_click_preference = d.pop("one_click_preference", UNSET)
        one_click_preference: list[OneClick] | Unset = UNSET
        if _one_click_preference is not UNSET:
            one_click_preference = []
            for one_click_preference_item_data in _one_click_preference:
                one_click_preference_item = OneClick.from_dict(one_click_preference_item_data)

                one_click_preference.append(one_click_preference_item)

        one_click = cls(
            one_click_id=one_click_id,
            payment_method=payment_method,
            description=description,
            method_type=method_type,
            creditcard_pan=creditcard_pan,
            date_expiry=date_expiry,
            date_created=date_created,
            one_click_preference=one_click_preference,
        )

        one_click.additional_properties = d
        return one_click

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
