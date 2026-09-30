from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HostingSubdomainCreateRequest")


@_attrs_define
class HostingSubdomainCreateRequest:
    level_name: str
    """ Third-level subdomain name (without the main domain). """
    subdomain: str | Unset = UNSET
    """ Alias of level_name. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        level_name = self.level_name

        subdomain = self.subdomain

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "level_name": level_name,
            }
        )
        if subdomain is not UNSET:
            field_dict["subdomain"] = subdomain

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        level_name = d.pop("level_name")

        subdomain = d.pop("subdomain", UNSET)

        hosting_subdomain_create_request = cls(
            level_name=level_name,
            subdomain=subdomain,
        )

        hosting_subdomain_create_request.additional_properties = d
        return hosting_subdomain_create_request

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
