from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.hosting_backup import HostingBackup
    from ..models.hosting_backup_response_meta_type_0 import HostingBackupResponseMetaType0


T = TypeVar("T", bound="HostingBackupResponse")


@_attrs_define
class HostingBackupResponse:
    """Successful response with one `HostingBackup`"""

    error: Literal[0]
    """ Always 0 in a successful response """
    message: None | str
    """ Always null in a successful response """
    data: HostingBackup
    """ Backup that contains the hosting: a backup of a web, database or mail server, with the database or the
    mailbox of the hosting that it saved """
    meta: HostingBackupResponseMetaType0 | None
    """ Always null: only the paginated lists have a `meta` """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.hosting_backup_response_meta_type_0 import HostingBackupResponseMetaType0

        error = self.error

        message: None | str
        message = self.message

        data = self.data.to_dict()

        meta: dict[str, Any] | None
        if isinstance(self.meta, HostingBackupResponseMetaType0):
            meta = self.meta.to_dict()
        else:
            meta = self.meta

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "error": error,
                "message": message,
                "data": data,
                "meta": meta,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.hosting_backup import HostingBackup
        from ..models.hosting_backup_response_meta_type_0 import (
            HostingBackupResponseMetaType0,
        )

        d = dict(src_dict)
        error = cast(Literal[0], d.pop("error"))
        if error != 0:
            raise ValueError(f"error must match const 0, got '{error}'")

        def _parse_message(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        message = _parse_message(d.pop("message"))

        data = HostingBackup.from_dict(d.pop("data"))

        def _parse_meta(data: object) -> HostingBackupResponseMetaType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                meta_type_0 = HostingBackupResponseMetaType0.from_dict(data)

                return meta_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(HostingBackupResponseMetaType0 | None, data)

        meta = _parse_meta(d.pop("meta"))

        hosting_backup_response = cls(
            error=error,
            message=message,
            data=data,
            meta=meta,
        )

        hosting_backup_response.additional_properties = d
        return hosting_backup_response

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
