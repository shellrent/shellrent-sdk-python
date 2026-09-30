from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServerReinstallRequest")


@_attrs_define
class ServerReinstallRequest:
    safety_backup_enabled: bool | Unset = True
    """ Whether to perform a safety backup before reinstall """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        safety_backup_enabled = self.safety_backup_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
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

        server_reinstall_request.additional_properties = d
        return server_reinstall_request

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
