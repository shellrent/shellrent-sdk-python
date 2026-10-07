from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ObjectStorageBucketChartPointsItem")


@_attrs_define
class ObjectStorageBucketChartPointsItem:
    x: float
    """ UNIX timestamp in milliseconds """
    active_storage_bytes: int
    """ Space used by the active objects on the day, in bytes """
    deleted_storage_bytes: int
    """ Space of the deleted objects still counted on the day, in bytes """
    active_objects: int
    """ Number of active objects on the day """
    deleted_objects: int
    """ Number of deleted objects still counted on the day """
    api_calls_count: int
    """ Number of API calls on the day """
    storage_wrote_bytes: int
    storage_read_bytes: int
    ingress_traffic_bytes: int
    egress_traffic_bytes: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        x = self.x

        active_storage_bytes = self.active_storage_bytes

        deleted_storage_bytes = self.deleted_storage_bytes

        active_objects = self.active_objects

        deleted_objects = self.deleted_objects

        api_calls_count = self.api_calls_count

        storage_wrote_bytes = self.storage_wrote_bytes

        storage_read_bytes = self.storage_read_bytes

        ingress_traffic_bytes = self.ingress_traffic_bytes

        egress_traffic_bytes = self.egress_traffic_bytes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "x": x,
                "active_storage_bytes": active_storage_bytes,
                "deleted_storage_bytes": deleted_storage_bytes,
                "active_objects": active_objects,
                "deleted_objects": deleted_objects,
                "api_calls_count": api_calls_count,
                "storage_wrote_bytes": storage_wrote_bytes,
                "storage_read_bytes": storage_read_bytes,
                "ingress_traffic_bytes": ingress_traffic_bytes,
                "egress_traffic_bytes": egress_traffic_bytes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        x = d.pop("x")

        active_storage_bytes = d.pop("active_storage_bytes")

        deleted_storage_bytes = d.pop("deleted_storage_bytes")

        active_objects = d.pop("active_objects")

        deleted_objects = d.pop("deleted_objects")

        api_calls_count = d.pop("api_calls_count")

        storage_wrote_bytes = d.pop("storage_wrote_bytes")

        storage_read_bytes = d.pop("storage_read_bytes")

        ingress_traffic_bytes = d.pop("ingress_traffic_bytes")

        egress_traffic_bytes = d.pop("egress_traffic_bytes")

        object_storage_bucket_chart_points_item = cls(
            x=x,
            active_storage_bytes=active_storage_bytes,
            deleted_storage_bytes=deleted_storage_bytes,
            active_objects=active_objects,
            deleted_objects=deleted_objects,
            api_calls_count=api_calls_count,
            storage_wrote_bytes=storage_wrote_bytes,
            storage_read_bytes=storage_read_bytes,
            ingress_traffic_bytes=ingress_traffic_bytes,
            egress_traffic_bytes=egress_traffic_bytes,
        )

        object_storage_bucket_chart_points_item.additional_properties = d
        return object_storage_bucket_chart_points_item

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
