from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DomainCanChangeNameservers")


@_attrs_define
class DomainCanChangeNameservers:
    domain_id: int
    can_activate_standard: bool
    can_activate_cloudflare: bool
    can_activate_external: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        domain_id = self.domain_id

        can_activate_standard = self.can_activate_standard

        can_activate_cloudflare = self.can_activate_cloudflare

        can_activate_external = self.can_activate_external

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "domain_id": domain_id,
                "can_activate_standard": can_activate_standard,
                "can_activate_cloudflare": can_activate_cloudflare,
                "can_activate_external": can_activate_external,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        domain_id = d.pop("domain_id")

        can_activate_standard = d.pop("can_activate_standard")

        can_activate_cloudflare = d.pop("can_activate_cloudflare")

        can_activate_external = d.pop("can_activate_external")

        domain_can_change_nameservers = cls(
            domain_id=domain_id,
            can_activate_standard=can_activate_standard,
            can_activate_cloudflare=can_activate_cloudflare,
            can_activate_external=can_activate_external,
        )

        domain_can_change_nameservers.additional_properties = d
        return domain_can_change_nameservers

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
