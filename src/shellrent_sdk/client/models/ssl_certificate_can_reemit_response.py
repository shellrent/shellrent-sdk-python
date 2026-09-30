from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.ssl_certificate_can_reemit import SslCertificateCanReemit
    from ..models.ssl_certificate_can_reemit_response_meta_type_0 import (
        SslCertificateCanReemitResponseMetaType0,
    )


T = TypeVar("T", bound="SslCertificateCanReemitResponse")


@_attrs_define
class SslCertificateCanReemitResponse:
    error: int
    message: None | str
    data: SslCertificateCanReemit
    meta: None | SslCertificateCanReemitResponseMetaType0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.ssl_certificate_can_reemit_response_meta_type_0 import (
            SslCertificateCanReemitResponseMetaType0,
        )

        error = self.error

        message: None | str
        message = self.message

        data = self.data.to_dict()

        meta: dict[str, Any] | None
        if isinstance(self.meta, SslCertificateCanReemitResponseMetaType0):
            meta = self.meta.to_dict()
        else:
            meta = self.meta

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "error": error,
                "message": message,
                "data": data,
                "meta": meta,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ssl_certificate_can_reemit import SslCertificateCanReemit
        from ..models.ssl_certificate_can_reemit_response_meta_type_0 import (
            SslCertificateCanReemitResponseMetaType0,
        )

        d = dict(src_dict)
        error = d.pop("error")

        def _parse_message(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        message = _parse_message(d.pop("message"))

        data = SslCertificateCanReemit.from_dict(d.pop("data"))

        def _parse_meta(data: object) -> None | SslCertificateCanReemitResponseMetaType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                meta_type_0 = SslCertificateCanReemitResponseMetaType0.from_dict(data)

                return meta_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SslCertificateCanReemitResponseMetaType0, data)

        meta = _parse_meta(d.pop("meta"))

        ssl_certificate_can_reemit_response = cls(
            error=error,
            message=message,
            data=data,
            meta=meta,
        )

        ssl_certificate_can_reemit_response.additional_properties = d
        return ssl_certificate_can_reemit_response

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
