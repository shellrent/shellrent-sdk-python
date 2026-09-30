from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CpanelLicense")


@_attrs_define
class CpanelLicense:
    license_id: int
    purchase_id: int
    purchase_server_id: int | None
    service_name: None | str
    purchase_name: None | str
    license_ref: None | str
    key_number: None | str
    ip_address: None | str
    is_els: bool
    operative_system: None | str
    purchase_status_code: None | str
    date_activation: datetime.date | None
    date_expiry: datetime.date | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        license_id = self.license_id

        purchase_id = self.purchase_id

        purchase_server_id: int | None
        purchase_server_id = self.purchase_server_id

        service_name: None | str
        service_name = self.service_name

        purchase_name: None | str
        purchase_name = self.purchase_name

        license_ref: None | str
        license_ref = self.license_ref

        key_number: None | str
        key_number = self.key_number

        ip_address: None | str
        ip_address = self.ip_address

        is_els = self.is_els

        operative_system: None | str
        operative_system = self.operative_system

        purchase_status_code: None | str
        purchase_status_code = self.purchase_status_code

        date_activation: None | str
        if isinstance(self.date_activation, datetime.date):
            date_activation = self.date_activation.isoformat()
        else:
            date_activation = self.date_activation

        date_expiry: None | str
        if isinstance(self.date_expiry, datetime.date):
            date_expiry = self.date_expiry.isoformat()
        else:
            date_expiry = self.date_expiry

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "license_id": license_id,
                "purchase_id": purchase_id,
                "purchase_server_id": purchase_server_id,
                "service_name": service_name,
                "purchase_name": purchase_name,
                "license_ref": license_ref,
                "key_number": key_number,
                "ip_address": ip_address,
                "is_els": is_els,
                "operative_system": operative_system,
                "purchase_status_code": purchase_status_code,
                "date_activation": date_activation,
                "date_expiry": date_expiry,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        license_id = d.pop("license_id")

        purchase_id = d.pop("purchase_id")

        def _parse_purchase_server_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        purchase_server_id = _parse_purchase_server_id(d.pop("purchase_server_id"))

        def _parse_service_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        service_name = _parse_service_name(d.pop("service_name"))

        def _parse_purchase_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        purchase_name = _parse_purchase_name(d.pop("purchase_name"))

        def _parse_license_ref(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        license_ref = _parse_license_ref(d.pop("license_ref"))

        def _parse_key_number(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        key_number = _parse_key_number(d.pop("key_number"))

        def _parse_ip_address(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        ip_address = _parse_ip_address(d.pop("ip_address"))

        is_els = d.pop("is_els")

        def _parse_operative_system(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        operative_system = _parse_operative_system(d.pop("operative_system"))

        def _parse_purchase_status_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        purchase_status_code = _parse_purchase_status_code(d.pop("purchase_status_code"))

        def _parse_date_activation(data: object) -> datetime.date | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_activation_type_0 = datetime.date.fromisoformat(data)

                return date_activation_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None, data)

        date_activation = _parse_date_activation(d.pop("date_activation"))

        def _parse_date_expiry(data: object) -> datetime.date | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_expiry_type_0 = datetime.date.fromisoformat(data)

                return date_expiry_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None, data)

        date_expiry = _parse_date_expiry(d.pop("date_expiry"))

        cpanel_license = cls(
            license_id=license_id,
            purchase_id=purchase_id,
            purchase_server_id=purchase_server_id,
            service_name=service_name,
            purchase_name=purchase_name,
            license_ref=license_ref,
            key_number=key_number,
            ip_address=ip_address,
            is_els=is_els,
            operative_system=operative_system,
            purchase_status_code=purchase_status_code,
            date_activation=date_activation,
            date_expiry=date_expiry,
        )

        cpanel_license.additional_properties = d
        return cpanel_license

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
