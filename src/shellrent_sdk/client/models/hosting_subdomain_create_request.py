from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="HostingSubdomainCreateRequest")


@_attrs_define
class HostingSubdomainCreateRequest:
    level_name: str
    """ Third-level subdomain name (without the main domain). """

    def to_dict(self) -> dict[str, Any]:
        level_name = self.level_name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "level_name": level_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        level_name = d.pop("level_name")

        hosting_subdomain_create_request = cls(
            level_name=level_name,
        )

        return hosting_subdomain_create_request
