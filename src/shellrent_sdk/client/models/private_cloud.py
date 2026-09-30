from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PrivateCloud")


@_attrs_define
class PrivateCloud:
    purchase_id: int
    server_id: int | None
    max_vm: int | None
    available_vm: int | None
    max_cpu: int | None
    cpu_overallocation: int | None
    min_vm_cpu: int | None
    max_vm_cpu: int | None
    max_ram: int | None
    min_vm_ram: int | None
    max_vm_ram: int | None
    max_disk: int | None
    min_vm_disk: int | None
    max_vm_disk: int | None
    max_backup: int | None
    max_disk_backup: int | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        purchase_id = self.purchase_id

        server_id: int | None
        server_id = self.server_id

        max_vm: int | None
        max_vm = self.max_vm

        available_vm: int | None
        available_vm = self.available_vm

        max_cpu: int | None
        max_cpu = self.max_cpu

        cpu_overallocation: int | None
        cpu_overallocation = self.cpu_overallocation

        min_vm_cpu: int | None
        min_vm_cpu = self.min_vm_cpu

        max_vm_cpu: int | None
        max_vm_cpu = self.max_vm_cpu

        max_ram: int | None
        max_ram = self.max_ram

        min_vm_ram: int | None
        min_vm_ram = self.min_vm_ram

        max_vm_ram: int | None
        max_vm_ram = self.max_vm_ram

        max_disk: int | None
        max_disk = self.max_disk

        min_vm_disk: int | None
        min_vm_disk = self.min_vm_disk

        max_vm_disk: int | None
        max_vm_disk = self.max_vm_disk

        max_backup: int | None
        max_backup = self.max_backup

        max_disk_backup: int | None
        max_disk_backup = self.max_disk_backup

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "purchase_id": purchase_id,
                "server_id": server_id,
                "max_vm": max_vm,
                "available_vm": available_vm,
                "max_cpu": max_cpu,
                "cpu_overallocation": cpu_overallocation,
                "min_vm_cpu": min_vm_cpu,
                "max_vm_cpu": max_vm_cpu,
                "max_ram": max_ram,
                "min_vm_ram": min_vm_ram,
                "max_vm_ram": max_vm_ram,
                "max_disk": max_disk,
                "min_vm_disk": min_vm_disk,
                "max_vm_disk": max_vm_disk,
                "max_backup": max_backup,
                "max_disk_backup": max_disk_backup,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        purchase_id = d.pop("purchase_id")

        def _parse_server_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        server_id = _parse_server_id(d.pop("server_id"))

        def _parse_max_vm(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        max_vm = _parse_max_vm(d.pop("max_vm"))

        def _parse_available_vm(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        available_vm = _parse_available_vm(d.pop("available_vm"))

        def _parse_max_cpu(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        max_cpu = _parse_max_cpu(d.pop("max_cpu"))

        def _parse_cpu_overallocation(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        cpu_overallocation = _parse_cpu_overallocation(d.pop("cpu_overallocation"))

        def _parse_min_vm_cpu(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        min_vm_cpu = _parse_min_vm_cpu(d.pop("min_vm_cpu"))

        def _parse_max_vm_cpu(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        max_vm_cpu = _parse_max_vm_cpu(d.pop("max_vm_cpu"))

        def _parse_max_ram(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        max_ram = _parse_max_ram(d.pop("max_ram"))

        def _parse_min_vm_ram(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        min_vm_ram = _parse_min_vm_ram(d.pop("min_vm_ram"))

        def _parse_max_vm_ram(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        max_vm_ram = _parse_max_vm_ram(d.pop("max_vm_ram"))

        def _parse_max_disk(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        max_disk = _parse_max_disk(d.pop("max_disk"))

        def _parse_min_vm_disk(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        min_vm_disk = _parse_min_vm_disk(d.pop("min_vm_disk"))

        def _parse_max_vm_disk(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        max_vm_disk = _parse_max_vm_disk(d.pop("max_vm_disk"))

        def _parse_max_backup(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        max_backup = _parse_max_backup(d.pop("max_backup"))

        def _parse_max_disk_backup(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        max_disk_backup = _parse_max_disk_backup(d.pop("max_disk_backup"))

        private_cloud = cls(
            purchase_id=purchase_id,
            server_id=server_id,
            max_vm=max_vm,
            available_vm=available_vm,
            max_cpu=max_cpu,
            cpu_overallocation=cpu_overallocation,
            min_vm_cpu=min_vm_cpu,
            max_vm_cpu=max_vm_cpu,
            max_ram=max_ram,
            min_vm_ram=min_vm_ram,
            max_vm_ram=max_vm_ram,
            max_disk=max_disk,
            min_vm_disk=min_vm_disk,
            max_vm_disk=max_vm_disk,
            max_backup=max_backup,
            max_disk_backup=max_disk_backup,
        )

        private_cloud.additional_properties = d
        return private_cloud

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
