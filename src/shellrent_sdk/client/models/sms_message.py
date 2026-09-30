from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sms_price import SmsPrice


T = TypeVar("T", bound="SmsMessage")


@_attrs_define
class SmsMessage:
    id: int
    sms_id: int
    contact_name: None | str
    phone_number: str
    date_sent: datetime.datetime | None
    date_delivered: datetime.datetime | None
    error: None | str
    """ Error code if the SMS was not delivered """
    sms_price: SmsPrice | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        sms_id = self.sms_id

        contact_name: None | str
        contact_name = self.contact_name

        phone_number = self.phone_number

        date_sent: None | str
        if isinstance(self.date_sent, datetime.datetime):
            date_sent = self.date_sent.isoformat()
        else:
            date_sent = self.date_sent

        date_delivered: None | str
        if isinstance(self.date_delivered, datetime.datetime):
            date_delivered = self.date_delivered.isoformat()
        else:
            date_delivered = self.date_delivered

        error: None | str
        error = self.error

        sms_price: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sms_price, Unset):
            sms_price = self.sms_price.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "sms_id": sms_id,
                "contact_name": contact_name,
                "phone_number": phone_number,
                "date_sent": date_sent,
                "date_delivered": date_delivered,
                "error": error,
            }
        )
        if sms_price is not UNSET:
            field_dict["sms_price"] = sms_price

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.sms_price import SmsPrice

        d = dict(src_dict)
        id = d.pop("id")

        sms_id = d.pop("sms_id")

        def _parse_contact_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        contact_name = _parse_contact_name(d.pop("contact_name"))

        phone_number = d.pop("phone_number")

        def _parse_date_sent(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_sent_type_0 = datetime.datetime.fromisoformat(data)

                return date_sent_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        date_sent = _parse_date_sent(d.pop("date_sent"))

        def _parse_date_delivered(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_delivered_type_0 = datetime.datetime.fromisoformat(data)

                return date_delivered_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        date_delivered = _parse_date_delivered(d.pop("date_delivered"))

        def _parse_error(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        error = _parse_error(d.pop("error"))

        _sms_price = d.pop("sms_price", UNSET)
        sms_price: SmsPrice | Unset
        if isinstance(_sms_price, Unset):
            sms_price = UNSET
        else:
            sms_price = SmsPrice.from_dict(_sms_price)

        sms_message = cls(
            id=id,
            sms_id=sms_id,
            contact_name=contact_name,
            phone_number=phone_number,
            date_sent=date_sent,
            date_delivered=date_delivered,
            error=error,
            sms_price=sms_price,
        )

        sms_message.additional_properties = d
        return sms_message

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
