from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.hosting_ssl_certificate import HostingSslCertificate
    from ..models.hosting_ssl_certificate_list_response_meta_type_0 import (
        HostingSslCertificateListResponseMetaType0,
    )


T = TypeVar("T", bound="HostingSslCertificateListResponse")


@_attrs_define
class HostingSslCertificateListResponse:
    error: int
    message: None | str
    data: list[HostingSslCertificate]
    meta: HostingSslCertificateListResponseMetaType0 | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.hosting_ssl_certificate_list_response_meta_type_0 import (
            HostingSslCertificateListResponseMetaType0,
        )

        error = self.error

        message: None | str
        message = self.message

        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        meta: dict[str, Any] | None
        if isinstance(self.meta, HostingSslCertificateListResponseMetaType0):
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
        from ..models.hosting_ssl_certificate import HostingSslCertificate
        from ..models.hosting_ssl_certificate_list_response_meta_type_0 import (
            HostingSslCertificateListResponseMetaType0,
        )

        d = dict(src_dict)
        error = d.pop("error")

        def _parse_message(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        message = _parse_message(d.pop("message"))

        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = HostingSslCertificate.from_dict(data_item_data)

            data.append(data_item)

        def _parse_meta(data: object) -> HostingSslCertificateListResponseMetaType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                meta_type_0 = HostingSslCertificateListResponseMetaType0.from_dict(data)

                return meta_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(HostingSslCertificateListResponseMetaType0 | None, data)

        meta = _parse_meta(d.pop("meta"))

        hosting_ssl_certificate_list_response = cls(
            error=error,
            message=message,
            data=data,
            meta=meta,
        )

        hosting_ssl_certificate_list_response.additional_properties = d
        return hosting_ssl_certificate_list_response

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
