from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SimplePaginationMeta")


@_attrs_define
class SimplePaginationMeta:
    count: int
    page: int
    per_page: int
    next_: bool
    """ Tells if there is another page after this one """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        page = self.page

        per_page = self.per_page

        next_ = self.next_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "count": count,
                "page": page,
                "per_page": per_page,
                "next": next_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        count = d.pop("count")

        page = d.pop("page")

        per_page = d.pop("per_page")

        next_ = d.pop("next")

        simple_pagination_meta = cls(
            count=count,
            page=page,
            per_page=per_page,
            next_=next_,
        )

        simple_pagination_meta.additional_properties = d
        return simple_pagination_meta

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
