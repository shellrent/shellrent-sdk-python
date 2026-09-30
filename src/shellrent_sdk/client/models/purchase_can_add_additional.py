from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.service import Service


T = TypeVar("T", bound="PurchaseCanAddAdditional")


@_attrs_define
class PurchaseCanAddAdditional:
    purchase_id: int
    can_add_additional: bool
    services: list[Service]
    """ Collection of Services to which it is possible to make the change. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        purchase_id = self.purchase_id

        can_add_additional = self.can_add_additional

        services = []
        for services_item_data in self.services:
            services_item = services_item_data.to_dict()
            services.append(services_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "purchase_id": purchase_id,
                "can_add_additional": can_add_additional,
                "services": services,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.service import Service

        d = dict(src_dict)
        purchase_id = d.pop("purchase_id")

        can_add_additional = d.pop("can_add_additional")

        services = []
        _services = d.pop("services")
        for services_item_data in _services:
            services_item = Service.from_dict(services_item_data)

            services.append(services_item)

        purchase_can_add_additional = cls(
            purchase_id=purchase_id,
            can_add_additional=can_add_additional,
            services=services,
        )

        purchase_can_add_additional.additional_properties = d
        return purchase_can_add_additional

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
