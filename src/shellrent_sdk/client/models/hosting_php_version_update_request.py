from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="HostingPhpVersionUpdateRequest")


@_attrs_define
class HostingPhpVersionUpdateRequest:
    version: str
    """ PHP version, one of those returned by `GET /api/v3/hostings/{hosting_id}/php-versions` (e.g. `8.3`) """

    def to_dict(self) -> dict[str, Any]:
        version = self.version

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "version": version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        version = d.pop("version")

        hosting_php_version_update_request = cls(
            version=version,
        )

        return hosting_php_version_update_request
