from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="PrivateCloudVmUpdateRequest")


@_attrs_define
class PrivateCloudVmUpdateRequest:
    cpu: int | Unset = UNSET
    """ Number of CPU cores. Omit it to keep the current value; the allowed range depends on the resources available
    on the private cloud """
    ram: int | Unset = UNSET
    """ RAM of the virtual machine, in megabytes. Omit it to keep the current value; the allowed range depends on
    the resources available on the private cloud """
    disk: int | Unset = UNSET
    """ Disk space of the virtual machine, in gigabytes: it cannot be lower than the current one. Omit it to keep
    the current value """
    note: None | str | Unset = UNSET
    """ Note of the virtual machine. Omit it to keep the current note; send an empty string or null to remove it """

    def to_dict(self) -> dict[str, Any]:
        cpu = self.cpu

        ram = self.ram

        disk = self.disk

        note: None | str | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        field_dict: dict[str, Any] = {}

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

        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))

        private_cloud_vm_update_request = cls(
            cpu=cpu,
            ram=ram,
            disk=disk,
            note=note,
        )

        return private_cloud_vm_update_request
