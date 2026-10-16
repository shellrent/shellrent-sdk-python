from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="CloudStorageUserSizeUpdateRequest")


@_attrs_define
class CloudStorageUserSizeUpdateRequest:
    """New quota of an additional user of the cloud storage"""

    quota_gb: float
    """ New quota of the user, in GB (1 GB = 1024 MB), set as both its soft and hard quota: from 0 to the soft quota
    of the `PRIMARY` user. Only `ADDITIONAL` users can be changed """

    def to_dict(self) -> dict[str, Any]:
        quota_gb = self.quota_gb

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "quota_gb": quota_gb,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        quota_gb = d.pop("quota_gb")

        cloud_storage_user_size_update_request = cls(
            quota_gb=quota_gb,
        )

        return cloud_storage_user_size_update_request
