from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="License")


@_attrs_define
class License:
    """cPanel or Plesk license of the account, with the server or the IP address where it is installed"""

    license_id: int
    purchase_id: int
    """ Id of the purchase of the license (`GET /api/v3/purchases/{purchase_id}`) """
    purchase_server_id: int | None
    """ Id of the purchase of the server where the license is installed (`GET /api/v3/purchases/{purchase_id}`);
    null for a license on an external host (`ip_address`) or without a server """
    service_name: None | str
    """ Name of the service of the purchase, in Italian """
    purchase_name: None | str
    """ Object name of the purchase, as `purchase_name.object_name` of the purchase """
    key_number: None | str
    """ Key number of a Plesk license; null for cPanel licenses """
    ip_address: None | str
    """ IP address of the external host where the license is installed, instead of a server (`purchase_server_id`)
    """
    is_els: bool
    """ Whether the server runs an obsolete operating system, covered by the Extended Lifecycle Support (ELS) of the
    supplier and charged as an additional fee """
    operative_system: None | str
    """ Operating system of the server, as reported by the license supplier; null until reported """
    purchase_status_code: None | str
    """ Status code of the purchase (`status_code` of `PurchaseStatus`): `NEW_V2`, `ACTIVE_V2` or `DELIVERED_V2` """
    date_activation: datetime.date | None
    """ Activation date of the purchase (`date_activation` of the purchase) """
    date_expiry: datetime.date | None
    """ Expiry date of the purchase (`date_expiry` of the purchase) """
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

        license_ = cls(
            license_id=license_id,
            purchase_id=purchase_id,
            purchase_server_id=purchase_server_id,
            service_name=service_name,
            purchase_name=purchase_name,
            key_number=key_number,
            ip_address=ip_address,
            is_els=is_els,
            operative_system=operative_system,
            purchase_status_code=purchase_status_code,
            date_activation=date_activation,
            date_expiry=date_expiry,
        )

        license_.additional_properties = d
        return license_

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
