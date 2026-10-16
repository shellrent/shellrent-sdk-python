from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..models.hosting_cronjob_create_request_http_request_method import (
    HostingCronjobCreateRequestHttpRequestMethod,
)
from ..models.hosting_cronjob_create_request_request_protocol import (
    HostingCronjobCreateRequestRequestProtocol,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="HostingCronjobCreateRequest")


@_attrs_define
class HostingCronjobCreateRequest:
    request_protocol: HostingCronjobCreateRequestRequestProtocol
    """ http or https """
    request_url: str
    """ URL to call, without protocol (e.g. `www.example.com/cron.php`): a leading http:// or https:// is removed
    and request_protocol is used """
    http_request_method: HostingCronjobCreateRequestHttpRequestMethod | Unset = (
        HostingCronjobCreateRequestHttpRequestMethod.GET
    )
    """ HTTP method of the call """
    plan_month: None | str | Unset = UNSET
    """ Month in which the cronjob runs, from 1 (January) to 12 (December). Omit it, or send null or an empty
    string, to run it every month """
    plan_monthday: None | str | Unset = UNSET
    """ Days of the month, as a comma-separated list of values from 1 to 31 (e.g. `1,15`). Omit it, or send null or
    an empty string, to run it every day """
    plan_weekday: None | str | Unset = UNSET
    """ Day of the week, from 1 (Monday) to 7 (Sunday). Omit it, or send null or an empty string, to run it every
    day of the week """
    plan_hour: None | str | Unset = UNSET
    """ Hours, as a comma-separated list of values from 0 to 23 (e.g. `0,12`). Omit it, or send null or an empty
    string, to run it every hour """
    plan_minute: None | str | Unset = UNSET
    """ Minutes, as a comma-separated list of values from 0 to 59 (e.g. `0,30`). Omit it, or send null or an empty
    string, to run it every minute """

    def to_dict(self) -> dict[str, Any]:
        request_protocol = self.request_protocol.value

        request_url = self.request_url

        http_request_method: str | Unset = UNSET
        if not isinstance(self.http_request_method, Unset):
            http_request_method = self.http_request_method.value

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

        field_dict.update(
            {
                "request_protocol": request_protocol,
                "request_url": request_url,
            }
        )
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
        request_protocol = HostingCronjobCreateRequestRequestProtocol(d.pop("request_protocol"))

        request_url = d.pop("request_url")

        _http_request_method = d.pop("http_request_method", UNSET)
        http_request_method: HostingCronjobCreateRequestHttpRequestMethod | Unset
        if isinstance(_http_request_method, Unset):
            http_request_method = UNSET
        else:
            http_request_method = HostingCronjobCreateRequestHttpRequestMethod(_http_request_method)

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

        return hosting_cronjob_create_request
