from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.hosting_antivirus_scan import HostingAntivirusScan
    from ..models.pagination_meta import PaginationMeta


T = TypeVar("T", bound="HostingAntivirusScanPaginatedListResponse")


@_attrs_define
class HostingAntivirusScanPaginatedListResponse:
    error: int
    message: None | str
    data: list[HostingAntivirusScan]
    meta: PaginationMeta
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error = self.error

        message: None | str
        message = self.message

        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        meta = self.meta.to_dict()

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
        from ..models.hosting_antivirus_scan import HostingAntivirusScan
        from ..models.pagination_meta import PaginationMeta

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
            data_item = HostingAntivirusScan.from_dict(data_item_data)

            data.append(data_item)

        meta = PaginationMeta.from_dict(d.pop("meta"))

        hosting_antivirus_scan_paginated_list_response = cls(
            error=error,
            message=message,
            data=data,
            meta=meta,
        )

        hosting_antivirus_scan_paginated_list_response.additional_properties = d
        return hosting_antivirus_scan_paginated_list_response

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
