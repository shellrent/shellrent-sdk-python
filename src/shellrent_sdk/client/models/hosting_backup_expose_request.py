from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="HostingBackupExposeRequest")


@_attrs_define
class HostingBackupExposeRequest:
    """Backups to expose: they are copied, without restoring them, into the FTP space of the hosting"""

    web_backup_id: int | None | Unset = UNSET
    """ The `backup_id` of a backup with category `web` returned by `GET /api/v3/hostings/{hosting_id}/backups`.
    Send at least one of web_backup_id and db_backup_id """
    db_backup_id: int | None | Unset = UNSET
    """ The `backup_id` of a backup with category `database` returned by `GET
    /api/v3/hostings/{hosting_id}/backups`. Send at least one of web_backup_id and db_backup_id """

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

        return hosting_backup_expose_request
