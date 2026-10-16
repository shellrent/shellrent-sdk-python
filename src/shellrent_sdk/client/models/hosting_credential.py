from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="HostingCredential")


@_attrs_define
class HostingCredential:
    """Active FTP or database account of the hosting, with its password"""

    credential_id: int
    type_: str
    """ Type of the account: `FTP` (main FTP account), `FTP_SECONDARY` (additional FTP account), `DATABASE_MYSQL` or
    `DATABASE_MSSQL` (database account) """
    username: str
    password: str
    """ Password of the account, in clear text, as in the control panel: a temporary random one while the account is
    suspended """
    root_path: None | str
    """ Root directory of an `FTP_SECONDARY` account; null for the other accounts """
    is_active: bool
    """ Whether the account is active """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        credential_id = self.credential_id

        type_ = self.type_

        username = self.username

        password = self.password

        root_path: None | str
        root_path = self.root_path

        is_active = self.is_active

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "credential_id": credential_id,
                "type": type_,
                "username": username,
                "password": password,
                "root_path": root_path,
                "is_active": is_active,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        credential_id = d.pop("credential_id")

        type_ = d.pop("type")

        username = d.pop("username")

        password = d.pop("password")

        def _parse_root_path(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        root_path = _parse_root_path(d.pop("root_path"))

        is_active = d.pop("is_active")

        hosting_credential = cls(
            credential_id=credential_id,
            type_=type_,
            username=username,
            password=password,
            root_path=root_path,
            is_active=is_active,
        )

        hosting_credential.additional_properties = d
        return hosting_credential

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
