from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ServerMonitoring")


@_attrs_define
class ServerMonitoring:
    """Server monitoring service of the account, with the host it checks and its settings"""

    server_monitoring_id: int
    purchase_monitoring_id: int | None
    """ Id of the purchase of the monitoring service (`GET /api/v3/purchases/{purchase_id}`) """
    purchase_server_id: int | None
    """ Id of the purchase of the monitored server (`GET /api/v3/purchases/{purchase_id}`); null when the monitoring
    checks a hostname or an IP address """
    service_name: None | str
    """ Name of the service of the monitoring purchase """
    purchase_name: None | str
    """ Name of the object of the monitoring purchase, usually the monitored hostname or IP address """
    purchase_status_code: None | str
    """ Status code of the monitoring purchase, for example `ACTIVE_V2` or `NEW_V2` (not active yet) """
    monitoring_key: None | str
    """ Host checked by the monitoring: the hostname of the monitored server, or the hostname or IP address given
    """
    is_server_monitored: bool
    """ Whether the monitoring checks a server, given by its purchase (`purchase_server_id`) or by its hostname """
    is_ip_monitored: bool
    """ Whether the monitoring checks an IP address """
    is_external_device_monitored: bool
    """ Whether the monitoring checks an external device, given by hostname or IP address instead of a server or an
    IP address of the account """
    monitoring_host_enabled: bool
    """ Whether the monitoring of the host is enabled """
    monitoring_type: None | str
    """ Type of the monitoring: `default` (Base) or `plus` (Managed), which can also run the automatic actions of
    the probes """
    probe_limit: int | None
    """ Maximum number of probes of the monitoring, counting the probes with `advanced_item` """
    severity_level: None | str
    """ Severity of the problems detected by the probes: `default`, `high` or `disaster` """
    email_notification: None | str
    """ Default email address for the notifications of the probes; each probe has its own (`notification_email`) """
    sms_notification: None | str
    """ Default phone number for the SMS notifications of the probes; each probe has its own (`notification_sms`)
    """
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
