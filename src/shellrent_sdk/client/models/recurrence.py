from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.recurrence_frequency import RecurrenceFrequency


T = TypeVar("T", bound="Recurrence")


@_attrs_define
class Recurrence:
    recurrence_id: int
    frequency: RecurrenceFrequency
    days_renew: int | None
    days_autorenew: int | None
    days_suspension: int | None
    days_restore: int | None
    days_dismission: int | None
    days_cancel: int
    days_renew_dismission: int | None
    days_no_secondary: int | None
    days_no_service_change: int | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        recurrence_id = self.recurrence_id

        frequency = self.frequency.to_dict()

        days_renew: int | None
        days_renew = self.days_renew

        days_autorenew: int | None
        days_autorenew = self.days_autorenew

        days_suspension: int | None
        days_suspension = self.days_suspension

        days_restore: int | None
        days_restore = self.days_restore

        days_dismission: int | None
        days_dismission = self.days_dismission

        days_cancel = self.days_cancel

        days_renew_dismission: int | None
        days_renew_dismission = self.days_renew_dismission

        days_no_secondary: int | None
        days_no_secondary = self.days_no_secondary

        days_no_service_change: int | None
        days_no_service_change = self.days_no_service_change

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "recurrence_id": recurrence_id,
                "frequency": frequency,
                "days_renew": days_renew,
                "days_autorenew": days_autorenew,
                "days_suspension": days_suspension,
                "days_restore": days_restore,
                "days_dismission": days_dismission,
                "days_cancel": days_cancel,
                "days_renew_dismission": days_renew_dismission,
                "days_no_secondary": days_no_secondary,
                "days_no_service_change": days_no_service_change,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.recurrence_frequency import RecurrenceFrequency

        d = dict(src_dict)
        recurrence_id = d.pop("recurrence_id")

        frequency = RecurrenceFrequency.from_dict(d.pop("frequency"))

        def _parse_days_renew(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        days_renew = _parse_days_renew(d.pop("days_renew"))

        def _parse_days_autorenew(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        days_autorenew = _parse_days_autorenew(d.pop("days_autorenew"))

        def _parse_days_suspension(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        days_suspension = _parse_days_suspension(d.pop("days_suspension"))

        def _parse_days_restore(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        days_restore = _parse_days_restore(d.pop("days_restore"))

        def _parse_days_dismission(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        days_dismission = _parse_days_dismission(d.pop("days_dismission"))

        days_cancel = d.pop("days_cancel")

        def _parse_days_renew_dismission(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        days_renew_dismission = _parse_days_renew_dismission(d.pop("days_renew_dismission"))

        def _parse_days_no_secondary(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        days_no_secondary = _parse_days_no_secondary(d.pop("days_no_secondary"))

        def _parse_days_no_service_change(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        days_no_service_change = _parse_days_no_service_change(d.pop("days_no_service_change"))

        recurrence = cls(
            recurrence_id=recurrence_id,
            frequency=frequency,
            days_renew=days_renew,
            days_autorenew=days_autorenew,
            days_suspension=days_suspension,
            days_restore=days_restore,
            days_dismission=days_dismission,
            days_cancel=days_cancel,
            days_renew_dismission=days_renew_dismission,
            days_no_secondary=days_no_secondary,
            days_no_service_change=days_no_service_change,
        )

        recurrence.additional_properties = d
        return recurrence

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
