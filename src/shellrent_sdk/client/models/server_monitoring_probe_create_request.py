from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.server_monitoring_probe_create_request_parameters import (
        ServerMonitoringProbeCreateRequestParameters,
    )


T = TypeVar("T", bound="ServerMonitoringProbeCreateRequest")


@_attrs_define
class ServerMonitoringProbeCreateRequest:
    server_monitoring_item_template_id: int
    """ Probe template identifier. """
    parameters: ServerMonitoringProbeCreateRequestParameters | Unset = UNSET
    """ Template probe parameters as key-value map. """
    notification_email: str | Unset = UNSET
    """ Notification email for this probe. """
    notification_sms: str | Unset = UNSET
    """ Notification phone number for this probe. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        server_monitoring_item_template_id = self.server_monitoring_item_template_id

        parameters: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = self.parameters.to_dict()

        notification_email = self.notification_email

        notification_sms = self.notification_sms

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "server_monitoring_item_template_id": server_monitoring_item_template_id,
            }
        )
        if parameters is not UNSET:
            field_dict["parameters"] = parameters
        if notification_email is not UNSET:
            field_dict["notification_email"] = notification_email
        if notification_sms is not UNSET:
            field_dict["notification_sms"] = notification_sms

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.server_monitoring_probe_create_request_parameters import (
            ServerMonitoringProbeCreateRequestParameters,
        )

        d = dict(src_dict)
        server_monitoring_item_template_id = d.pop("server_monitoring_item_template_id")

        _parameters = d.pop("parameters", UNSET)
        parameters: ServerMonitoringProbeCreateRequestParameters | Unset
        if isinstance(_parameters, Unset):
            parameters = UNSET
        else:
            parameters = ServerMonitoringProbeCreateRequestParameters.from_dict(_parameters)

        notification_email = d.pop("notification_email", UNSET)

        notification_sms = d.pop("notification_sms", UNSET)

        server_monitoring_probe_create_request = cls(
            server_monitoring_item_template_id=server_monitoring_item_template_id,
            parameters=parameters,
            notification_email=notification_email,
            notification_sms=notification_sms,
        )

        server_monitoring_probe_create_request.additional_properties = d
        return server_monitoring_probe_create_request

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
