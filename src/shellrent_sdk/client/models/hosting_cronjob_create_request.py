from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HostingCronjobCreateRequest")


@_attrs_define
class HostingCronjobCreateRequest:
    request_protocol: str | Unset = UNSET
    """ http or https """
    request_url: str | Unset = UNSET
    """ URL without protocol """
    http_request_method: str | Unset = "GET"
    plan_month: None | str | Unset = UNSET
    plan_monthday: None | str | Unset = UNSET
    plan_weekday: None | str | Unset = UNSET
    plan_hour: None | str | Unset = UNSET
    plan_minute: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        request_protocol = self.request_protocol

        request_url = self.request_url

        http_request_method = self.http_request_method

        plan_month: None | str | Unset
        if isinstance(self.plan_month, Unset):
            plan_month = UNSET
        else:
            plan_month = self.plan_month

        plan_monthday: None | str | Unset
        if isinstance(self.plan_monthday, Unset):
            plan_monthday = UNSET
        else:
            plan_monthday = self.plan_monthday

        plan_weekday: None | str | Unset
        if isinstance(self.plan_weekday, Unset):
            plan_weekday = UNSET
        else:
            plan_weekday = self.plan_weekday

        plan_hour: None | str | Unset
        if isinstance(self.plan_hour, Unset):
            plan_hour = UNSET
        else:
            plan_hour = self.plan_hour

        plan_minute: None | str | Unset
        if isinstance(self.plan_minute, Unset):
            plan_minute = UNSET
        else:
            plan_minute = self.plan_minute

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if request_protocol is not UNSET:
            field_dict["request_protocol"] = request_protocol
        if request_url is not UNSET:
            field_dict["request_url"] = request_url
        if http_request_method is not UNSET:
            field_dict["http_request_method"] = http_request_method
        if plan_month is not UNSET:
            field_dict["plan_month"] = plan_month
        if plan_monthday is not UNSET:
            field_dict["plan_monthday"] = plan_monthday
        if plan_weekday is not UNSET:
            field_dict["plan_weekday"] = plan_weekday
        if plan_hour is not UNSET:
            field_dict["plan_hour"] = plan_hour
        if plan_minute is not UNSET:
            field_dict["plan_minute"] = plan_minute

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        request_protocol = d.pop("request_protocol", UNSET)

        request_url = d.pop("request_url", UNSET)

        http_request_method = d.pop("http_request_method", UNSET)

        def _parse_plan_month(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        plan_month = _parse_plan_month(d.pop("plan_month", UNSET))

        def _parse_plan_monthday(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        plan_monthday = _parse_plan_monthday(d.pop("plan_monthday", UNSET))

        def _parse_plan_weekday(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        plan_weekday = _parse_plan_weekday(d.pop("plan_weekday", UNSET))

        def _parse_plan_hour(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        plan_hour = _parse_plan_hour(d.pop("plan_hour", UNSET))

        def _parse_plan_minute(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        plan_minute = _parse_plan_minute(d.pop("plan_minute", UNSET))

        hosting_cronjob_create_request = cls(
            request_protocol=request_protocol,
            request_url=request_url,
            http_request_method=http_request_method,
            plan_month=plan_month,
            plan_monthday=plan_monthday,
            plan_weekday=plan_weekday,
            plan_hour=plan_hour,
            plan_minute=plan_minute,
        )

        hosting_cronjob_create_request.additional_properties = d
        return hosting_cronjob_create_request

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
