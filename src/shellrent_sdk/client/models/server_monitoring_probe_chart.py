from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.server_monitoring_probe_chart_points_item import (
        ServerMonitoringProbeChartPointsItem,
    )


T = TypeVar("T", bound="ServerMonitoringProbeChart")


@_attrs_define
class ServerMonitoringProbeChart:
    server_monitoring_id: int
    probe_id: int
    interval: str
    points: list[ServerMonitoringProbeChartPointsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        server_monitoring_id = self.server_monitoring_id

        probe_id = self.probe_id

        interval = self.interval

        points = []
        for points_item_data in self.points:
            points_item = points_item_data.to_dict()
            points.append(points_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "server_monitoring_id": server_monitoring_id,
                "probe_id": probe_id,
                "interval": interval,
                "points": points,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.server_monitoring_probe_chart_points_item import (
            ServerMonitoringProbeChartPointsItem,
        )

        d = dict(src_dict)
        server_monitoring_id = d.pop("server_monitoring_id")

        probe_id = d.pop("probe_id")

        interval = d.pop("interval")

        points = []
        _points = d.pop("points")
        for points_item_data in _points:
            points_item = ServerMonitoringProbeChartPointsItem.from_dict(points_item_data)

            points.append(points_item)

        server_monitoring_probe_chart = cls(
            server_monitoring_id=server_monitoring_id,
            probe_id=probe_id,
            interval=interval,
            points=points,
        )

        server_monitoring_probe_chart.additional_properties = d
        return server_monitoring_probe_chart

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
