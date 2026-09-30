from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.server_os import ServerOs


T = TypeVar("T", bound="ServerTemplate")


@_attrs_define
class ServerTemplate:
    template_code: str
    template_name: str
    template_name_alternative: None | str
    min_ram: int | None
    """ Min RAM (GB), for VPS/VM only """
    min_cpu: int | None
    """ Min vCPU, for VPS/VM only """
    min_disk: int | None
    """ Min disk (GB), for VPS/VM only """
    operative_systems: list[ServerOs]
    """ Compatible operative systems """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        template_code = self.template_code

        template_name = self.template_name

        template_name_alternative: None | str
        template_name_alternative = self.template_name_alternative

        min_ram: int | None
        min_ram = self.min_ram

        min_cpu: int | None
        min_cpu = self.min_cpu

        min_disk: int | None
        min_disk = self.min_disk

        operative_systems = []
        for operative_systems_item_data in self.operative_systems:
            operative_systems_item = operative_systems_item_data.to_dict()
            operative_systems.append(operative_systems_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "template_code": template_code,
                "template_name": template_name,
                "template_name_alternative": template_name_alternative,
                "min_ram": min_ram,
                "min_cpu": min_cpu,
                "min_disk": min_disk,
                "operative_systems": operative_systems,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.server_os import ServerOs

        d = dict(src_dict)
        template_code = d.pop("template_code")

        template_name = d.pop("template_name")

        def _parse_template_name_alternative(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        template_name_alternative = _parse_template_name_alternative(
            d.pop("template_name_alternative")
        )

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

        operative_systems = []
        _operative_systems = d.pop("operative_systems")
        for operative_systems_item_data in _operative_systems:
            operative_systems_item = ServerOs.from_dict(operative_systems_item_data)

            operative_systems.append(operative_systems_item)

        server_template = cls(
            template_code=template_code,
            template_name=template_name,
            template_name_alternative=template_name_alternative,
            min_ram=min_ram,
            min_cpu=min_cpu,
            min_disk=min_disk,
            operative_systems=operative_systems,
        )

        server_template.additional_properties = d
        return server_template

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
