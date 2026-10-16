from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="CloudStorageAccessCreateRequest")


@_attrs_define
class CloudStorageAccessCreateRequest:
    """NFS access to create: an IPv4 address allowed to mount the storage of a user"""

    hostname: str
    """ IPv4 address to allow to mount the storage via NFS """
    username: str
    """ Username of the user whose storage the address can mount: the `PRIMARY` user or an `ADDITIONAL` user of the
    cloud storage (`GET /api/v3/cloud-storages/{cloud_storage_id}/users`) """

    def to_dict(self) -> dict[str, Any]:
        hostname = self.hostname

        username = self.username

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "hostname": hostname,
                "username": username,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        hostname = d.pop("hostname")

        username = d.pop("username")

        cloud_storage_access_create_request = cls(
            hostname=hostname,
            username=username,
        )

        return cloud_storage_access_create_request
