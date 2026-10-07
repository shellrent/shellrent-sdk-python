from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServerReinstallRequest")


@_attrs_define
class ServerReinstallRequest:
    safety_backup_enabled: bool | Unset = True
    """ Whether to perform a safety backup before reinstall """

    def to_dict(self) -> dict[str, Any]:
        safety_backup_enabled = self.safety_backup_enabled

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if safety_backup_enabled is not UNSET:
            field_dict["safety_backup_enabled"] = safety_backup_enabled

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        safety_backup_enabled = d.pop("safety_backup_enabled", UNSET)

        server_reinstall_request = cls(
            safety_backup_enabled=safety_backup_enabled,
        )

        return server_reinstall_request
