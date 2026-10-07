from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.sms_can_cancel import SmsCanCancel
    from ..models.sms_can_cancel_response_meta_type_0 import SmsCanCancelResponseMetaType0


T = TypeVar("T", bound="SmsCanCancelResponse")


@_attrs_define
class SmsCanCancelResponse:
    """Successful response with one `SmsCanCancel`"""

    error: Literal[0]
    """ Always 0 in a successful response """
    message: None | str
    """ Always null in a successful response """
    data: SmsCanCancel
    """ Whether the sending of an SMS can be cancelled (`POST /api/v3/sms/{sms_id}/cancellation`) """
    meta: None | SmsCanCancelResponseMetaType0
    """ Always null: only the paginated lists have a `meta` """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.sms_can_cancel_response_meta_type_0 import SmsCanCancelResponseMetaType0

        error = self.error

        message: None | str
        message = self.message

        data = self.data.to_dict()

        meta: dict[str, Any] | None
        if isinstance(self.meta, SmsCanCancelResponseMetaType0):
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
        from ..models.sms_can_cancel import SmsCanCancel
        from ..models.sms_can_cancel_response_meta_type_0 import (
            SmsCanCancelResponseMetaType0,
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

        data = SmsCanCancel.from_dict(d.pop("data"))

        def _parse_meta(data: object) -> None | SmsCanCancelResponseMetaType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                meta_type_0 = SmsCanCancelResponseMetaType0.from_dict(data)

                return meta_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SmsCanCancelResponseMetaType0, data)

        meta = _parse_meta(d.pop("meta"))

        sms_can_cancel_response = cls(
            error=error,
            message=message,
            data=data,
            meta=meta,
        )

        sms_can_cancel_response.additional_properties = d
        return sms_can_cancel_response

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
