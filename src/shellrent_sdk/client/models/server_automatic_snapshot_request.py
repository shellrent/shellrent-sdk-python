from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="ServerAutomaticSnapshotRequest")


@_attrs_define
class ServerAutomaticSnapshotRequest:
    """Schedule of the automatic snapshots of a server"""

    name: str
    """ Name of the snapshots: only letters, numbers, spaces, underscores and dashes """
    day_of_week: list[int]
    """ Days of week (1-7, where 1 is Monday) """
    hour_of_day: str
    """ Time of the snapshot, in 24-hour HH:MM format. Times after 01:00 and before 04:59 are not allowed """

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        day_of_week = self.day_of_week

        hour_of_day = self.hour_of_day

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "day_of_week": day_of_week,
                "hour_of_day": hour_of_day,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name")

        day_of_week = cast(list[int], d.pop("day_of_week"))

        hour_of_day = d.pop("hour_of_day")

        server_automatic_snapshot_request = cls(
            name=name,
            day_of_week=day_of_week,
            hour_of_day=hour_of_day,
        )

        return server_automatic_snapshot_request
