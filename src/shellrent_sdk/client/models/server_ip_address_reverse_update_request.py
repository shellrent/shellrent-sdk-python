from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="ServerIpAddressReverseUpdateRequest")


@_attrs_define
class ServerIpAddressReverseUpdateRequest:
    reverse_dns: None | str
    """ Hostname to set as reverse DNS of the IP address; null or an empty string removes it, like `DELETE
    /api/v3/servers/{server_id}/ip-addresses/{ip_address_id}/rdns` """

    def to_dict(self) -> dict[str, Any]:
        reverse_dns: None | str
        reverse_dns = self.reverse_dns

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "reverse_dns": reverse_dns,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_reverse_dns(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        reverse_dns = _parse_reverse_dns(d.pop("reverse_dns"))

        server_ip_address_reverse_update_request = cls(
            reverse_dns=reverse_dns,
        )

        return server_ip_address_reverse_update_request
