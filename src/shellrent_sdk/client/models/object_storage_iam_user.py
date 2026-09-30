from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ObjectStorageIamUser")


@_attrs_define
class ObjectStorageIamUser:
    iam_user_id: int
    object_storage_id: int
    sub_account_id: int
    code: None | str
    code_full: None | str
    iam_id: None | str
    arn: None | str
    active: bool | None
    firewall_policy: None | str
    date_created: datetime.datetime | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        iam_user_id = self.iam_user_id

        object_storage_id = self.object_storage_id

        sub_account_id = self.sub_account_id

        code: None | str
        code = self.code

        code_full: None | str
        code_full = self.code_full

        iam_id: None | str
        iam_id = self.iam_id

        arn: None | str
        arn = self.arn

        active: bool | None
        active = self.active

        firewall_policy: None | str
        firewall_policy = self.firewall_policy

        date_created: None | str
        if isinstance(self.date_created, datetime.datetime):
            date_created = self.date_created.isoformat()
        else:
            date_created = self.date_created

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "iam_user_id": iam_user_id,
                "object_storage_id": object_storage_id,
                "sub_account_id": sub_account_id,
                "code": code,
                "code_full": code_full,
                "iam_id": iam_id,
                "arn": arn,
                "active": active,
                "firewall_policy": firewall_policy,
                "date_created": date_created,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        iam_user_id = d.pop("iam_user_id")

        object_storage_id = d.pop("object_storage_id")

        sub_account_id = d.pop("sub_account_id")

        def _parse_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        code = _parse_code(d.pop("code"))

        def _parse_code_full(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        code_full = _parse_code_full(d.pop("code_full"))

        def _parse_iam_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        iam_id = _parse_iam_id(d.pop("iam_id"))

        def _parse_arn(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        arn = _parse_arn(d.pop("arn"))

        def _parse_active(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        active = _parse_active(d.pop("active"))

        def _parse_firewall_policy(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        firewall_policy = _parse_firewall_policy(d.pop("firewall_policy"))

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

        object_storage_iam_user = cls(
            iam_user_id=iam_user_id,
            object_storage_id=object_storage_id,
            sub_account_id=sub_account_id,
            code=code,
            code_full=code_full,
            iam_id=iam_id,
            arn=arn,
            active=active,
            firewall_policy=firewall_policy,
            date_created=date_created,
        )

        object_storage_iam_user.additional_properties = d
        return object_storage_iam_user

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
