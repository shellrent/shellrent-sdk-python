from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SslCertificateReemitRequest")


@_attrs_define
class SslCertificateReemitRequest:
    private_key: None | str | Unset = UNSET
    csr_key: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        private_key: None | str | Unset
        if isinstance(self.private_key, Unset):
            private_key = UNSET
        else:
            private_key = self.private_key

        csr_key: None | str | Unset
        if isinstance(self.csr_key, Unset):
            csr_key = UNSET
        else:
            csr_key = self.csr_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if private_key is not UNSET:
            field_dict["private_key"] = private_key
        if csr_key is not UNSET:
            field_dict["csr_key"] = csr_key

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_private_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        private_key = _parse_private_key(d.pop("private_key", UNSET))

        def _parse_csr_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        csr_key = _parse_csr_key(d.pop("csr_key", UNSET))

        ssl_certificate_reemit_request = cls(
            private_key=private_key,
            csr_key=csr_key,
        )

        ssl_certificate_reemit_request.additional_properties = d
        return ssl_certificate_reemit_request

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
