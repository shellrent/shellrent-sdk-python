from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TaxRegime")


@_attrs_define
class TaxRegime:
    """Tax regime: how VAT applies to the documents"""

    regime_code: str
    """ One of `ORDINARY`, `SPLIT_PAYMENT`, `EU_VIES`, `EU_EXPORTER` (habitual exporter), `EXTRA_EU`, `VATICAN`,
    `SANMARINO` or `ART_26` """
    regime_name: str
    """ Name of the regime, in Italian, for example `Ordinario` """
    code_edocument: None | str
    """ Nature code of the operation on the electronic invoice (`Natura`) when VAT is not applied, for example
    `N2.1`; null for the regimes with VAT """
    tax_rate: float
    """ VAT rate as a fraction, for example `0.22` for 22% """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        regime_code = self.regime_code

        regime_name = self.regime_name

        code_edocument: None | str
        code_edocument = self.code_edocument

        tax_rate = self.tax_rate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "regime_code": regime_code,
                "regime_name": regime_name,
                "code_edocument": code_edocument,
                "tax_rate": tax_rate,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        regime_code = d.pop("regime_code")

        regime_name = d.pop("regime_name")

        def _parse_code_edocument(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        code_edocument = _parse_code_edocument(d.pop("code_edocument"))

        tax_rate = d.pop("tax_rate")

        tax_regime = cls(
            regime_code=regime_code,
            regime_name=regime_name,
            code_edocument=code_edocument,
            tax_rate=tax_rate,
        )

        tax_regime.additional_properties = d
        return tax_regime

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
