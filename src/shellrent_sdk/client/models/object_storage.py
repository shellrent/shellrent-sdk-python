from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ObjectStorage")


@_attrs_define
class ObjectStorage:
    object_storage_id: int
    purchase_id: int | None
    name: None | str
    email: None | str
    code: None | str
    code_full: None | str
    active: bool | None
    active_storage_bytes: int | None
    deleted_storage_bytes: int | None
    active_objects: int | None
    deleted_objects: int | None
    api_calls_count: int | None
    storage_wrote_bytes: int | None
    storage_read_bytes: int | None
    egress_traffic_bytes: int | None
    ingress_traffic_bytes: int | None
    reference_date: datetime.date | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_storage_id = self.object_storage_id

        purchase_id: int | None
        purchase_id = self.purchase_id

        name: None | str
        name = self.name

        email: None | str
        email = self.email

        code: None | str
        code = self.code

        code_full: None | str
        code_full = self.code_full

        active: bool | None
        active = self.active

        active_storage_bytes: int | None
        active_storage_bytes = self.active_storage_bytes

        deleted_storage_bytes: int | None
        deleted_storage_bytes = self.deleted_storage_bytes

        active_objects: int | None
        active_objects = self.active_objects

        deleted_objects: int | None
        deleted_objects = self.deleted_objects

        api_calls_count: int | None
        api_calls_count = self.api_calls_count

        storage_wrote_bytes: int | None
        storage_wrote_bytes = self.storage_wrote_bytes

        storage_read_bytes: int | None
        storage_read_bytes = self.storage_read_bytes

        egress_traffic_bytes: int | None
        egress_traffic_bytes = self.egress_traffic_bytes

        ingress_traffic_bytes: int | None
        ingress_traffic_bytes = self.ingress_traffic_bytes

        reference_date: None | str
        if isinstance(self.reference_date, datetime.date):
            reference_date = self.reference_date.isoformat()
        else:
            reference_date = self.reference_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "object_storage_id": object_storage_id,
                "purchase_id": purchase_id,
                "name": name,
                "email": email,
                "code": code,
                "code_full": code_full,
                "active": active,
                "active_storage_bytes": active_storage_bytes,
                "deleted_storage_bytes": deleted_storage_bytes,
                "active_objects": active_objects,
                "deleted_objects": deleted_objects,
                "api_calls_count": api_calls_count,
                "storage_wrote_bytes": storage_wrote_bytes,
                "storage_read_bytes": storage_read_bytes,
                "egress_traffic_bytes": egress_traffic_bytes,
                "ingress_traffic_bytes": ingress_traffic_bytes,
                "reference_date": reference_date,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        object_storage_id = d.pop("object_storage_id")

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

        def _parse_email(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        email = _parse_email(d.pop("email"))

        def _parse_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        code = _parse_code(d.pop("code"))

        def _parse_code_full(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        code_full = _parse_code_full(d.pop("code_full"))

        def _parse_active(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        active = _parse_active(d.pop("active"))

        def _parse_active_storage_bytes(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        active_storage_bytes = _parse_active_storage_bytes(d.pop("active_storage_bytes"))

        def _parse_deleted_storage_bytes(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        deleted_storage_bytes = _parse_deleted_storage_bytes(d.pop("deleted_storage_bytes"))

        def _parse_active_objects(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        active_objects = _parse_active_objects(d.pop("active_objects"))

        def _parse_deleted_objects(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        deleted_objects = _parse_deleted_objects(d.pop("deleted_objects"))

        def _parse_api_calls_count(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        api_calls_count = _parse_api_calls_count(d.pop("api_calls_count"))

        def _parse_storage_wrote_bytes(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        storage_wrote_bytes = _parse_storage_wrote_bytes(d.pop("storage_wrote_bytes"))

        def _parse_storage_read_bytes(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        storage_read_bytes = _parse_storage_read_bytes(d.pop("storage_read_bytes"))

        def _parse_egress_traffic_bytes(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        egress_traffic_bytes = _parse_egress_traffic_bytes(d.pop("egress_traffic_bytes"))

        def _parse_ingress_traffic_bytes(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        ingress_traffic_bytes = _parse_ingress_traffic_bytes(d.pop("ingress_traffic_bytes"))

        def _parse_reference_date(data: object) -> datetime.date | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                reference_date_type_0 = datetime.date.fromisoformat(data)

                return reference_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None, data)

        reference_date = _parse_reference_date(d.pop("reference_date"))

        object_storage = cls(
            object_storage_id=object_storage_id,
            purchase_id=purchase_id,
            name=name,
            email=email,
            code=code,
            code_full=code_full,
            active=active,
            active_storage_bytes=active_storage_bytes,
            deleted_storage_bytes=deleted_storage_bytes,
            active_objects=active_objects,
            deleted_objects=deleted_objects,
            api_calls_count=api_calls_count,
            storage_wrote_bytes=storage_wrote_bytes,
            storage_read_bytes=storage_read_bytes,
            egress_traffic_bytes=egress_traffic_bytes,
            ingress_traffic_bytes=ingress_traffic_bytes,
            reference_date=reference_date,
        )

        object_storage.additional_properties = d
        return object_storage

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
