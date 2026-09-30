from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.amount import Amount
    from ..models.recurrence import Recurrence
    from ..models.service_category import ServiceCategory


T = TypeVar("T", bound="Service")


@_attrs_define
class Service:
    service_id: int
    service_category: ServiceCategory
    service_name: str
    recurrence: Recurrence
    recurrences_available: list[Recurrence]
    tld_id: int | None
    service_code: str
    service_url: str
    activation_price: Amount
    renew_price: Amount | None
    restore_price: Amount | None
    transfer_price: Amount | None
    is_primary: bool | None
    is_secondary: bool | None
    is_presale: bool | None
    is_aftersale: bool | None
    is_quantifiable: bool | None
    quantity_min: int | None
    quantity_max: int | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.amount import Amount

        service_id = self.service_id

        service_category = self.service_category.to_dict()

        service_name = self.service_name

        recurrence = self.recurrence.to_dict()

        recurrences_available = []
        for recurrences_available_item_data in self.recurrences_available:
            recurrences_available_item = recurrences_available_item_data.to_dict()
            recurrences_available.append(recurrences_available_item)

        tld_id: int | None
        tld_id = self.tld_id

        service_code = self.service_code

        service_url = self.service_url

        activation_price = self.activation_price.to_dict()

        renew_price: dict[str, Any] | None
        if isinstance(self.renew_price, Amount):
            renew_price = self.renew_price.to_dict()
        else:
            renew_price = self.renew_price

        restore_price: dict[str, Any] | None
        if isinstance(self.restore_price, Amount):
            restore_price = self.restore_price.to_dict()
        else:
            restore_price = self.restore_price

        transfer_price: dict[str, Any] | None
        if isinstance(self.transfer_price, Amount):
            transfer_price = self.transfer_price.to_dict()
        else:
            transfer_price = self.transfer_price

        is_primary: bool | None
        is_primary = self.is_primary

        is_secondary: bool | None
        is_secondary = self.is_secondary

        is_presale: bool | None
        is_presale = self.is_presale

        is_aftersale: bool | None
        is_aftersale = self.is_aftersale

        is_quantifiable: bool | None
        is_quantifiable = self.is_quantifiable

        quantity_min: int | None
        quantity_min = self.quantity_min

        quantity_max: int | None
        quantity_max = self.quantity_max

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "service_id": service_id,
                "service_category": service_category,
                "service_name": service_name,
                "recurrence": recurrence,
                "recurrences_available": recurrences_available,
                "tld_id": tld_id,
                "service_code": service_code,
                "service_url": service_url,
                "activation_price": activation_price,
                "renew_price": renew_price,
                "restore_price": restore_price,
                "transfer_price": transfer_price,
                "is_primary": is_primary,
                "is_secondary": is_secondary,
                "is_presale": is_presale,
                "is_aftersale": is_aftersale,
                "is_quantifiable": is_quantifiable,
                "quantity_min": quantity_min,
                "quantity_max": quantity_max,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.amount import Amount
        from ..models.recurrence import Recurrence
        from ..models.service_category import ServiceCategory

        d = dict(src_dict)
        service_id = d.pop("service_id")

        service_category = ServiceCategory.from_dict(d.pop("service_category"))

        service_name = d.pop("service_name")

        recurrence = Recurrence.from_dict(d.pop("recurrence"))

        recurrences_available = []
        _recurrences_available = d.pop("recurrences_available")
        for recurrences_available_item_data in _recurrences_available:
            recurrences_available_item = Recurrence.from_dict(recurrences_available_item_data)

            recurrences_available.append(recurrences_available_item)

        def _parse_tld_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        tld_id = _parse_tld_id(d.pop("tld_id"))

        service_code = d.pop("service_code")

        service_url = d.pop("service_url")

        activation_price = Amount.from_dict(d.pop("activation_price"))

        def _parse_renew_price(data: object) -> Amount | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                renew_price_type_0 = Amount.from_dict(data)

                return renew_price_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Amount | None, data)

        renew_price = _parse_renew_price(d.pop("renew_price"))

        def _parse_restore_price(data: object) -> Amount | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                restore_price_type_0 = Amount.from_dict(data)

                return restore_price_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Amount | None, data)

        restore_price = _parse_restore_price(d.pop("restore_price"))

        def _parse_transfer_price(data: object) -> Amount | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                transfer_price_type_0 = Amount.from_dict(data)

                return transfer_price_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Amount | None, data)

        transfer_price = _parse_transfer_price(d.pop("transfer_price"))

        def _parse_is_primary(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        is_primary = _parse_is_primary(d.pop("is_primary"))

        def _parse_is_secondary(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        is_secondary = _parse_is_secondary(d.pop("is_secondary"))

        def _parse_is_presale(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        is_presale = _parse_is_presale(d.pop("is_presale"))

        def _parse_is_aftersale(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        is_aftersale = _parse_is_aftersale(d.pop("is_aftersale"))

        def _parse_is_quantifiable(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        is_quantifiable = _parse_is_quantifiable(d.pop("is_quantifiable"))

        def _parse_quantity_min(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        quantity_min = _parse_quantity_min(d.pop("quantity_min"))

        def _parse_quantity_max(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        quantity_max = _parse_quantity_max(d.pop("quantity_max"))

        service = cls(
            service_id=service_id,
            service_category=service_category,
            service_name=service_name,
            recurrence=recurrence,
            recurrences_available=recurrences_available,
            tld_id=tld_id,
            service_code=service_code,
            service_url=service_url,
            activation_price=activation_price,
            renew_price=renew_price,
            restore_price=restore_price,
            transfer_price=transfer_price,
            is_primary=is_primary,
            is_secondary=is_secondary,
            is_presale=is_presale,
            is_aftersale=is_aftersale,
            is_quantifiable=is_quantifiable,
            quantity_min=quantity_min,
            quantity_max=quantity_max,
        )

        service.additional_properties = d
        return service

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
