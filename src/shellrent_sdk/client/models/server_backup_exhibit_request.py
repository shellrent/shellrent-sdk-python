from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="ServerBackupExhibitRequest")


@_attrs_define
class ServerBackupExhibitRequest:
    """Backup of the server to expose"""

    backup_id: int
    """ ID of the server backup to expose """

    def to_dict(self) -> dict[str, Any]:
        backup_id = self.backup_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "backup_id": backup_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        backup_id = d.pop("backup_id")

        server_backup_exhibit_request = cls(
            backup_id=backup_id,
        )

        return server_backup_exhibit_request
