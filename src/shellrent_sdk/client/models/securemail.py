from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Securemail")


@_attrs_define
class Securemail:
    securemail_id: int
    purchase_id: int
    service_name: None | str
    purchase_name: None | str
    purchase_status_code: None | str
    quantity: int | None
    domain: None | str
    relay_to: None | str
    relay_to_port: int | None
    is_feasible: bool
    provider: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        securemail_id = self.securemail_id

        purchase_id = self.purchase_id

        service_name: None | str
        service_name = self.service_name

        purchase_name: None | str
        purchase_name = self.purchase_name

        purchase_status_code: None | str
        purchase_status_code = self.purchase_status_code

        quantity: int | None
        quantity = self.quantity

        domain: None | str
        domain = self.domain

        relay_to: None | str
        relay_to = self.relay_to

        relay_to_port: int | None
        relay_to_port = self.relay_to_port

        is_feasible = self.is_feasible

        provider = self.provider

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "securemail_id": securemail_id,
                "purchase_id": purchase_id,
                "service_name": service_name,
                "purchase_name": purchase_name,
                "purchase_status_code": purchase_status_code,
                "quantity": quantity,
                "domain": domain,
                "relay_to": relay_to,
                "relay_to_port": relay_to_port,
                "is_feasible": is_feasible,
                "provider": provider,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        securemail_id = d.pop("securemail_id")

        purchase_id = d.pop("purchase_id")

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

        def _parse_purchase_status_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        purchase_status_code = _parse_purchase_status_code(d.pop("purchase_status_code"))

        def _parse_quantity(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        quantity = _parse_quantity(d.pop("quantity"))

        def _parse_domain(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        domain = _parse_domain(d.pop("domain"))

        def _parse_relay_to(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        relay_to = _parse_relay_to(d.pop("relay_to"))

        def _parse_relay_to_port(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        relay_to_port = _parse_relay_to_port(d.pop("relay_to_port"))

        is_feasible = d.pop("is_feasible")

        provider = d.pop("provider")

        securemail = cls(
            securemail_id=securemail_id,
            purchase_id=purchase_id,
            service_name=service_name,
            purchase_name=purchase_name,
            purchase_status_code=purchase_status_code,
            quantity=quantity,
            domain=domain,
            relay_to=relay_to,
            relay_to_port=relay_to_port,
            is_feasible=is_feasible,
            provider=provider,
        )

        securemail.additional_properties = d
        return securemail

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
