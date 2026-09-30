from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SslCertificateKeys")


@_attrs_define
class SslCertificateKeys:
    ssl_certificate_id: int
    csr: None | str
    private_key: None | str
    public_key: None | str
    certificate_authority: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ssl_certificate_id = self.ssl_certificate_id

        csr: None | str
        csr = self.csr

        private_key: None | str
        private_key = self.private_key

        public_key: None | str
        public_key = self.public_key

        certificate_authority: None | str
        certificate_authority = self.certificate_authority

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ssl_certificate_id": ssl_certificate_id,
                "csr": csr,
                "private_key": private_key,
                "public_key": public_key,
                "certificate_authority": certificate_authority,
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

        def _parse_private_key(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        private_key = _parse_private_key(d.pop("private_key"))

        def _parse_public_key(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        public_key = _parse_public_key(d.pop("public_key"))

        def _parse_certificate_authority(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        certificate_authority = _parse_certificate_authority(d.pop("certificate_authority"))

        ssl_certificate_keys = cls(
            ssl_certificate_id=ssl_certificate_id,
            csr=csr,
            private_key=private_key,
            public_key=public_key,
            certificate_authority=certificate_authority,
        )

        ssl_certificate_keys.additional_properties = d
        return ssl_certificate_keys

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
