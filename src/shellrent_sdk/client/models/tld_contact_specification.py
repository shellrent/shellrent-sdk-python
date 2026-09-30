from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TldContactSpecification")


@_attrs_define
class TldContactSpecification:
    """Represents a single TLD contact specification"""

    name: str
    """ Code of the contact specification """
    type_: str
    """ Data type of the specification value """
    enum: list[str] | None
    """ If not null, the list of allowed values for this specification """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_ = self.type_

        enum: list[str] | None
        if isinstance(self.enum, list):
            enum = self.enum

        else:
            enum = self.enum

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "type": type_,
                "enum": enum,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name")

        type_ = d.pop("type")

        def _parse_enum(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                enum_type_0 = cast(list[str], data)

                return enum_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        enum = _parse_enum(d.pop("enum"))

        tld_contact_specification = cls(
            name=name,
            type_=type_,
            enum=enum,
        )

        tld_contact_specification.additional_properties = d
        return tld_contact_specification

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
