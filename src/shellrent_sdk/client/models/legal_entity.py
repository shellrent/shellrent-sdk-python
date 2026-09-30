from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.legal_entity_group import LegalEntityGroup
    from ..models.tax_regime import TaxRegime


T = TypeVar("T", bound="LegalEntity")


@_attrs_define
class LegalEntity:
    legal_entity_group: LegalEntityGroup
    tax_regime: TaxRegime
    entity_code: str
    entity_name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        legal_entity_group = self.legal_entity_group.to_dict()

        tax_regime = self.tax_regime.to_dict()

        entity_code = self.entity_code

        entity_name = self.entity_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "legal_entity_group": legal_entity_group,
                "tax_regime": tax_regime,
                "entity_code": entity_code,
                "entity_name": entity_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.legal_entity_group import LegalEntityGroup
        from ..models.tax_regime import TaxRegime

        d = dict(src_dict)
        legal_entity_group = LegalEntityGroup.from_dict(d.pop("legal_entity_group"))

        tax_regime = TaxRegime.from_dict(d.pop("tax_regime"))

        entity_code = d.pop("entity_code")

        entity_name = d.pop("entity_name")

        legal_entity = cls(
            legal_entity_group=legal_entity_group,
            tax_regime=tax_regime,
            entity_code=entity_code,
            entity_name=entity_name,
        )

        legal_entity.additional_properties = d
        return legal_entity

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
