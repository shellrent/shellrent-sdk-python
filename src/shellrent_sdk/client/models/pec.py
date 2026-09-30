from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Pec")


@_attrs_define
class Pec:
    pec_id: int
    purchase_id: int | None
    purchase_name: None | str
    purchase_status_code: None | str
    box_name: None | str
    full_box_name: None | str
    domain: None | str
    report_email: None | str
    report_sms: None | str
    password_recovery_email: None | str
    inbox_usage: float | None
    archive_usage: float | None
    extra_inbox: int | None
    extra_archive: int | None
    transfer_in: bool
    owner_not_assignable: bool
    password_wrong: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pec_id = self.pec_id

        purchase_id: int | None
        purchase_id = self.purchase_id

        purchase_name: None | str
        purchase_name = self.purchase_name

        purchase_status_code: None | str
        purchase_status_code = self.purchase_status_code

        box_name: None | str
        box_name = self.box_name

        full_box_name: None | str
        full_box_name = self.full_box_name

        domain: None | str
        domain = self.domain

        report_email: None | str
        report_email = self.report_email

        report_sms: None | str
        report_sms = self.report_sms

        password_recovery_email: None | str
        password_recovery_email = self.password_recovery_email

        inbox_usage: float | None
        inbox_usage = self.inbox_usage

        archive_usage: float | None
        archive_usage = self.archive_usage

        extra_inbox: int | None
        extra_inbox = self.extra_inbox

        extra_archive: int | None
        extra_archive = self.extra_archive

        transfer_in = self.transfer_in

        owner_not_assignable = self.owner_not_assignable

        password_wrong = self.password_wrong

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pec_id": pec_id,
                "purchase_id": purchase_id,
                "purchase_name": purchase_name,
                "purchase_status_code": purchase_status_code,
                "box_name": box_name,
                "full_box_name": full_box_name,
                "domain": domain,
                "report_email": report_email,
                "report_sms": report_sms,
                "password_recovery_email": password_recovery_email,
                "inbox_usage": inbox_usage,
                "archive_usage": archive_usage,
                "extra_inbox": extra_inbox,
                "extra_archive": extra_archive,
                "transfer_in": transfer_in,
                "owner_not_assignable": owner_not_assignable,
                "password_wrong": password_wrong,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        pec_id = d.pop("pec_id")

        def _parse_purchase_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        purchase_id = _parse_purchase_id(d.pop("purchase_id"))

        def _parse_purchase_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        purchase_name = _parse_purchase_name(d.pop("purchase_name"))

        def _parse_purchase_status_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        purchase_status_code = _parse_purchase_status_code(d.pop("purchase_status_code"))

        def _parse_box_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        box_name = _parse_box_name(d.pop("box_name"))

        def _parse_full_box_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        full_box_name = _parse_full_box_name(d.pop("full_box_name"))

        def _parse_domain(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        domain = _parse_domain(d.pop("domain"))

        def _parse_report_email(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        report_email = _parse_report_email(d.pop("report_email"))

        def _parse_report_sms(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        report_sms = _parse_report_sms(d.pop("report_sms"))

        def _parse_password_recovery_email(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        password_recovery_email = _parse_password_recovery_email(d.pop("password_recovery_email"))

        def _parse_inbox_usage(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        inbox_usage = _parse_inbox_usage(d.pop("inbox_usage"))

        def _parse_archive_usage(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        archive_usage = _parse_archive_usage(d.pop("archive_usage"))

        def _parse_extra_inbox(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        extra_inbox = _parse_extra_inbox(d.pop("extra_inbox"))

        def _parse_extra_archive(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        extra_archive = _parse_extra_archive(d.pop("extra_archive"))

        transfer_in = d.pop("transfer_in")

        owner_not_assignable = d.pop("owner_not_assignable")

        password_wrong = d.pop("password_wrong")

        pec = cls(
            pec_id=pec_id,
            purchase_id=purchase_id,
            purchase_name=purchase_name,
            purchase_status_code=purchase_status_code,
            box_name=box_name,
            full_box_name=full_box_name,
            domain=domain,
            report_email=report_email,
            report_sms=report_sms,
            password_recovery_email=password_recovery_email,
            inbox_usage=inbox_usage,
            archive_usage=archive_usage,
            extra_inbox=extra_inbox,
            extra_archive=extra_archive,
            transfer_in=transfer_in,
            owner_not_assignable=owner_not_assignable,
            password_wrong=password_wrong,
        )

        pec.additional_properties = d
        return pec

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
