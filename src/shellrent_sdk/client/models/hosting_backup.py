from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="HostingBackup")


@_attrs_define
class HostingBackup:
    hosting_backup_id: int
    hosting_id: int
    backup_id: int
    category: None | str
    backup_type_code: None | str
    backup_frequency_code: None | str
    backup_date: datetime.datetime | None
    backup_size: int | None
    backup_duration: None | str
    exit_status: int | None
    error_type: None | str
    mailbox_name: None | str
    database_name: None | str
    date_created: datetime.datetime | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hosting_backup_id = self.hosting_backup_id

        hosting_id = self.hosting_id

        backup_id = self.backup_id

        category: None | str
        category = self.category

        backup_type_code: None | str
        backup_type_code = self.backup_type_code

        backup_frequency_code: None | str
        backup_frequency_code = self.backup_frequency_code

        backup_date: None | str
        if isinstance(self.backup_date, datetime.datetime):
            backup_date = self.backup_date.isoformat()
        else:
            backup_date = self.backup_date

        backup_size: int | None
        backup_size = self.backup_size

        backup_duration: None | str
        backup_duration = self.backup_duration

        exit_status: int | None
        exit_status = self.exit_status

        error_type: None | str
        error_type = self.error_type

        mailbox_name: None | str
        mailbox_name = self.mailbox_name

        database_name: None | str
        database_name = self.database_name

        date_created: None | str
        if isinstance(self.date_created, datetime.datetime):
            date_created = self.date_created.isoformat()
        else:
            date_created = self.date_created

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hosting_backup_id": hosting_backup_id,
                "hosting_id": hosting_id,
                "backup_id": backup_id,
                "category": category,
                "backup_type_code": backup_type_code,
                "backup_frequency_code": backup_frequency_code,
                "backup_date": backup_date,
                "backup_size": backup_size,
                "backup_duration": backup_duration,
                "exit_status": exit_status,
                "error_type": error_type,
                "mailbox_name": mailbox_name,
                "database_name": database_name,
                "date_created": date_created,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        hosting_backup_id = d.pop("hosting_backup_id")

        hosting_id = d.pop("hosting_id")

        backup_id = d.pop("backup_id")

        def _parse_category(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        category = _parse_category(d.pop("category"))

        def _parse_backup_type_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        backup_type_code = _parse_backup_type_code(d.pop("backup_type_code"))

        def _parse_backup_frequency_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        backup_frequency_code = _parse_backup_frequency_code(d.pop("backup_frequency_code"))

        def _parse_backup_date(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                backup_date_type_0 = datetime.datetime.fromisoformat(data)

                return backup_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        backup_date = _parse_backup_date(d.pop("backup_date"))

        def _parse_backup_size(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        backup_size = _parse_backup_size(d.pop("backup_size"))

        def _parse_backup_duration(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        backup_duration = _parse_backup_duration(d.pop("backup_duration"))

        def _parse_exit_status(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        exit_status = _parse_exit_status(d.pop("exit_status"))

        def _parse_error_type(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        error_type = _parse_error_type(d.pop("error_type"))

        def _parse_mailbox_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        mailbox_name = _parse_mailbox_name(d.pop("mailbox_name"))

        def _parse_database_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        database_name = _parse_database_name(d.pop("database_name"))

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

        hosting_backup = cls(
            hosting_backup_id=hosting_backup_id,
            hosting_id=hosting_id,
            backup_id=backup_id,
            category=category,
            backup_type_code=backup_type_code,
            backup_frequency_code=backup_frequency_code,
            backup_date=backup_date,
            backup_size=backup_size,
            backup_duration=backup_duration,
            exit_status=exit_status,
            error_type=error_type,
            mailbox_name=mailbox_name,
            database_name=database_name,
            date_created=date_created,
        )

        hosting_backup.additional_properties = d
        return hosting_backup

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
