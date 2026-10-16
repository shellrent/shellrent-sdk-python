from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="WebMonitoringResponseTimeChartPointsItem")


@_attrs_define
class WebMonitoringResponseTimeChartPointsItem:
    x: float
    """ UNIX timestamp in milliseconds """
    y: float
    """ Response time value in milliseconds """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        x = self.x

        y = self.y

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "x": x,
                "y": y,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        x = d.pop("x")

        y = d.pop("y")

        web_monitoring_response_time_chart_points_item = cls(
            x=x,
            y=y,
        )

        web_monitoring_response_time_chart_points_item.additional_properties = d
        return web_monitoring_response_time_chart_points_item

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
