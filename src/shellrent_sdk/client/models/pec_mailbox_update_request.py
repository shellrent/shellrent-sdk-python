from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PecMailboxUpdateRequest")


@_attrs_define
class PecMailboxUpdateRequest:
    report_email: str | Unset = UNSET
    """ Notification email for PEC reports. Use empty string to clear. """
    report_sms: str | Unset = UNSET
    """ Notification phone number for PEC reports. Use empty string to clear. """
    password_recovery_email: str | Unset = UNSET
    """ Email used for PEC password recovery. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        report_email = self.report_email

        report_sms = self.report_sms

        password_recovery_email = self.password_recovery_email

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if report_email is not UNSET:
            field_dict["report_email"] = report_email
        if report_sms is not UNSET:
            field_dict["report_sms"] = report_sms
        if password_recovery_email is not UNSET:
            field_dict["password_recovery_email"] = password_recovery_email

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        report_email = d.pop("report_email", UNSET)

        report_sms = d.pop("report_sms", UNSET)

        password_recovery_email = d.pop("password_recovery_email", UNSET)

        pec_mailbox_update_request = cls(
            report_email=report_email,
            report_sms=report_sms,
            password_recovery_email=password_recovery_email,
        )

        pec_mailbox_update_request.additional_properties = d
        return pec_mailbox_update_request

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
