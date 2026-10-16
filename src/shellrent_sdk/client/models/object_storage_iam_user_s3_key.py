from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ObjectStorageIamUserS3Key")


@_attrs_define
class ObjectStorageIamUserS3Key:
    """S3 key of an IAM user of an object storage"""

    s3_key_id: int
    object_storage_id: int
    """ Id of the object storage (`GET /api/v3/object-storages/{object_storage_id}`) """
    iam_user_id: int
    """ Id of the IAM user (`GET /api/v3/object-storages/{object_storage_id}/iam-users/{iam_user_id}`) """
    access_key: None | str
    """ Access key ID, to use with `secret_key` in the S3 clients """
    secret_key: None | str
    """ Secret of the S3 key; returned when the key is created and, afterwards, only with the objectstorage:secrets
    scope (null otherwise) """
    status: None | str
    """ Status of the key in the IAM service of the storage, for example `Active` """
    active: bool | None
    """ Whether the key is active: deleted keys are not returned; its state on the storage is in `status` """
    date_created: datetime.datetime | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        s3_key_id = self.s3_key_id

        object_storage_id = self.object_storage_id

        iam_user_id = self.iam_user_id

        access_key: None | str
        access_key = self.access_key

        secret_key: None | str
        secret_key = self.secret_key

        status: None | str
        status = self.status

        active: bool | None
        active = self.active

        date_created: None | str
        if isinstance(self.date_created, datetime.datetime):
            date_created = self.date_created.isoformat()
        else:
            date_created = self.date_created

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "s3_key_id": s3_key_id,
                "object_storage_id": object_storage_id,
                "iam_user_id": iam_user_id,
                "access_key": access_key,
                "secret_key": secret_key,
                "status": status,
                "active": active,
                "date_created": date_created,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        s3_key_id = d.pop("s3_key_id")

        object_storage_id = d.pop("object_storage_id")

        iam_user_id = d.pop("iam_user_id")

        def _parse_access_key(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        access_key = _parse_access_key(d.pop("access_key"))

        def _parse_secret_key(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        secret_key = _parse_secret_key(d.pop("secret_key"))

        def _parse_status(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        status = _parse_status(d.pop("status"))

        def _parse_active(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        active = _parse_active(d.pop("active"))

        def _parse_date_created(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_created_type_0 = datetime.datetime.fromisoformat(data)

                return date_created_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        date_created = _parse_date_created(d.pop("date_created"))

        object_storage_iam_user_s3_key = cls(
            s3_key_id=s3_key_id,
            object_storage_id=object_storage_id,
            iam_user_id=iam_user_id,
            access_key=access_key,
            secret_key=secret_key,
            status=status,
            active=active,
            date_created=date_created,
        )

        object_storage_iam_user_s3_key.additional_properties = d
        return object_storage_iam_user_s3_key

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
