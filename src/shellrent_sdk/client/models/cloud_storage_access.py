from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CloudStorageAccess")


@_attrs_define
class CloudStorageAccess:
    """NFS access to a cloud storage: an IPv4 address allowed to mount the storage of a user"""

    access_id: None | str
    """ Id of the access, used in its path: the IPv4 address in `hostname` """
    cloud_storage_id: int
    """ Id of the cloud storage (`GET /api/v3/cloud-storages/{cloud_storage_id}`) """
    hostname: None | str
    """ IPv4 address allowed to mount the storage via NFS """
    username: None | str
    """ Username of the cloud storage user whose storage the address can mount (`GET /api/v3/cloud-
    storages/{cloud_storage_id}/users`) """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access_id: None | str
        access_id = self.access_id

        cloud_storage_id = self.cloud_storage_id

        hostname: None | str
        hostname = self.hostname

        username: None | str
        username = self.username

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "access_id": access_id,
                "cloud_storage_id": cloud_storage_id,
                "hostname": hostname,
                "username": username,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_access_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        access_id = _parse_access_id(d.pop("access_id"))

        cloud_storage_id = d.pop("cloud_storage_id")

        def _parse_hostname(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        hostname = _parse_hostname(d.pop("hostname"))

        def _parse_username(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        username = _parse_username(d.pop("username"))

        cloud_storage_access = cls(
            access_id=access_id,
            cloud_storage_id=cloud_storage_id,
            hostname=hostname,
            username=username,
        )

        cloud_storage_access.additional_properties = d
        return cloud_storage_access

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
