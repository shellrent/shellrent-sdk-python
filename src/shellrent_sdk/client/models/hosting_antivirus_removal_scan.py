from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="HostingAntivirusRemovalScan")


@_attrs_define
class HostingAntivirusRemovalScan:
    removal_scan_id: int
    hosting_id: int
    task_id: int | None
    status: bool | None
    error: None | str
    date_created: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        removal_scan_id = self.removal_scan_id

        hosting_id = self.hosting_id

        task_id: int | None
        task_id = self.task_id

        status: bool | None
        status = self.status

        error: None | str
        error = self.error

        date_created = self.date_created.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "removal_scan_id": removal_scan_id,
                "hosting_id": hosting_id,
                "task_id": task_id,
                "status": status,
                "error": error,
                "date_created": date_created,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        removal_scan_id = d.pop("removal_scan_id")

        hosting_id = d.pop("hosting_id")

        def _parse_task_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        task_id = _parse_task_id(d.pop("task_id"))

        def _parse_status(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        status = _parse_status(d.pop("status"))

        def _parse_error(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        error = _parse_error(d.pop("error"))

        date_created = datetime.datetime.fromisoformat(d.pop("date_created"))

        hosting_antivirus_removal_scan = cls(
            removal_scan_id=removal_scan_id,
            hosting_id=hosting_id,
            task_id=task_id,
            status=status,
            error=error,
            date_created=date_created,
        )

        hosting_antivirus_removal_scan.additional_properties = d
        return hosting_antivirus_removal_scan

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
