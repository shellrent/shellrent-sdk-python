from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domain_dnssec import DomainDnssec
    from ..models.domain_dnssec_response_meta_type_0 import DomainDnssecResponseMetaType0


T = TypeVar("T", bound="DomainDnssecResponse")


@_attrs_define
class DomainDnssecResponse:
    error: int
    message: None | str
    data: DomainDnssec
    meta: DomainDnssecResponseMetaType0 | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.domain_dnssec_response_meta_type_0 import DomainDnssecResponseMetaType0

        error = self.error

        message: None | str
        message = self.message

        data = self.data.to_dict()

        meta: dict[str, Any] | None
        if isinstance(self.meta, DomainDnssecResponseMetaType0):
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
        from ..models.domain_dnssec import DomainDnssec
        from ..models.domain_dnssec_response_meta_type_0 import (
            DomainDnssecResponseMetaType0,
        )

        d = dict(src_dict)
        error = d.pop("error")

        def _parse_message(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        message = _parse_message(d.pop("message"))

        data = DomainDnssec.from_dict(d.pop("data"))

        def _parse_meta(data: object) -> DomainDnssecResponseMetaType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                meta_type_0 = DomainDnssecResponseMetaType0.from_dict(data)

                return meta_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DomainDnssecResponseMetaType0 | None, data)

        meta = _parse_meta(d.pop("meta"))

        domain_dnssec_response = cls(
            error=error,
            message=message,
            data=data,
            meta=meta,
        )

        domain_dnssec_response.additional_properties = d
        return domain_dnssec_response

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
