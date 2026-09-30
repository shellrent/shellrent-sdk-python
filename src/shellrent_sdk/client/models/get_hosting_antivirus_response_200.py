from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_hosting_antivirus_response_200_meta_type_0 import (
        GetHostingAntivirusResponse200MetaType0,
    )
    from ..models.hosting_antivirus import HostingAntivirus


T = TypeVar("T", bound="GetHostingAntivirusResponse200")


@_attrs_define
class GetHostingAntivirusResponse200:
    error: int
    message: None | str
    data: HostingAntivirus | None
    meta: GetHostingAntivirusResponse200MetaType0 | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_hosting_antivirus_response_200_meta_type_0 import (
            GetHostingAntivirusResponse200MetaType0,
        )
        from ..models.hosting_antivirus import HostingAntivirus

        error = self.error

        message: None | str
        message = self.message

        data: dict[str, Any] | None
        if isinstance(self.data, HostingAntivirus):
            data = self.data.to_dict()
        else:
            data = self.data

        meta: dict[str, Any] | None
        if isinstance(self.meta, GetHostingAntivirusResponse200MetaType0):
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
        from ..models.get_hosting_antivirus_response_200_meta_type_0 import (
            GetHostingAntivirusResponse200MetaType0,
        )
        from ..models.hosting_antivirus import HostingAntivirus

        d = dict(src_dict)
        error = d.pop("error")

        def _parse_message(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        message = _parse_message(d.pop("message"))

        def _parse_data(data: object) -> HostingAntivirus | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_0 = HostingAntivirus.from_dict(data)

                return data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(HostingAntivirus | None, data)

        data = _parse_data(d.pop("data"))

        def _parse_meta(data: object) -> GetHostingAntivirusResponse200MetaType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                meta_type_0 = GetHostingAntivirusResponse200MetaType0.from_dict(data)

                return meta_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetHostingAntivirusResponse200MetaType0 | None, data)

        meta = _parse_meta(d.pop("meta"))

        get_hosting_antivirus_response_200 = cls(
            error=error,
            message=message,
            data=data,
            meta=meta,
        )

        get_hosting_antivirus_response_200.additional_properties = d
        return get_hosting_antivirus_response_200

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
