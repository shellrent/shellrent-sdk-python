from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="WebMonitoring")


@_attrs_define
class WebMonitoring:
    web_monitoring_id: int
    purchase_id: int | None
    service_name: None | str
    purchase_name: None | str
    purchase_status_code: None | str
    monitored_domain: None | str
    host_ref: None | str
    web_scenario_ref: None | str
    status: None | str
    email_notification: None | str
    sms_notification: None | str
    ips: None | str
    ip_isp: None | str
    ip_location: None | str
    last_http_response: int | None
    last_down_date: datetime.datetime | None
    send_ssl_notify: bool
    active: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        web_monitoring_id = self.web_monitoring_id

        purchase_id: int | None
        purchase_id = self.purchase_id

        service_name: None | str
        service_name = self.service_name

        purchase_name: None | str
        purchase_name = self.purchase_name

        purchase_status_code: None | str
        purchase_status_code = self.purchase_status_code

        monitored_domain: None | str
        monitored_domain = self.monitored_domain

        host_ref: None | str
        host_ref = self.host_ref

        web_scenario_ref: None | str
        web_scenario_ref = self.web_scenario_ref

        status: None | str
        status = self.status

        email_notification: None | str
        email_notification = self.email_notification

        sms_notification: None | str
        sms_notification = self.sms_notification

        ips: None | str
        ips = self.ips

        ip_isp: None | str
        ip_isp = self.ip_isp

        ip_location: None | str
        ip_location = self.ip_location

        last_http_response: int | None
        last_http_response = self.last_http_response

        last_down_date: None | str
        if isinstance(self.last_down_date, datetime.datetime):
            last_down_date = self.last_down_date.isoformat()
        else:
            last_down_date = self.last_down_date

        send_ssl_notify = self.send_ssl_notify

        active = self.active

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "web_monitoring_id": web_monitoring_id,
                "purchase_id": purchase_id,
                "service_name": service_name,
                "purchase_name": purchase_name,
                "purchase_status_code": purchase_status_code,
                "monitored_domain": monitored_domain,
                "host_ref": host_ref,
                "web_scenario_ref": web_scenario_ref,
                "status": status,
                "email_notification": email_notification,
                "sms_notification": sms_notification,
                "ips": ips,
                "ip_isp": ip_isp,
                "ip_location": ip_location,
                "last_http_response": last_http_response,
                "last_down_date": last_down_date,
                "send_ssl_notify": send_ssl_notify,
                "active": active,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        web_monitoring_id = d.pop("web_monitoring_id")

        def _parse_purchase_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        purchase_id = _parse_purchase_id(d.pop("purchase_id"))

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

        def _parse_monitored_domain(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        monitored_domain = _parse_monitored_domain(d.pop("monitored_domain"))

        def _parse_host_ref(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        host_ref = _parse_host_ref(d.pop("host_ref"))

        def _parse_web_scenario_ref(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        web_scenario_ref = _parse_web_scenario_ref(d.pop("web_scenario_ref"))

        def _parse_status(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        status = _parse_status(d.pop("status"))

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

        def _parse_ips(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        ips = _parse_ips(d.pop("ips"))

        def _parse_ip_isp(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        ip_isp = _parse_ip_isp(d.pop("ip_isp"))

        def _parse_ip_location(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        ip_location = _parse_ip_location(d.pop("ip_location"))

        def _parse_last_http_response(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        last_http_response = _parse_last_http_response(d.pop("last_http_response"))

        def _parse_last_down_date(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_down_date_type_0 = datetime.datetime.fromisoformat(data)

                return last_down_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_down_date = _parse_last_down_date(d.pop("last_down_date"))

        send_ssl_notify = d.pop("send_ssl_notify")

        active = d.pop("active")

        web_monitoring = cls(
            web_monitoring_id=web_monitoring_id,
            purchase_id=purchase_id,
            service_name=service_name,
            purchase_name=purchase_name,
            purchase_status_code=purchase_status_code,
            monitored_domain=monitored_domain,
            host_ref=host_ref,
            web_scenario_ref=web_scenario_ref,
            status=status,
            email_notification=email_notification,
            sms_notification=sms_notification,
            ips=ips,
            ip_isp=ip_isp,
            ip_location=ip_location,
            last_http_response=last_http_response,
            last_down_date=last_down_date,
            send_ssl_notify=send_ssl_notify,
            active=active,
        )

        web_monitoring.additional_properties = d
        return web_monitoring

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
