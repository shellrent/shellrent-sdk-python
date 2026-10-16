from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ServerAutomaticSnapshot")


@_attrs_define
class ServerAutomaticSnapshot:
    """Schedule of the automatic snapshots of a server"""

    snapshot_id: int
    """ Id of the schedule (not of a snapshot) """
    server_id: int
    """ Id of the server (`GET /api/v3/servers/{server_id}`) """
    name: str
    """ Name of the snapshots that the schedule creates """
    days_of_week: list[int]
    """ Days of the week of the snapshots, from 1 (Monday) to 7 (Sunday) """
    hour_of_day: str
    """ Time of the snapshots, in 24-hour `HH:MM` format """
    is_active: bool
    """ Whether the schedule is active """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        snapshot_id = self.snapshot_id

        server_id = self.server_id

        name = self.name

        days_of_week = self.days_of_week

        hour_of_day = self.hour_of_day

        is_active = self.is_active

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "snapshot_id": snapshot_id,
                "server_id": server_id,
                "name": name,
                "days_of_week": days_of_week,
                "hour_of_day": hour_of_day,
                "is_active": is_active,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        snapshot_id = d.pop("snapshot_id")

        server_id = d.pop("server_id")

        name = d.pop("name")

        days_of_week = cast(list[int], d.pop("days_of_week"))

        hour_of_day = d.pop("hour_of_day")

        is_active = d.pop("is_active")

        server_automatic_snapshot = cls(
            snapshot_id=snapshot_id,
            server_id=server_id,
            name=name,
            days_of_week=days_of_week,
            hour_of_day=hour_of_day,
            is_active=is_active,
        )

        server_automatic_snapshot.additional_properties = d
        return server_automatic_snapshot

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
