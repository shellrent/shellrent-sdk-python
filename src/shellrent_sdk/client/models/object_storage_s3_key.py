from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ObjectStorageS3Key")


@_attrs_define
class ObjectStorageS3Key:
    object_storage_id: int
    sub_account_id: int
    username: None | str
    user_id: None | str
    arn: None | str
    access_key: None | str
    secret_key: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_storage_id = self.object_storage_id

        sub_account_id = self.sub_account_id

        username: None | str
        username = self.username

        user_id: None | str
        user_id = self.user_id

        arn: None | str
        arn = self.arn

        access_key: None | str
        access_key = self.access_key

        secret_key: None | str
        secret_key = self.secret_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "object_storage_id": object_storage_id,
                "sub_account_id": sub_account_id,
                "username": username,
                "user_id": user_id,
                "arn": arn,
                "access_key": access_key,
                "secret_key": secret_key,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        object_storage_id = d.pop("object_storage_id")

        sub_account_id = d.pop("sub_account_id")

        def _parse_username(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        username = _parse_username(d.pop("username"))

        def _parse_user_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        user_id = _parse_user_id(d.pop("user_id"))

        def _parse_arn(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        arn = _parse_arn(d.pop("arn"))

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

        object_storage_s3_key = cls(
            object_storage_id=object_storage_id,
            sub_account_id=sub_account_id,
            username=username,
            user_id=user_id,
            arn=arn,
            access_key=access_key,
            secret_key=secret_key,
        )

        object_storage_s3_key.additional_properties = d
        return object_storage_s3_key

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
