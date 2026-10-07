from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domain_name import DomainName
    from ..models.domain_premium_prices import DomainPremiumPrices


T = TypeVar("T", bound="DomainAvailability")


@_attrs_define
class DomainAvailability:
    """Availability of a domain name (whois): how it can be bought and, for premium domains, our prices"""

    domain_name: DomainName
    """ Name of a domain, whole and split into name and extension, in Unicode and in punycode """
    availability: str
    """ How the domain can be bought: `A` (available: it can be registered), `T` (already registered: it can be
    transferred) or `R` (expired with us: it can be restored) """
    premium: bool
    """ Whether the registry sells the domain at a premium price, which it sets itself """
    premium_prices: DomainPremiumPrices | None
    """ Our prices for the premium domain; null when the domain is not premium, when the registry gave no price (the
    domain cannot be bought) and for sub-accounts """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.domain_premium_prices import DomainPremiumPrices

        domain_name = self.domain_name.to_dict()

        availability = self.availability

        premium = self.premium

        premium_prices: dict[str, Any] | None
        if isinstance(self.premium_prices, DomainPremiumPrices):
            premium_prices = self.premium_prices.to_dict()
        else:
            premium_prices = self.premium_prices

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "domain_name": domain_name,
                "availability": availability,
                "premium": premium,
                "premium_prices": premium_prices,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.domain_name import DomainName
        from ..models.domain_premium_prices import DomainPremiumPrices

        d = dict(src_dict)
        domain_name = DomainName.from_dict(d.pop("domain_name"))

        availability = d.pop("availability")

        premium = d.pop("premium")

        def _parse_premium_prices(data: object) -> DomainPremiumPrices | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                premium_prices_type_0 = DomainPremiumPrices.from_dict(data)

                return premium_prices_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DomainPremiumPrices | None, data)

        premium_prices = _parse_premium_prices(d.pop("premium_prices"))

        domain_availability = cls(
            domain_name=domain_name,
            availability=availability,
            premium=premium,
            premium_prices=premium_prices,
        )

        domain_availability.additional_properties = d
        return domain_availability

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
