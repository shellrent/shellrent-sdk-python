from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RecurrenceFrequency")


@_attrs_define
class RecurrenceFrequency:
    """Frequency of a recurrence: a number of years, months or weeks, or a one-off charge"""

    family: str
    """ Unit of the frequency: `Y` (years), `M` (months), `W` (weeks) or `U` (one-off, without renewals) """
    value: int | None
    """ Number of units of the frequency, for example 12 with `M`; null with `U` """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        family = self.family

        value: int | None
        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "family": family,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        family = d.pop("family")

        def _parse_value(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        value = _parse_value(d.pop("value"))

        recurrence_frequency = cls(
            family=family,
            value=value,
        )

        recurrence_frequency.additional_properties = d
        return recurrence_frequency

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
