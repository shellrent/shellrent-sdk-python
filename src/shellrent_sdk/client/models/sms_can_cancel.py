from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SmsCanCancel")


@_attrs_define
class SmsCanCancel:
    sms_id: int
    can_cancel: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sms_id = self.sms_id

        can_cancel = self.can_cancel

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sms_id": sms_id,
                "can_cancel": can_cancel,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        sms_id = d.pop("sms_id")

        can_cancel = d.pop("can_cancel")

        sms_can_cancel = cls(
            sms_id=sms_id,
            can_cancel=can_cancel,
        )

        sms_can_cancel.additional_properties = d
        return sms_can_cancel

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
