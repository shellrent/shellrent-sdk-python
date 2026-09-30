from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Microsoft365DomainAvailable")


@_attrs_define
class Microsoft365DomainAvailable:
    domain_prefix: str
    """ Requested tenant domain prefix """
    microsoft_domain: str
    """ Full ".onmicrosoft.com" domain """
    available: bool
    """ Whether the domain is available """
    microsoft_uuid: None | str
    """ Microsoft tenant UUID if available """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        domain_prefix = self.domain_prefix

        microsoft_domain = self.microsoft_domain

        available = self.available

        microsoft_uuid: None | str
        microsoft_uuid = self.microsoft_uuid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "domain_prefix": domain_prefix,
                "microsoft_domain": microsoft_domain,
                "available": available,
                "microsoft_uuid": microsoft_uuid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        domain_prefix = d.pop("domain_prefix")

        microsoft_domain = d.pop("microsoft_domain")

        available = d.pop("available")

        def _parse_microsoft_uuid(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        microsoft_uuid = _parse_microsoft_uuid(d.pop("microsoft_uuid"))

        microsoft_365_domain_available = cls(
            domain_prefix=domain_prefix,
            microsoft_domain=microsoft_domain,
            available=available,
            microsoft_uuid=microsoft_uuid,
        )

        microsoft_365_domain_available.additional_properties = d
        return microsoft_365_domain_available

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
