from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ServerBackup")


@_attrs_define
class ServerBackup:
    """Backup of a server that the customer can see"""

    server_backup_id: int
    backup_recurrent_id: int | None
    """ Id of the run of the recurrent backup that made the backup; null for a one-off backup """
    backup_server_id_parent: int | None
    """ Id of the backup this one is based on, for incremental backups; null otherwise """
    server_id: int | None
    """ Id of the backed up server (`GET /api/v3/servers/{server_id}`) """
    cluster_id_server_residence: int | None
    """ Id of the cluster where the server resides """
    cluster_id_backup_residence: int | None
    """ Id of the cluster where the backup is kept """
    backup_type_id: int | None
    """ Id of the backup type """
    backup_mode: None | str
    """ Strategy of the backup type: `FULL`, `INC` (incremental) or `DIFF` (differential) """
    backup_frequency_id: int | None
    """ Id of the frequency of the backup type """
    backup_type_code: None | str
    """ Code of the backup type, for example `CLOUD_DAILY`, `CLOUD_WEEKLY` or `CLOUD_UNA_TANTUM` (one-off) """
    backup_frequency_code: None | str
    """ Frequency of the backup type: `D` daily, `W` weekly, `HM` twice a month, `M` monthly, `HY` every six months,
    `Y` yearly, `C` one-off, `R` private cloud replication """
    backup_date: datetime.datetime | None
    """ Date the backup was taken """
    backup_size: int | None
    """ Size of the backup, in MB """
    backup_duration: None | str
    """ Duration of the backup, as text in the `H:MM:SS` form, preceded by the days for longer backups (for example
    `1 day, 2:03:04`) """
    exit_status: int | None
    """ Exit status of the backup: `0` if it succeeded """
    error_type: None | str
    """ Error of the backup, as a code or a message (for example `DOWNLOAD_DISK_FAILED`); `N.A.` when it succeeded
    """
    date_created: datetime.datetime | None
    checksum: None | str
    """ Checksum of the backup, sent by the backup scripts; null if not sent """
    backup_user_visibility: bool | None
    """ Whether the customer can see the backup: only the most recent successful backups of each type are visible,
    as many as the retention of the type, and only those are returned """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        server_backup_id = self.server_backup_id

        backup_recurrent_id: int | None
        backup_recurrent_id = self.backup_recurrent_id

        backup_server_id_parent: int | None
        backup_server_id_parent = self.backup_server_id_parent

        server_id: int | None
        server_id = self.server_id

        cluster_id_server_residence: int | None
        cluster_id_server_residence = self.cluster_id_server_residence

        cluster_id_backup_residence: int | None
        cluster_id_backup_residence = self.cluster_id_backup_residence

        backup_type_id: int | None
        backup_type_id = self.backup_type_id

        backup_mode: None | str
        backup_mode = self.backup_mode

        backup_frequency_id: int | None
        backup_frequency_id = self.backup_frequency_id

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

        date_created: None | str
        if isinstance(self.date_created, datetime.datetime):
            date_created = self.date_created.isoformat()
        else:
            date_created = self.date_created

        checksum: None | str
        checksum = self.checksum

        backup_user_visibility: bool | None
        backup_user_visibility = self.backup_user_visibility

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "server_backup_id": server_backup_id,
                "backup_recurrent_id": backup_recurrent_id,
                "backup_server_id_parent": backup_server_id_parent,
                "server_id": server_id,
                "cluster_id_server_residence": cluster_id_server_residence,
                "cluster_id_backup_residence": cluster_id_backup_residence,
                "backup_type_id": backup_type_id,
                "backup_mode": backup_mode,
                "backup_frequency_id": backup_frequency_id,
                "backup_type_code": backup_type_code,
                "backup_frequency_code": backup_frequency_code,
                "backup_date": backup_date,
                "backup_size": backup_size,
                "backup_duration": backup_duration,
                "exit_status": exit_status,
                "error_type": error_type,
                "date_created": date_created,
                "checksum": checksum,
                "backup_user_visibility": backup_user_visibility,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        server_backup_id = d.pop("server_backup_id")

        def _parse_backup_recurrent_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        backup_recurrent_id = _parse_backup_recurrent_id(d.pop("backup_recurrent_id"))

        def _parse_backup_server_id_parent(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        backup_server_id_parent = _parse_backup_server_id_parent(d.pop("backup_server_id_parent"))

        def _parse_server_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        server_id = _parse_server_id(d.pop("server_id"))

        def _parse_cluster_id_server_residence(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        cluster_id_server_residence = _parse_cluster_id_server_residence(
            d.pop("cluster_id_server_residence")
        )

        def _parse_cluster_id_backup_residence(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        cluster_id_backup_residence = _parse_cluster_id_backup_residence(
            d.pop("cluster_id_backup_residence")
        )

        def _parse_backup_type_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        backup_type_id = _parse_backup_type_id(d.pop("backup_type_id"))

        def _parse_backup_mode(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        backup_mode = _parse_backup_mode(d.pop("backup_mode"))

        def _parse_backup_frequency_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        backup_frequency_id = _parse_backup_frequency_id(d.pop("backup_frequency_id"))

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

        def _parse_checksum(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        checksum = _parse_checksum(d.pop("checksum"))

        def _parse_backup_user_visibility(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        backup_user_visibility = _parse_backup_user_visibility(d.pop("backup_user_visibility"))

        server_backup = cls(
            server_backup_id=server_backup_id,
            backup_recurrent_id=backup_recurrent_id,
            backup_server_id_parent=backup_server_id_parent,
            server_id=server_id,
            cluster_id_server_residence=cluster_id_server_residence,
            cluster_id_backup_residence=cluster_id_backup_residence,
            backup_type_id=backup_type_id,
            backup_mode=backup_mode,
            backup_frequency_id=backup_frequency_id,
            backup_type_code=backup_type_code,
            backup_frequency_code=backup_frequency_code,
            backup_date=backup_date,
            backup_size=backup_size,
            backup_duration=backup_duration,
            exit_status=exit_status,
            error_type=error_type,
            date_created=date_created,
            checksum=checksum,
            backup_user_visibility=backup_user_visibility,
        )

        server_backup.additional_properties = d
        return server_backup

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
