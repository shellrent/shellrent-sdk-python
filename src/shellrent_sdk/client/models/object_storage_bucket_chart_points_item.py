from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ObjectStorageBucketChartPointsItem")


@_attrs_define
class ObjectStorageBucketChartPointsItem:
    x: float | Unset = UNSET
    """ UNIX timestamp in milliseconds """
    active_storage_bytes: int | Unset = UNSET
    deleted_storage_bytes: int | Unset = UNSET
    active_objects: int | Unset = UNSET
    deleted_objects: int | Unset = UNSET
    api_calls_count: int | Unset = UNSET
    storage_wrote_bytes: int | Unset = UNSET
    storage_read_bytes: int | Unset = UNSET
    ingress_traffic_bytes: int | Unset = UNSET
    egress_traffic_bytes: int | Unset = UNSET
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
        field_dict.update({})
        if x is not UNSET:
            field_dict["x"] = x
        if active_storage_bytes is not UNSET:
            field_dict["active_storage_bytes"] = active_storage_bytes
        if deleted_storage_bytes is not UNSET:
            field_dict["deleted_storage_bytes"] = deleted_storage_bytes
        if active_objects is not UNSET:
            field_dict["active_objects"] = active_objects
        if deleted_objects is not UNSET:
            field_dict["deleted_objects"] = deleted_objects
        if api_calls_count is not UNSET:
            field_dict["api_calls_count"] = api_calls_count
        if storage_wrote_bytes is not UNSET:
            field_dict["storage_wrote_bytes"] = storage_wrote_bytes
        if storage_read_bytes is not UNSET:
            field_dict["storage_read_bytes"] = storage_read_bytes
        if ingress_traffic_bytes is not UNSET:
            field_dict["ingress_traffic_bytes"] = ingress_traffic_bytes
        if egress_traffic_bytes is not UNSET:
            field_dict["egress_traffic_bytes"] = egress_traffic_bytes

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        x = d.pop("x", UNSET)

        active_storage_bytes = d.pop("active_storage_bytes", UNSET)

        deleted_storage_bytes = d.pop("deleted_storage_bytes", UNSET)

        active_objects = d.pop("active_objects", UNSET)

        deleted_objects = d.pop("deleted_objects", UNSET)

        api_calls_count = d.pop("api_calls_count", UNSET)

        storage_wrote_bytes = d.pop("storage_wrote_bytes", UNSET)

        storage_read_bytes = d.pop("storage_read_bytes", UNSET)

        ingress_traffic_bytes = d.pop("ingress_traffic_bytes", UNSET)

        egress_traffic_bytes = d.pop("egress_traffic_bytes", UNSET)

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
