from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="PurchaseRecurrenceChangeRequest")


@_attrs_define
class PurchaseRecurrenceChangeRequest:
    recurrence_id: int
    """ ID of the recurrence to use on the purchase """

    def to_dict(self) -> dict[str, Any]:
        recurrence_id = self.recurrence_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "recurrence_id": recurrence_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        recurrence_id = d.pop("recurrence_id")

        purchase_recurrence_change_request = cls(
            recurrence_id=recurrence_id,
        )

        return purchase_recurrence_change_request
