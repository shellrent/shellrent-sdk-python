from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SslCertificateKey")


@_attrs_define
class SslCertificateKey:
    ssl_certificate_id: int
    csr: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ssl_certificate_id = self.ssl_certificate_id

        csr: None | str
        csr = self.csr

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ssl_certificate_id": ssl_certificate_id,
                "csr": csr,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        ssl_certificate_id = d.pop("ssl_certificate_id")

        def _parse_csr(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        csr = _parse_csr(d.pop("csr"))

        ssl_certificate_key = cls(
            ssl_certificate_id=ssl_certificate_id,
            csr=csr,
        )

        ssl_certificate_key.additional_properties = d
        return ssl_certificate_key

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
