from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ServerMonitoring")


@_attrs_define
class ServerMonitoring:
    server_monitoring_id: int
    purchase_monitoring_id: int | None
    purchase_server_id: int | None
    service_name: None | str
    purchase_name: None | str
    purchase_status_code: None | str
    monitoring_key: None | str
    is_server_monitored: bool
    is_ip_monitored: bool
    is_external_device_monitored: bool
    monitoring_host_enabled: bool
    monitoring_type: None | str
    probe_limit: int | None
    severity_level: None | str
    email_notification: None | str
    sms_notification: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        server_monitoring_id = self.server_monitoring_id

        purchase_monitoring_id: int | None
        purchase_monitoring_id = self.purchase_monitoring_id

        purchase_server_id: int | None
        purchase_server_id = self.purchase_server_id

        service_name: None | str
        service_name = self.service_name

        purchase_name: None | str
        purchase_name = self.purchase_name

        purchase_status_code: None | str
        purchase_status_code = self.purchase_status_code

        monitoring_key: None | str
        monitoring_key = self.monitoring_key

        is_server_monitored = self.is_server_monitored

        is_ip_monitored = self.is_ip_monitored

        is_external_device_monitored = self.is_external_device_monitored

        monitoring_host_enabled = self.monitoring_host_enabled

        monitoring_type: None | str
        monitoring_type = self.monitoring_type

        probe_limit: int | None
        probe_limit = self.probe_limit

        severity_level: None | str
        severity_level = self.severity_level

        email_notification: None | str
        email_notification = self.email_notification

        sms_notification: None | str
        sms_notification = self.sms_notification

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "server_monitoring_id": server_monitoring_id,
                "purchase_monitoring_id": purchase_monitoring_id,
                "purchase_server_id": purchase_server_id,
                "service_name": service_name,
                "purchase_name": purchase_name,
                "purchase_status_code": purchase_status_code,
                "monitoring_key": monitoring_key,
                "is_server_monitored": is_server_monitored,
                "is_ip_monitored": is_ip_monitored,
                "is_external_device_monitored": is_external_device_monitored,
                "monitoring_host_enabled": monitoring_host_enabled,
                "monitoring_type": monitoring_type,
                "probe_limit": probe_limit,
                "severity_level": severity_level,
                "email_notification": email_notification,
                "sms_notification": sms_notification,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        server_monitoring_id = d.pop("server_monitoring_id")

        def _parse_purchase_monitoring_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        purchase_monitoring_id = _parse_purchase_monitoring_id(d.pop("purchase_monitoring_id"))

        def _parse_purchase_server_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        purchase_server_id = _parse_purchase_server_id(d.pop("purchase_server_id"))

        def _parse_service_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        service_name = _parse_service_name(d.pop("service_name"))

        def _parse_purchase_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        purchase_name = _parse_purchase_name(d.pop("purchase_name"))

        def _parse_purchase_status_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        purchase_status_code = _parse_purchase_status_code(d.pop("purchase_status_code"))

        def _parse_monitoring_key(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        monitoring_key = _parse_monitoring_key(d.pop("monitoring_key"))

        is_server_monitored = d.pop("is_server_monitored")

        is_ip_monitored = d.pop("is_ip_monitored")

        is_external_device_monitored = d.pop("is_external_device_monitored")

        monitoring_host_enabled = d.pop("monitoring_host_enabled")

        def _parse_monitoring_type(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        monitoring_type = _parse_monitoring_type(d.pop("monitoring_type"))

        def _parse_probe_limit(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        probe_limit = _parse_probe_limit(d.pop("probe_limit"))

        def _parse_severity_level(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        severity_level = _parse_severity_level(d.pop("severity_level"))

        def _parse_email_notification(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        email_notification = _parse_email_notification(d.pop("email_notification"))

        def _parse_sms_notification(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        sms_notification = _parse_sms_notification(d.pop("sms_notification"))

        server_monitoring = cls(
            server_monitoring_id=server_monitoring_id,
            purchase_monitoring_id=purchase_monitoring_id,
            purchase_server_id=purchase_server_id,
            service_name=service_name,
            purchase_name=purchase_name,
            purchase_status_code=purchase_status_code,
            monitoring_key=monitoring_key,
            is_server_monitored=is_server_monitored,
            is_ip_monitored=is_ip_monitored,
            is_external_device_monitored=is_external_device_monitored,
            monitoring_host_enabled=monitoring_host_enabled,
            monitoring_type=monitoring_type,
            probe_limit=probe_limit,
            severity_level=severity_level,
            email_notification=email_notification,
            sms_notification=sms_notification,
        )

        server_monitoring.additional_properties = d
        return server_monitoring

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
