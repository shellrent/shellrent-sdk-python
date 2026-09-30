from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WebMonitoringNoticesUpdateRequest")


@_attrs_define
class WebMonitoringNoticesUpdateRequest:
    notification_email: str | Unset = UNSET
    """ Notification email. Use empty string to clear. """
    notification_sms: str | Unset = UNSET
    """ Notification phone number. Use empty string to clear. """
    send_ssl_notify: bool | Unset = UNSET
    """ Enable or disable SSL expiry notices. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        notification_email = self.notification_email

        notification_sms = self.notification_sms

        send_ssl_notify = self.send_ssl_notify

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if notification_email is not UNSET:
            field_dict["notification_email"] = notification_email
        if notification_sms is not UNSET:
            field_dict["notification_sms"] = notification_sms
        if send_ssl_notify is not UNSET:
            field_dict["send_ssl_notify"] = send_ssl_notify

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        notification_email = d.pop("notification_email", UNSET)

        notification_sms = d.pop("notification_sms", UNSET)

        send_ssl_notify = d.pop("send_ssl_notify", UNSET)

        web_monitoring_notices_update_request = cls(
            notification_email=notification_email,
            notification_sms=notification_sms,
            send_ssl_notify=send_ssl_notify,
        )

        web_monitoring_notices_update_request.additional_properties = d
        return web_monitoring_notices_update_request

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
