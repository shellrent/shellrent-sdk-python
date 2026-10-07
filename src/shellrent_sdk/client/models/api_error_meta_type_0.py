from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_error_meta_type_0_errors import ApiErrorMetaType0Errors


T = TypeVar("T", bound="ApiErrorMetaType0")


@_attrs_define
class ApiErrorMetaType0:
    """Null, except in validation errors (HTTP 400 with error 1000), where it contains `errors`"""

    errors: ApiErrorMetaType0Errors | Unset = UNSET
    """ Errors for each field: path of the field (e.g. cpu, configuration.ram, ids[3]) => messages """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        errors: dict[str, Any] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = self.errors.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.api_error_meta_type_0_errors import ApiErrorMetaType0Errors

        d = dict(src_dict)
        _errors = d.pop("errors", UNSET)
        errors: ApiErrorMetaType0Errors | Unset
        if isinstance(_errors, Unset):
            errors = UNSET
        else:
            errors = ApiErrorMetaType0Errors.from_dict(_errors)

        api_error_meta_type_0 = cls(
            errors=errors,
        )

        api_error_meta_type_0.additional_properties = d
        return api_error_meta_type_0

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
