from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="HostingModSecurityUpdateRequest")


@_attrs_define
class HostingModSecurityUpdateRequest:
    enable: bool
    """ Whether to enable (true) or disable (false) ModSecurity """

    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "enable": enable,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        enable = d.pop("enable")

        hosting_mod_security_update_request = cls(
            enable=enable,
        )

        return hosting_mod_security_update_request
