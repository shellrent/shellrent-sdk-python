from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CloudStorageUser")


@_attrs_define
class CloudStorageUser:
    """User of a cloud storage, with its quotas and the space used"""

    cloud_storage_user_id: int
    cloud_storage_id: int
    """ Id of the cloud storage (`GET /api/v3/cloud-storages/{cloud_storage_id}`) """
    purchase_id: int | None
    """ Id of the purchase of the user (`GET /api/v3/purchases/{purchase_id}`): the cloud storage purchase, or the
    own purchase of an `ADDITIONAL` user """
    type_: None | str
    """ Type of the user: `PRIMARY` (main user), `ADDITIONAL` (additional user, with its own purchase), or
    `DISASTER_RECOVERY`, `TEMPLATE_VM` and `SELF_CLOUD` for the users managed by those services """
    username: None | str
    password: None | str
    """ Password of the user; null without the cloudstorage:secrets scope """
    path: None | str
    """ Home path of the user on the storage """
    soft_quota_gb: float | None
    """ Soft quota of the user, in GB (1 GB = 1024 MB): it can be exceeded, up to the hard quota, for a grace period
    """
    hard_quota_gb: float | None
    """ Hard quota of the user, in GB (1 GB = 1024 MB): the limit that the used space cannot exceed """
    used_space_bytes: int | None
    """ Space used by the user at the last sync of the cloud storage, in bytes; null before the first sync """
    allocated_space_bytes: int | None
    """ Space allocated to the user, that is its hard quota at the last sync of the cloud storage, in bytes; null
    before the first sync """
    grace_period_seconds: int | None
    """ Grace period left to go back under the soft quota, in seconds, saved the last time the user was found over
    quota; `0` if never. Only `PRIMARY` users are checked: `0` for the `ADDITIONAL` ones, null for the users of the
    services """
    last_alert: datetime.datetime | None
    """ Date of the last email that warned the customer that the user is over its soft quota, sent at most once a
    week and only for `PRIMARY` users; null if it was not over quota at the last check """
    active: bool | None
    """ Whether the user is active: deleted users are not returned """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cloud_storage_user_id = self.cloud_storage_user_id

        cloud_storage_id = self.cloud_storage_id

        purchase_id: int | None
        purchase_id = self.purchase_id

        type_: None | str
        type_ = self.type_

        username: None | str
        username = self.username

        password: None | str
        password = self.password

        path: None | str
        path = self.path

        soft_quota_gb: float | None
        soft_quota_gb = self.soft_quota_gb

        hard_quota_gb: float | None
        hard_quota_gb = self.hard_quota_gb

        used_space_bytes: int | None
        used_space_bytes = self.used_space_bytes

        allocated_space_bytes: int | None
        allocated_space_bytes = self.allocated_space_bytes

        grace_period_seconds: int | None
        grace_period_seconds = self.grace_period_seconds

        last_alert: None | str
        if isinstance(self.last_alert, datetime.datetime):
            last_alert = self.last_alert.isoformat()
        else:
            last_alert = self.last_alert

        active: bool | None
        active = self.active

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cloud_storage_user_id": cloud_storage_user_id,
                "cloud_storage_id": cloud_storage_id,
                "purchase_id": purchase_id,
                "type": type_,
                "username": username,
                "password": password,
                "path": path,
                "soft_quota_gb": soft_quota_gb,
                "hard_quota_gb": hard_quota_gb,
                "used_space_bytes": used_space_bytes,
                "allocated_space_bytes": allocated_space_bytes,
                "grace_period_seconds": grace_period_seconds,
                "last_alert": last_alert,
                "active": active,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        cloud_storage_user_id = d.pop("cloud_storage_user_id")

        cloud_storage_id = d.pop("cloud_storage_id")

        def _parse_purchase_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        purchase_id = _parse_purchase_id(d.pop("purchase_id"))

        def _parse_type_(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        type_ = _parse_type_(d.pop("type"))

        def _parse_username(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        username = _parse_username(d.pop("username"))

        def _parse_password(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        password = _parse_password(d.pop("password"))

        def _parse_path(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        path = _parse_path(d.pop("path"))

        def _parse_soft_quota_gb(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        soft_quota_gb = _parse_soft_quota_gb(d.pop("soft_quota_gb"))

        def _parse_hard_quota_gb(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        hard_quota_gb = _parse_hard_quota_gb(d.pop("hard_quota_gb"))

        def _parse_used_space_bytes(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        used_space_bytes = _parse_used_space_bytes(d.pop("used_space_bytes"))

        def _parse_allocated_space_bytes(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        allocated_space_bytes = _parse_allocated_space_bytes(d.pop("allocated_space_bytes"))

        def _parse_grace_period_seconds(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        grace_period_seconds = _parse_grace_period_seconds(d.pop("grace_period_seconds"))

        def _parse_last_alert(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_alert_type_0 = datetime.datetime.fromisoformat(data)

                return last_alert_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_alert = _parse_last_alert(d.pop("last_alert"))

        def _parse_active(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        active = _parse_active(d.pop("active"))

        cloud_storage_user = cls(
            cloud_storage_user_id=cloud_storage_user_id,
            cloud_storage_id=cloud_storage_id,
            purchase_id=purchase_id,
            type_=type_,
            username=username,
            password=password,
            path=path,
            soft_quota_gb=soft_quota_gb,
            hard_quota_gb=hard_quota_gb,
            used_space_bytes=used_space_bytes,
            allocated_space_bytes=allocated_space_bytes,
            grace_period_seconds=grace_period_seconds,
            last_alert=last_alert,
            active=active,
        )

        cloud_storage_user.additional_properties = d
        return cloud_storage_user

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
