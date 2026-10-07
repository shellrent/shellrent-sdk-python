from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

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

    def to_dict(self) -> dict[str, Any]:
        report_email = self.report_email

        report_sms = self.report_sms

        password_recovery_email = self.password_recovery_email

        field_dict: dict[str, Any] = {}

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

        return pec_mailbox_update_request
