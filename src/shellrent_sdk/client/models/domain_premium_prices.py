from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.amount import Amount


T = TypeVar("T", bound="DomainPremiumPrices")


@_attrs_define
class DomainPremiumPrices:
    """Our prices for a premium domain, without VAT: the cost asked by the registry plus our markup. The order of a premium
    domain uses these prices

    """

    activation_price: Amount
    """ Amount in euros: the taxable amount and, when computed with a tax regime, the VAT rate, the VAT and the
    total, which are null otherwise """
    renew_price: Amount
    """ Amount in euros: the taxable amount and, when computed with a tax regime, the VAT rate, the VAT and the
    total, which are null otherwise """
    restore_price: Amount | None
    """ Restore price; null when the registry gave none """
    transfer_price: Amount | None
    """ Transfer price; null when the registry gave none """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.amount import Amount

        activation_price = self.activation_price.to_dict()

        renew_price = self.renew_price.to_dict()

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "activation_price": activation_price,
                "renew_price": renew_price,
                "restore_price": restore_price,
                "transfer_price": transfer_price,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.amount import Amount

        d = dict(src_dict)
        activation_price = Amount.from_dict(d.pop("activation_price"))

        renew_price = Amount.from_dict(d.pop("renew_price"))

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

        domain_premium_prices = cls(
            activation_price=activation_price,
            renew_price=renew_price,
            restore_price=restore_price,
            transfer_price=transfer_price,
        )

        domain_premium_prices.additional_properties = d
        return domain_premium_prices

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
