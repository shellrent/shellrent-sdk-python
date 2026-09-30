from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sms_create_request_quality import SmsCreateRequestQuality
from ..types import UNSET, Unset

T = TypeVar("T", bound="SmsCreateRequest")


@_attrs_define
class SmsCreateRequest:
    """Sends an SMS. Recipients: provide exactly one of phone_numbers or phonebooks, not both. Sender: required when
    quality is PREMIUM (from 2 to 11 characters), ignored when quality is STANDARD.

    """

    message: str
    """ Text of the SMS you want to send. It can contain emojis, but keep in mind that emojis take up more
    characters. GSM-7: max 160 chars (153 per part if concatenated). Unicode (UCS-2): max 70 chars (67 per part if
    concatenated). """
    quality: SmsCreateRequestQuality
    """ SMS delivery quality. PREMIUM requires sender. """
    phone_numbers: list[str] | Unset = UNSET
    """ SMS recipients (mutually exclusive). Provide exactly one of: "phone_numbers" or "phonebooks". Collection of
    one or more phone numbers in international format using the "00" prefix (digits only, no spaces/separators).
    Example: 00393331122444. """
    phonebooks: list[int] | Unset = UNSET
    """ SMS recipients (mutually exclusive). Provide exactly one of: "phone_numbers" or "phonebooks". Collection of
    one or more phonebook IDs. """
    sender: str | Unset = UNSET
    """ Sender name, from 2 to 11 characters. Required when quality is PREMIUM, ignored when quality is STANDARD.
    """
    send_date: datetime.datetime | Unset = UNSET
    """ Date and time from which to send the SMS. If not specified, the SMS is sent immediately. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        quality = self.quality.value

        phone_numbers: list[str] | Unset = UNSET
        if not isinstance(self.phone_numbers, Unset):
            phone_numbers = self.phone_numbers

        phonebooks: list[int] | Unset = UNSET
        if not isinstance(self.phonebooks, Unset):
            phonebooks = self.phonebooks

        sender = self.sender

        send_date: str | Unset = UNSET
        if not isinstance(self.send_date, Unset):
            send_date = self.send_date.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "message": message,
                "quality": quality,
            }
        )
        if phone_numbers is not UNSET:
            field_dict["phone_numbers"] = phone_numbers
        if phonebooks is not UNSET:
            field_dict["phonebooks"] = phonebooks
        if sender is not UNSET:
            field_dict["sender"] = sender
        if send_date is not UNSET:
            field_dict["send_date"] = send_date

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        message = d.pop("message")

        quality = SmsCreateRequestQuality(d.pop("quality"))

        phone_numbers = cast(list[str], d.pop("phone_numbers", UNSET))

        phonebooks = cast(list[int], d.pop("phonebooks", UNSET))

        sender = d.pop("sender", UNSET)

        _send_date = d.pop("send_date", UNSET)
        send_date: datetime.datetime | Unset
        if isinstance(_send_date, Unset):
            send_date = UNSET
        else:
            send_date = datetime.datetime.fromisoformat(_send_date)

        sms_create_request = cls(
            message=message,
            quality=quality,
            phone_numbers=phone_numbers,
            phonebooks=phonebooks,
            sender=sender,
            send_date=send_date,
        )

        sms_create_request.additional_properties = d
        return sms_create_request

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
