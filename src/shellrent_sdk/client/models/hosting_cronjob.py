from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="HostingCronjob")


@_attrs_define
class HostingCronjob:
    """Cron job of the hosting: a URL called on a schedule"""

    cronjob_id: int
    hosting_id: int
    """ Id of the hosting of the request: cron jobs belong to the purchase, so a subdomain lists those of its main
    hosting """
    purchase_id: int
    """ Id of the purchase of the hosting (`GET /api/v3/purchases/{purchase_id}`) """
    request_url: str
    """ URL called by the cron job, with the protocol """
    http_request_method: None | str
    """ HTTP method of the call: `GET` or `POST` """
    plan_month: None | str
    """ Months, from 1 (January) to 12 (December), as a comma-separated list like in the creation (for example
    `1,6`); null for every month """
    plan_monthday: None | str
    """ Days of the month, from 1 to 31, as a comma-separated list like in the creation (for example `1,15`); null
    for every day """
    plan_weekday: None | str
    """ Days of the week, from 1 (Monday) to 7 (Sunday), as a comma-separated list like in the creation (for example
    `1,5`); null for every day of the week """
    plan_hour: None | str
    """ Hours, from 0 to 23, as a comma-separated list like in the creation (for example `0,12`); null for every
    hour """
    plan_minute: None | str
    """ Minutes, from 0 to 59, as a comma-separated list like in the creation (for example `0,30`); null for every
    minute """
    active: bool
    """ Whether the cron job is active: deleted cron jobs, and the old versions of changed ones, stay in the list as
    inactive """
    date_created: datetime.datetime | None
    date_disabled: datetime.datetime | None
    """ When the cron job was deleted or replaced by a new version; null while it is active """
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
