from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ServerOs")


@_attrs_define
class ServerOs:
    os_code: str
    os_name: str
    min_ram: int | None
    """ Min RAM (GB), for VPS/VM only """
    min_cpu: int | None
    """ Min vCPU, for VPS/VM only """
    min_disk: int | None
    """ Min disk (GB), for VPS/VM only """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        os_code = self.os_code

        os_name = self.os_name

        min_ram: int | None
        min_ram = self.min_ram

        min_cpu: int | None
        min_cpu = self.min_cpu

        min_disk: int | None
        min_disk = self.min_disk

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "os_code": os_code,
                "os_name": os_name,
                "min_ram": min_ram,
                "min_cpu": min_cpu,
                "min_disk": min_disk,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        os_code = d.pop("os_code")

        os_name = d.pop("os_name")

        def _parse_min_ram(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        min_ram = _parse_min_ram(d.pop("min_ram"))

        def _parse_min_cpu(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        min_cpu = _parse_min_cpu(d.pop("min_cpu"))

        def _parse_min_disk(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        min_disk = _parse_min_disk(d.pop("min_disk"))

        server_os = cls(
            os_code=os_code,
            os_name=os_name,
            min_ram=min_ram,
            min_cpu=min_cpu,
            min_disk=min_disk,
        )

        server_os.additional_properties = d
        return server_os

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
