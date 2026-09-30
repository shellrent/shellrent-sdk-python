from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="HostingAntivirus")


@_attrs_define
class HostingAntivirus:
    antivirus_id: int
    hosting_id: int
    status_code: None | str
    status_name: None | str
    status_color: None | str
    antivirus_type: str
    date_started: datetime.datetime | None
    date_completed: datetime.datetime | None
    date_timeout: datetime.datetime | None
    total_files: int | None
    total_infected: int | None
    total_cleaned: int | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        antivirus_id = self.antivirus_id

        hosting_id = self.hosting_id

        status_code: None | str
        status_code = self.status_code

        status_name: None | str
        status_name = self.status_name

        status_color: None | str
        status_color = self.status_color

        antivirus_type = self.antivirus_type

        date_started: None | str
        if isinstance(self.date_started, datetime.datetime):
            date_started = self.date_started.isoformat()
        else:
            date_started = self.date_started

        date_completed: None | str
        if isinstance(self.date_completed, datetime.datetime):
            date_completed = self.date_completed.isoformat()
        else:
            date_completed = self.date_completed

        date_timeout: None | str
        if isinstance(self.date_timeout, datetime.datetime):
            date_timeout = self.date_timeout.isoformat()
        else:
            date_timeout = self.date_timeout

        total_files: int | None
        total_files = self.total_files

        total_infected: int | None
        total_infected = self.total_infected

        total_cleaned: int | None
        total_cleaned = self.total_cleaned

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "antivirus_id": antivirus_id,
                "hosting_id": hosting_id,
                "status_code": status_code,
                "status_name": status_name,
                "status_color": status_color,
                "antivirus_type": antivirus_type,
                "date_started": date_started,
                "date_completed": date_completed,
                "date_timeout": date_timeout,
                "total_files": total_files,
                "total_infected": total_infected,
                "total_cleaned": total_cleaned,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        antivirus_id = d.pop("antivirus_id")

        hosting_id = d.pop("hosting_id")

        def _parse_status_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        status_code = _parse_status_code(d.pop("status_code"))

        def _parse_status_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        status_name = _parse_status_name(d.pop("status_name"))

        def _parse_status_color(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        status_color = _parse_status_color(d.pop("status_color"))

        antivirus_type = d.pop("antivirus_type")

        def _parse_date_started(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_started_type_0 = datetime.datetime.fromisoformat(data)

                return date_started_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        date_started = _parse_date_started(d.pop("date_started"))

        def _parse_date_completed(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_completed_type_0 = datetime.datetime.fromisoformat(data)

                return date_completed_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        date_completed = _parse_date_completed(d.pop("date_completed"))

        def _parse_date_timeout(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_timeout_type_0 = datetime.datetime.fromisoformat(data)

                return date_timeout_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        date_timeout = _parse_date_timeout(d.pop("date_timeout"))

        def _parse_total_files(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        total_files = _parse_total_files(d.pop("total_files"))

        def _parse_total_infected(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        total_infected = _parse_total_infected(d.pop("total_infected"))

        def _parse_total_cleaned(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        total_cleaned = _parse_total_cleaned(d.pop("total_cleaned"))

        hosting_antivirus = cls(
            antivirus_id=antivirus_id,
            hosting_id=hosting_id,
            status_code=status_code,
            status_name=status_name,
            status_color=status_color,
            antivirus_type=antivirus_type,
            date_started=date_started,
            date_completed=date_completed,
            date_timeout=date_timeout,
            total_files=total_files,
            total_infected=total_infected,
            total_cleaned=total_cleaned,
        )

        hosting_antivirus.additional_properties = d
        return hosting_antivirus

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
