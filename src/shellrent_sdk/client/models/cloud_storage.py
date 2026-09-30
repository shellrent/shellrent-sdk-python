from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CloudStorage")


@_attrs_define
class CloudStorage:
    cloud_storage_id: int
    purchase_id: int | None
    name: None | str
    read_write_host: None | str
    read_only_host: None | str
    app_host: None | str
    group_disk_used_bytes: int | None
    date_sync: datetime.datetime | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cloud_storage_id = self.cloud_storage_id

        purchase_id: int | None
        purchase_id = self.purchase_id

        name: None | str
        name = self.name

        read_write_host: None | str
        read_write_host = self.read_write_host

        read_only_host: None | str
        read_only_host = self.read_only_host

        app_host: None | str
        app_host = self.app_host

        group_disk_used_bytes: int | None
        group_disk_used_bytes = self.group_disk_used_bytes

        date_sync: None | str
        if isinstance(self.date_sync, datetime.datetime):
            date_sync = self.date_sync.isoformat()
        else:
            date_sync = self.date_sync

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cloud_storage_id": cloud_storage_id,
                "purchase_id": purchase_id,
                "name": name,
                "read_write_host": read_write_host,
                "read_only_host": read_only_host,
                "app_host": app_host,
                "group_disk_used_bytes": group_disk_used_bytes,
                "date_sync": date_sync,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        cloud_storage_id = d.pop("cloud_storage_id")

        def _parse_purchase_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        purchase_id = _parse_purchase_id(d.pop("purchase_id"))

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        def _parse_read_write_host(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        read_write_host = _parse_read_write_host(d.pop("read_write_host"))

        def _parse_read_only_host(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        read_only_host = _parse_read_only_host(d.pop("read_only_host"))

        def _parse_app_host(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        app_host = _parse_app_host(d.pop("app_host"))

        def _parse_group_disk_used_bytes(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        group_disk_used_bytes = _parse_group_disk_used_bytes(d.pop("group_disk_used_bytes"))

        def _parse_date_sync(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_sync_type_0 = datetime.datetime.fromisoformat(data)

                return date_sync_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        date_sync = _parse_date_sync(d.pop("date_sync"))

        cloud_storage = cls(
            cloud_storage_id=cloud_storage_id,
            purchase_id=purchase_id,
            name=name,
            read_write_host=read_write_host,
            read_only_host=read_only_host,
            app_host=app_host,
            group_disk_used_bytes=group_disk_used_bytes,
            date_sync=date_sync,
        )

        cloud_storage.additional_properties = d
        return cloud_storage

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
