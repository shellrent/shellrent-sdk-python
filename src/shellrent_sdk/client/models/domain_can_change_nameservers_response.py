from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domain_can_change_nameservers import DomainCanChangeNameservers
    from ..models.domain_can_change_nameservers_response_meta_type_0 import (
        DomainCanChangeNameserversResponseMetaType0,
    )


T = TypeVar("T", bound="DomainCanChangeNameserversResponse")


@_attrs_define
class DomainCanChangeNameserversResponse:
    error: int
    message: None | str
    data: DomainCanChangeNameservers
    meta: DomainCanChangeNameserversResponseMetaType0 | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.domain_can_change_nameservers_response_meta_type_0 import (
            DomainCanChangeNameserversResponseMetaType0,
        )

        error = self.error

        message: None | str
        message = self.message

        data = self.data.to_dict()

        meta: dict[str, Any] | None
        if isinstance(self.meta, DomainCanChangeNameserversResponseMetaType0):
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
        from ..models.domain_can_change_nameservers import (
            DomainCanChangeNameservers,
        )
        from ..models.domain_can_change_nameservers_response_meta_type_0 import (
            DomainCanChangeNameserversResponseMetaType0,
        )

        d = dict(src_dict)
        error = d.pop("error")

        def _parse_message(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        message = _parse_message(d.pop("message"))

        data = DomainCanChangeNameservers.from_dict(d.pop("data"))

        def _parse_meta(data: object) -> DomainCanChangeNameserversResponseMetaType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                meta_type_0 = DomainCanChangeNameserversResponseMetaType0.from_dict(data)

                return meta_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DomainCanChangeNameserversResponseMetaType0 | None, data)

        meta = _parse_meta(d.pop("meta"))

        domain_can_change_nameservers_response = cls(
            error=error,
            message=message,
            data=data,
            meta=meta,
        )

        domain_can_change_nameservers_response.additional_properties = d
        return domain_can_change_nameservers_response

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
