from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ServerAutomaticSnapshotRequest")


@_attrs_define
class ServerAutomaticSnapshotRequest:
    name: str
    day_of_week: list[int]
    """ Days of week (1-7, where 1 is Monday) """
    hour_of_day: str
    """ Time in HH:MM """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        day_of_week = self.day_of_week

        hour_of_day = self.hour_of_day

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
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

        server_automatic_snapshot_request.additional_properties = d
        return server_automatic_snapshot_request

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
