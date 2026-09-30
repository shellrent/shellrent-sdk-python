from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PrivateCloudVmUpdateRequest")


@_attrs_define
class PrivateCloudVmUpdateRequest:
    cpu: int | Unset = UNSET
    ram: int | Unset = UNSET
    disk: int | Unset = UNSET
    note: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cpu = self.cpu

        ram = self.ram

        disk = self.disk

        note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cpu is not UNSET:
            field_dict["cpu"] = cpu
        if ram is not UNSET:
            field_dict["ram"] = ram
        if disk is not UNSET:
            field_dict["disk"] = disk
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        cpu = d.pop("cpu", UNSET)

        ram = d.pop("ram", UNSET)

        disk = d.pop("disk", UNSET)

        note = d.pop("note", UNSET)

        private_cloud_vm_update_request = cls(
            cpu=cpu,
            ram=ram,
            disk=disk,
            note=note,
        )

        private_cloud_vm_update_request.additional_properties = d
        return private_cloud_vm_update_request

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
