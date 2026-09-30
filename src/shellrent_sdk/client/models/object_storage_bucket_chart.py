from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.object_storage_bucket_chart_points_item import ObjectStorageBucketChartPointsItem


T = TypeVar("T", bound="ObjectStorageBucketChart")


@_attrs_define
class ObjectStorageBucketChart:
    object_storage_id: int
    bucket_id: int
    interval: str
    points: list[ObjectStorageBucketChartPointsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_storage_id = self.object_storage_id

        bucket_id = self.bucket_id

        interval = self.interval

        points = []
        for points_item_data in self.points:
            points_item = points_item_data.to_dict()
            points.append(points_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "object_storage_id": object_storage_id,
                "bucket_id": bucket_id,
                "interval": interval,
                "points": points,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.object_storage_bucket_chart_points_item import (
            ObjectStorageBucketChartPointsItem,
        )

        d = dict(src_dict)
        object_storage_id = d.pop("object_storage_id")

        bucket_id = d.pop("bucket_id")

        interval = d.pop("interval")

        points = []
        _points = d.pop("points")
        for points_item_data in _points:
            points_item = ObjectStorageBucketChartPointsItem.from_dict(points_item_data)

            points.append(points_item)

        object_storage_bucket_chart = cls(
            object_storage_id=object_storage_id,
            bucket_id=bucket_id,
            interval=interval,
            points=points,
        )

        object_storage_bucket_chart.additional_properties = d
        return object_storage_bucket_chart

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
