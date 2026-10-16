from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.purchase_can_change_recurrence import PurchaseCanChangeRecurrence


T = TypeVar("T", bound="PurchaseCanChangeRecurrenceResponse")


@_attrs_define
class PurchaseCanChangeRecurrenceResponse:
    """Successful response with one `PurchaseCanChangeRecurrence`"""

    error: Literal[0]
    """ Always 0 in a successful response """
    message: None | str
    """ Always null in a successful response """
    data: PurchaseCanChangeRecurrence
    """ Whether the recurrence of the purchase can be changed (`PATCH /api/v3/purchases/{purchase_id}/recurrence`)
    """
    meta: Any
    """ Always null: only the paginated lists have a `meta` """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error = self.error

        message: None | str
        message = self.message

        data = self.data.to_dict()

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
        from ..models.purchase_can_change_recurrence import (
            PurchaseCanChangeRecurrence,
        )

        d = dict(src_dict)
        error = cast(Literal[0], d.pop("error"))
        if error != 0:
            raise ValueError(f"error must match const 0, got '{error}'")

        def _parse_message(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        message = _parse_message(d.pop("message"))

        data = PurchaseCanChangeRecurrence.from_dict(d.pop("data"))

        meta = d.pop("meta")

        purchase_can_change_recurrence_response = cls(
            error=error,
            message=message,
            data=data,
            meta=meta,
        )

        purchase_can_change_recurrence_response.additional_properties = d
        return purchase_can_change_recurrence_response

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
