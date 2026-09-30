from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.amount import Amount
    from ..models.country import Country


T = TypeVar("T", bound="SmsPrice")


@_attrs_define
class SmsPrice:
    country: Country
    standard_price: Amount
    premium_price: Amount
    valid_from: datetime.datetime | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        country = self.country.to_dict()

        standard_price = self.standard_price.to_dict()

        premium_price = self.premium_price.to_dict()

        valid_from: None | str
        if isinstance(self.valid_from, datetime.datetime):
            valid_from = self.valid_from.isoformat()
        else:
            valid_from = self.valid_from

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "country": country,
                "standard_price": standard_price,
                "premium_price": premium_price,
                "valid_from": valid_from,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.amount import Amount
        from ..models.country import Country

        d = dict(src_dict)
        country = Country.from_dict(d.pop("country"))

        standard_price = Amount.from_dict(d.pop("standard_price"))

        premium_price = Amount.from_dict(d.pop("premium_price"))

        def _parse_valid_from(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                valid_from_type_0 = datetime.datetime.fromisoformat(data)

                return valid_from_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        valid_from = _parse_valid_from(d.pop("valid_from"))

        sms_price = cls(
            country=country,
            standard_price=standard_price,
            premium_price=premium_price,
            valid_from=valid_from,
        )

        sms_price.additional_properties = d
        return sms_price

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
