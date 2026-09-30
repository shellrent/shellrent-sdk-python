from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Sms")


@_attrs_define
class Sms:
    id: int
    quality: str
    status: str
    sender: None | str
    message: None | str
    send_from: datetime.datetime | None
    date_approved: datetime.datetime | None
    stop_date: datetime.datetime | None
    sms_count: int | None
    date_created: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        quality = self.quality

        status = self.status

        sender: None | str
        sender = self.sender

        message: None | str
        message = self.message

        send_from: None | str
        if isinstance(self.send_from, datetime.datetime):
            send_from = self.send_from.isoformat()
        else:
            send_from = self.send_from

        date_approved: None | str
        if isinstance(self.date_approved, datetime.datetime):
            date_approved = self.date_approved.isoformat()
        else:
            date_approved = self.date_approved

        stop_date: None | str
        if isinstance(self.stop_date, datetime.datetime):
            stop_date = self.stop_date.isoformat()
        else:
            stop_date = self.stop_date

        sms_count: int | None
        sms_count = self.sms_count

        date_created = self.date_created.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "quality": quality,
                "status": status,
                "sender": sender,
                "message": message,
                "send_from": send_from,
                "date_approved": date_approved,
                "stop_date": stop_date,
                "sms_count": sms_count,
                "date_created": date_created,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        quality = d.pop("quality")

        status = d.pop("status")

        def _parse_sender(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        sender = _parse_sender(d.pop("sender"))

        def _parse_message(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        message = _parse_message(d.pop("message"))

        def _parse_send_from(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                send_from_type_0 = datetime.datetime.fromisoformat(data)

                return send_from_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        send_from = _parse_send_from(d.pop("send_from"))

        def _parse_date_approved(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_approved_type_0 = datetime.datetime.fromisoformat(data)

                return date_approved_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        date_approved = _parse_date_approved(d.pop("date_approved"))

        def _parse_stop_date(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                stop_date_type_0 = datetime.datetime.fromisoformat(data)

                return stop_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        stop_date = _parse_stop_date(d.pop("stop_date"))

        def _parse_sms_count(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        sms_count = _parse_sms_count(d.pop("sms_count"))

        date_created = datetime.datetime.fromisoformat(d.pop("date_created"))

        sms = cls(
            id=id,
            quality=quality,
            status=status,
            sender=sender,
            message=message,
            send_from=send_from,
            date_approved=date_approved,
            stop_date=stop_date,
            sms_count=sms_count,
            date_created=date_created,
        )

        sms.additional_properties = d
        return sms

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
