from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.service_change import ServiceChange


T = TypeVar("T", bound="PurchaseCanChangeService")


@_attrs_define
class PurchaseCanChangeService:
    purchase_id: int
    can_change_service: bool
    services: list[ServiceChange]
    """ Collection of Services to which it is possible to make the change. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        purchase_id = self.purchase_id

        can_change_service = self.can_change_service

        services = []
        for services_item_data in self.services:
            services_item = services_item_data.to_dict()
            services.append(services_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "purchase_id": purchase_id,
                "can_change_service": can_change_service,
                "services": services,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.service_change import ServiceChange

        d = dict(src_dict)
        purchase_id = d.pop("purchase_id")

        can_change_service = d.pop("can_change_service")

        services = []
        _services = d.pop("services")
        for services_item_data in _services:
            services_item = ServiceChange.from_dict(services_item_data)

            services.append(services_item)

        purchase_can_change_service = cls(
            purchase_id=purchase_id,
            can_change_service=can_change_service,
            services=services,
        )

        purchase_can_change_service.additional_properties = d
        return purchase_can_change_service

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
