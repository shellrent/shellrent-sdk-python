from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="WebMonitoringNotices")


@_attrs_define
class WebMonitoringNotices:
    web_monitoring_id: int
    notification_email: None | str
    notification_sms: None | str
    send_ssl_notify: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        web_monitoring_id = self.web_monitoring_id

        notification_email: None | str
        notification_email = self.notification_email

        notification_sms: None | str
        notification_sms = self.notification_sms

        send_ssl_notify = self.send_ssl_notify

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "web_monitoring_id": web_monitoring_id,
                "notification_email": notification_email,
                "notification_sms": notification_sms,
                "send_ssl_notify": send_ssl_notify,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        web_monitoring_id = d.pop("web_monitoring_id")

        def _parse_notification_email(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        notification_email = _parse_notification_email(d.pop("notification_email"))

        def _parse_notification_sms(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        notification_sms = _parse_notification_sms(d.pop("notification_sms"))

        send_ssl_notify = d.pop("send_ssl_notify")

        web_monitoring_notices = cls(
            web_monitoring_id=web_monitoring_id,
            notification_email=notification_email,
            notification_sms=notification_sms,
            send_ssl_notify=send_ssl_notify,
        )

        web_monitoring_notices.additional_properties = d
        return web_monitoring_notices

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
