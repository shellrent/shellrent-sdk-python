from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ServerSnapshot")


@_attrs_define
class ServerSnapshot:
    snapshot_id: int
    server_id: int
    snapshot_name: None | str
    snapshot_reference: None | str
    active: bool
    date_expiry: datetime.datetime | None
    date_created: datetime.datetime | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        snapshot_id = self.snapshot_id

        server_id = self.server_id

        snapshot_name: None | str
        snapshot_name = self.snapshot_name

        snapshot_reference: None | str
        snapshot_reference = self.snapshot_reference

        active = self.active

        date_expiry: None | str
        if isinstance(self.date_expiry, datetime.datetime):
            date_expiry = self.date_expiry.isoformat()
        else:
            date_expiry = self.date_expiry

        date_created: None | str
        if isinstance(self.date_created, datetime.datetime):
            date_created = self.date_created.isoformat()
        else:
            date_created = self.date_created

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "snapshot_id": snapshot_id,
                "server_id": server_id,
                "snapshot_name": snapshot_name,
                "snapshot_reference": snapshot_reference,
                "active": active,
                "date_expiry": date_expiry,
                "date_created": date_created,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        snapshot_id = d.pop("snapshot_id")

        server_id = d.pop("server_id")

        def _parse_snapshot_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        snapshot_name = _parse_snapshot_name(d.pop("snapshot_name"))

        def _parse_snapshot_reference(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        snapshot_reference = _parse_snapshot_reference(d.pop("snapshot_reference"))

        active = d.pop("active")

        def _parse_date_expiry(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_expiry_type_0 = datetime.datetime.fromisoformat(data)

                return date_expiry_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        date_expiry = _parse_date_expiry(d.pop("date_expiry"))

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

        server_snapshot = cls(
            snapshot_id=snapshot_id,
            server_id=server_id,
            snapshot_name=snapshot_name,
            snapshot_reference=snapshot_reference,
            active=active,
            date_expiry=date_expiry,
            date_created=date_created,
        )

        server_snapshot.additional_properties = d
        return server_snapshot

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
