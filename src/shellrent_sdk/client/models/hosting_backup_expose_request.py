from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HostingBackupExposeRequest")


@_attrs_define
class HostingBackupExposeRequest:
    web_backup_id: int | None | Unset = UNSET
    db_backup_id: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        web_backup_id: int | None | Unset
        if isinstance(self.web_backup_id, Unset):
            web_backup_id = UNSET
        else:
            web_backup_id = self.web_backup_id

        db_backup_id: int | None | Unset
        if isinstance(self.db_backup_id, Unset):
            db_backup_id = UNSET
        else:
            db_backup_id = self.db_backup_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if web_backup_id is not UNSET:
            field_dict["web_backup_id"] = web_backup_id
        if db_backup_id is not UNSET:
            field_dict["db_backup_id"] = db_backup_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_web_backup_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        web_backup_id = _parse_web_backup_id(d.pop("web_backup_id", UNSET))

        def _parse_db_backup_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        db_backup_id = _parse_db_backup_id(d.pop("db_backup_id", UNSET))

        hosting_backup_expose_request = cls(
            web_backup_id=web_backup_id,
            db_backup_id=db_backup_id,
        )

        hosting_backup_expose_request.additional_properties = d
        return hosting_backup_expose_request

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
