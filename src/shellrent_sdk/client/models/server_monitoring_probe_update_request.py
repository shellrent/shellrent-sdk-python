from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServerMonitoringProbeUpdateRequest")


@_attrs_define
class ServerMonitoringProbeUpdateRequest:
    notification_email: str | Unset = UNSET
    """ Notification email for this probe. Use empty string to remove the current email. """
    notification_sms: str | Unset = UNSET
    """ Notification phone number for this probe. Use empty string to remove the current SMS. """

    def to_dict(self) -> dict[str, Any]:
        notification_email = self.notification_email

        notification_sms = self.notification_sms

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if notification_email is not UNSET:
            field_dict["notification_email"] = notification_email
        if notification_sms is not UNSET:
            field_dict["notification_sms"] = notification_sms

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        notification_email = d.pop("notification_email", UNSET)

        notification_sms = d.pop("notification_sms", UNSET)

        server_monitoring_probe_update_request = cls(
            notification_email=notification_email,
            notification_sms=notification_sms,
        )

        return server_monitoring_probe_update_request
