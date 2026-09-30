from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="HostingCronjob")


@_attrs_define
class HostingCronjob:
    cronjob_id: int
    hosting_id: int
    purchase_id: int
    request_url: str
    http_request_method: None | str
    plan_month: None | str
    plan_monthday: None | str
    plan_weekday: None | str
    plan_hour: None | str
    plan_minute: None | str
    active: bool
    date_created: datetime.datetime | None
    date_disabled: datetime.datetime | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cronjob_id = self.cronjob_id

        hosting_id = self.hosting_id

        purchase_id = self.purchase_id

        request_url = self.request_url

        http_request_method: None | str
        http_request_method = self.http_request_method

        plan_month: None | str
        plan_month = self.plan_month

        plan_monthday: None | str
        plan_monthday = self.plan_monthday

        plan_weekday: None | str
        plan_weekday = self.plan_weekday

        plan_hour: None | str
        plan_hour = self.plan_hour

        plan_minute: None | str
        plan_minute = self.plan_minute

        active = self.active

        date_created: None | str
        if isinstance(self.date_created, datetime.datetime):
            date_created = self.date_created.isoformat()
        else:
            date_created = self.date_created

        date_disabled: None | str
        if isinstance(self.date_disabled, datetime.datetime):
            date_disabled = self.date_disabled.isoformat()
        else:
            date_disabled = self.date_disabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cronjob_id": cronjob_id,
                "hosting_id": hosting_id,
                "purchase_id": purchase_id,
                "request_url": request_url,
                "http_request_method": http_request_method,
                "plan_month": plan_month,
                "plan_monthday": plan_monthday,
                "plan_weekday": plan_weekday,
                "plan_hour": plan_hour,
                "plan_minute": plan_minute,
                "active": active,
                "date_created": date_created,
                "date_disabled": date_disabled,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        cronjob_id = d.pop("cronjob_id")

        hosting_id = d.pop("hosting_id")

        purchase_id = d.pop("purchase_id")

        request_url = d.pop("request_url")

        def _parse_http_request_method(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        http_request_method = _parse_http_request_method(d.pop("http_request_method"))

        def _parse_plan_month(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        plan_month = _parse_plan_month(d.pop("plan_month"))

        def _parse_plan_monthday(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        plan_monthday = _parse_plan_monthday(d.pop("plan_monthday"))

        def _parse_plan_weekday(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        plan_weekday = _parse_plan_weekday(d.pop("plan_weekday"))

        def _parse_plan_hour(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        plan_hour = _parse_plan_hour(d.pop("plan_hour"))

        def _parse_plan_minute(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        plan_minute = _parse_plan_minute(d.pop("plan_minute"))

        active = d.pop("active")

        def _parse_date_created(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_created_type_0 = datetime.datetime.fromisoformat(data)

                return date_created_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        date_created = _parse_date_created(d.pop("date_created"))

        def _parse_date_disabled(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_disabled_type_0 = datetime.datetime.fromisoformat(data)

                return date_disabled_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        date_disabled = _parse_date_disabled(d.pop("date_disabled"))

        hosting_cronjob = cls(
            cronjob_id=cronjob_id,
            hosting_id=hosting_id,
            purchase_id=purchase_id,
            request_url=request_url,
            http_request_method=http_request_method,
            plan_month=plan_month,
            plan_monthday=plan_monthday,
            plan_weekday=plan_weekday,
            plan_hour=plan_hour,
            plan_minute=plan_minute,
            active=active,
            date_created=date_created,
            date_disabled=date_disabled,
        )

        hosting_cronjob.additional_properties = d
        return hosting_cronjob

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
