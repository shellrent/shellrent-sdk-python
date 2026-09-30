from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.api_error_data_type_0 import ApiErrorDataType0
    from ..models.api_error_meta_type_0 import ApiErrorMetaType0


T = TypeVar("T", bound="ApiError")


@_attrs_define
class ApiError:
    error: int
    """ Codice d'errore maggiore di zero """
    message: str
    data: ApiErrorDataType0 | None
    """ Null nelle risposte d'errore """
    meta: ApiErrorMetaType0 | None
    """ Null nelle risposte d'errore """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_error_data_type_0 import ApiErrorDataType0
        from ..models.api_error_meta_type_0 import ApiErrorMetaType0

        error = self.error

        message = self.message

        data: dict[str, Any] | None
        if isinstance(self.data, ApiErrorDataType0):
            data = self.data.to_dict()
        else:
            data = self.data

        meta: dict[str, Any] | None
        if isinstance(self.meta, ApiErrorMetaType0):
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
        from ..models.api_error_data_type_0 import ApiErrorDataType0
        from ..models.api_error_meta_type_0 import ApiErrorMetaType0

        d = dict(src_dict)
        error = d.pop("error")

        message = d.pop("message")

        def _parse_data(data: object) -> ApiErrorDataType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_0 = ApiErrorDataType0.from_dict(data)

                return data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ApiErrorDataType0 | None, data)

        data = _parse_data(d.pop("data"))

        def _parse_meta(data: object) -> ApiErrorMetaType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                meta_type_0 = ApiErrorMetaType0.from_dict(data)

                return meta_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ApiErrorMetaType0 | None, data)

        meta = _parse_meta(d.pop("meta"))

        api_error = cls(
            error=error,
            message=message,
            data=data,
            meta=meta,
        )

        api_error.additional_properties = d
        return api_error

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
