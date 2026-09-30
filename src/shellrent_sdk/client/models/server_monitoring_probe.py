from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ServerMonitoringProbe")


@_attrs_define
class ServerMonitoringProbe:
    probe_id: int
    server_monitoring_id: int
    template_id: int | None
    template_code: None | str
    template_name: None | str
    monitoring_item_id: int | None
    monitoring_trigger_id: int | None
    is_default: bool
    advanced_item: bool
    is_error: bool
    monitoring_item_disabled: bool
    action_enabled: bool
    notification_email: None | str
    notification_sms: None | str
    date_problem: datetime.datetime | None
    date_last_notification: datetime.datetime | None
    active: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        probe_id = self.probe_id

        server_monitoring_id = self.server_monitoring_id

        template_id: int | None
        template_id = self.template_id

        template_code: None | str
        template_code = self.template_code

        template_name: None | str
        template_name = self.template_name

        monitoring_item_id: int | None
        monitoring_item_id = self.monitoring_item_id

        monitoring_trigger_id: int | None
        monitoring_trigger_id = self.monitoring_trigger_id

        is_default = self.is_default

        advanced_item = self.advanced_item

        is_error = self.is_error

        monitoring_item_disabled = self.monitoring_item_disabled

        action_enabled = self.action_enabled

        notification_email: None | str
        notification_email = self.notification_email

        notification_sms: None | str
        notification_sms = self.notification_sms

        date_problem: None | str
        if isinstance(self.date_problem, datetime.datetime):
            date_problem = self.date_problem.isoformat()
        else:
            date_problem = self.date_problem

        date_last_notification: None | str
        if isinstance(self.date_last_notification, datetime.datetime):
            date_last_notification = self.date_last_notification.isoformat()
        else:
            date_last_notification = self.date_last_notification

        active = self.active

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "probe_id": probe_id,
                "server_monitoring_id": server_monitoring_id,
                "template_id": template_id,
                "template_code": template_code,
                "template_name": template_name,
                "monitoring_item_id": monitoring_item_id,
                "monitoring_trigger_id": monitoring_trigger_id,
                "is_default": is_default,
                "advanced_item": advanced_item,
                "is_error": is_error,
                "monitoring_item_disabled": monitoring_item_disabled,
                "action_enabled": action_enabled,
                "notification_email": notification_email,
                "notification_sms": notification_sms,
                "date_problem": date_problem,
                "date_last_notification": date_last_notification,
                "active": active,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        probe_id = d.pop("probe_id")

        server_monitoring_id = d.pop("server_monitoring_id")

        def _parse_template_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        template_id = _parse_template_id(d.pop("template_id"))

        def _parse_template_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        template_code = _parse_template_code(d.pop("template_code"))

        def _parse_template_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        template_name = _parse_template_name(d.pop("template_name"))

        def _parse_monitoring_item_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        monitoring_item_id = _parse_monitoring_item_id(d.pop("monitoring_item_id"))

        def _parse_monitoring_trigger_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        monitoring_trigger_id = _parse_monitoring_trigger_id(d.pop("monitoring_trigger_id"))

        is_default = d.pop("is_default")

        advanced_item = d.pop("advanced_item")

        is_error = d.pop("is_error")

        monitoring_item_disabled = d.pop("monitoring_item_disabled")

        action_enabled = d.pop("action_enabled")

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

        def _parse_date_problem(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_problem_type_0 = datetime.datetime.fromisoformat(data)

                return date_problem_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        date_problem = _parse_date_problem(d.pop("date_problem"))

        def _parse_date_last_notification(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_last_notification_type_0 = datetime.datetime.fromisoformat(data)

                return date_last_notification_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        date_last_notification = _parse_date_last_notification(d.pop("date_last_notification"))

        active = d.pop("active")

        server_monitoring_probe = cls(
            probe_id=probe_id,
            server_monitoring_id=server_monitoring_id,
            template_id=template_id,
            template_code=template_code,
            template_name=template_name,
            monitoring_item_id=monitoring_item_id,
            monitoring_trigger_id=monitoring_trigger_id,
            is_default=is_default,
            advanced_item=advanced_item,
            is_error=is_error,
            monitoring_item_disabled=monitoring_item_disabled,
            action_enabled=action_enabled,
            notification_email=notification_email,
            notification_sms=notification_sms,
            date_problem=date_problem,
            date_last_notification=date_last_notification,
            active=active,
        )

        server_monitoring_probe.additional_properties = d
        return server_monitoring_probe

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
