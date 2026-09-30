from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.web_monitoring_response_time_chart_points_item import (
        WebMonitoringResponseTimeChartPointsItem,
    )


T = TypeVar("T", bound="WebMonitoringResponseTimeChart")


@_attrs_define
class WebMonitoringResponseTimeChart:
    web_monitoring_id: int
    interval: str
    unit: str
    points: list[WebMonitoringResponseTimeChartPointsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        web_monitoring_id = self.web_monitoring_id

        interval = self.interval

        unit = self.unit

        points = []
        for points_item_data in self.points:
            points_item = points_item_data.to_dict()
            points.append(points_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "web_monitoring_id": web_monitoring_id,
                "interval": interval,
                "unit": unit,
                "points": points,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.web_monitoring_response_time_chart_points_item import (
            WebMonitoringResponseTimeChartPointsItem,
        )

        d = dict(src_dict)
        web_monitoring_id = d.pop("web_monitoring_id")

        interval = d.pop("interval")

        unit = d.pop("unit")

        points = []
        _points = d.pop("points")
        for points_item_data in _points:
            points_item = WebMonitoringResponseTimeChartPointsItem.from_dict(points_item_data)

            points.append(points_item)

        web_monitoring_response_time_chart = cls(
            web_monitoring_id=web_monitoring_id,
            interval=interval,
            unit=unit,
            points=points,
        )

        web_monitoring_response_time_chart.additional_properties = d
        return web_monitoring_response_time_chart

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
