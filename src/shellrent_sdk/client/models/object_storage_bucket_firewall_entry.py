from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ObjectStorageBucketFirewallEntry")


@_attrs_define
class ObjectStorageBucketFirewallEntry:
    entry_id: int
    object_storage_id: int
    bucket_id: int
    ip: None | str
    active: bool | None
    date_created: datetime.datetime | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        entry_id = self.entry_id

        object_storage_id = self.object_storage_id

        bucket_id = self.bucket_id

        ip: None | str
        ip = self.ip

        active: bool | None
        active = self.active

        date_created: None | str
        if isinstance(self.date_created, datetime.datetime):
            date_created = self.date_created.isoformat()
        else:
            date_created = self.date_created

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "entry_id": entry_id,
                "object_storage_id": object_storage_id,
                "bucket_id": bucket_id,
                "ip": ip,
                "active": active,
                "date_created": date_created,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        entry_id = d.pop("entry_id")

        object_storage_id = d.pop("object_storage_id")

        bucket_id = d.pop("bucket_id")

        def _parse_ip(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        ip = _parse_ip(d.pop("ip"))

        def _parse_active(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        active = _parse_active(d.pop("active"))

        def _parse_date_created(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_created_type_0 = datetime.datetime.fromisoformat(data)

                return date_created_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        date_created = _parse_date_created(d.pop("date_created"))

        object_storage_bucket_firewall_entry = cls(
            entry_id=entry_id,
            object_storage_id=object_storage_id,
            bucket_id=bucket_id,
            ip=ip,
            active=active,
            date_created=date_created,
        )

        object_storage_bucket_firewall_entry.additional_properties = d
        return object_storage_bucket_firewall_entry

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
