from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.hosting_http_version_update_request_version import (
    HostingHttpVersionUpdateRequestVersion,
)

T = TypeVar("T", bound="HostingHttpVersionUpdateRequest")


@_attrs_define
class HostingHttpVersionUpdateRequest:
    version: HostingHttpVersionUpdateRequestVersion
    """ HTTP version: 1 for HTTP/1.1, 2 for HTTP/2 """

    def to_dict(self) -> dict[str, Any]:
        version = self.version.value

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
        version = HostingHttpVersionUpdateRequestVersion(d.pop("version"))

        hosting_http_version_update_request = cls(
            version=version,
        )

        return hosting_http_version_update_request
