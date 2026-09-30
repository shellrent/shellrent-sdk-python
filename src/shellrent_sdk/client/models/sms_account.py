from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.amount_simple import AmountSimple


T = TypeVar("T", bound="SmsAccount")


@_attrs_define
class SmsAccount:
    credit: AmountSimple
    sms_standard: int
    """ Estimated number of SMS messages available with "STANDARD" quality if sent to Italy """
    sms_premium: int
    """ Estimated number of SMS messages available with "PREMIUM" quality if sent to Italy """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        credit = self.credit.to_dict()

        sms_standard = self.sms_standard

        sms_premium = self.sms_premium

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "credit": credit,
                "sms_standard": sms_standard,
                "sms_premium": sms_premium,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.amount_simple import AmountSimple

        d = dict(src_dict)
        credit = AmountSimple.from_dict(d.pop("credit"))

        sms_standard = d.pop("sms_standard")

        sms_premium = d.pop("sms_premium")

        sms_account = cls(
            credit=credit,
            sms_standard=sms_standard,
            sms_premium=sms_premium,
        )

        sms_account.additional_properties = d
        return sms_account

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
