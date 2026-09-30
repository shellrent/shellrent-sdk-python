from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="HostingDatabase")


@_attrs_define
class HostingDatabase:
    database_id: str
    name: str
    type_: str
    credential_id: int | None
    username: None | str
    supplier_code: None | str
    table_count: int | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        database_id = self.database_id

        name = self.name

        type_ = self.type_

        credential_id: int | None
        credential_id = self.credential_id

        username: None | str
        username = self.username

        supplier_code: None | str
        supplier_code = self.supplier_code

        table_count: int | None
        table_count = self.table_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "database_id": database_id,
                "name": name,
                "type": type_,
                "credential_id": credential_id,
                "username": username,
                "supplier_code": supplier_code,
                "table_count": table_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        database_id = d.pop("database_id")

        name = d.pop("name")

        type_ = d.pop("type")

        def _parse_credential_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        credential_id = _parse_credential_id(d.pop("credential_id"))

        def _parse_username(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        username = _parse_username(d.pop("username"))

        def _parse_supplier_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        supplier_code = _parse_supplier_code(d.pop("supplier_code"))

        def _parse_table_count(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        table_count = _parse_table_count(d.pop("table_count"))

        hosting_database = cls(
            database_id=database_id,
            name=name,
            type_=type_,
            credential_id=credential_id,
            username=username,
            supplier_code=supplier_code,
            table_count=table_count,
        )

        hosting_database.additional_properties = d
        return hosting_database

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
