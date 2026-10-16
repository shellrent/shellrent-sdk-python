from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="ObjectStorageBucketFirewallEntryCreateRequest")


@_attrs_define
class ObjectStorageBucketFirewallEntryCreateRequest:
    """Address or subnet to allow in the firewall of a bucket"""

    ip: str
    """ IPv4 or IPv6 address, or a subnet in CIDR notation """

    def to_dict(self) -> dict[str, Any]:
        ip = self.ip

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "ip": ip,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        ip = d.pop("ip")

        object_storage_bucket_firewall_entry_create_request = cls(
            ip=ip,
        )

        return object_storage_bucket_firewall_entry_create_request
