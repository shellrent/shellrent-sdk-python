from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="HostingPhpVersion")


@_attrs_define
class HostingPhpVersion:
    """PHP version available for the hosting"""

    version: str
    """ PHP version, for example `8.3`: send it to `PATCH /api/v3/hostings/{hosting_id}/php-version` """
    is_current: bool
    """ Whether the hosting uses this version """
    is_default: bool
    """ Whether it is the default version of the web server """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        version = self.version

        is_current = self.is_current

        is_default = self.is_default

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "version": version,
                "is_current": is_current,
                "is_default": is_default,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        version = d.pop("version")

        is_current = d.pop("is_current")

        is_default = d.pop("is_default")

        hosting_php_version = cls(
            version=version,
            is_current=is_current,
            is_default=is_default,
        )

        hosting_php_version.additional_properties = d
        return hosting_php_version

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
