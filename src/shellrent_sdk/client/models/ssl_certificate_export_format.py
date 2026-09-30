from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SslCertificateExportFormat")


@_attrs_define
class SslCertificateExportFormat:
    format_: str
    name: str
    description: None | str
    filename: str
    available: bool
    requires_passphrase: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        format_ = self.format_

        name = self.name

        description: None | str
        description = self.description

        filename = self.filename

        available = self.available

        requires_passphrase = self.requires_passphrase

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "format": format_,
                "name": name,
                "description": description,
                "filename": filename,
                "available": available,
                "requires_passphrase": requires_passphrase,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        format_ = d.pop("format")

        name = d.pop("name")

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        filename = d.pop("filename")

        available = d.pop("available")

        requires_passphrase = d.pop("requires_passphrase")

        ssl_certificate_export_format = cls(
            format_=format_,
            name=name,
            description=description,
            filename=filename,
            available=available,
            requires_passphrase=requires_passphrase,
        )

        ssl_certificate_export_format.additional_properties = d
        return ssl_certificate_export_format

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
