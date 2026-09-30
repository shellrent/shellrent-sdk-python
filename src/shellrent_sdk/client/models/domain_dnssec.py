from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.dnssec_ds_data import DnssecDsData
    from ..models.dnssec_key_data import DnssecKeyData


T = TypeVar("T", bound="DomainDnssec")


@_attrs_define
class DomainDnssec:
    ds_data: list[DnssecDsData]
    key_data: list[DnssecKeyData]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ds_data = []
        for ds_data_item_data in self.ds_data:
            ds_data_item = ds_data_item_data.to_dict()
            ds_data.append(ds_data_item)

        key_data = []
        for key_data_item_data in self.key_data:
            key_data_item = key_data_item_data.to_dict()
            key_data.append(key_data_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ds_data": ds_data,
                "key_data": key_data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.dnssec_ds_data import DnssecDsData
        from ..models.dnssec_key_data import DnssecKeyData

        d = dict(src_dict)
        ds_data = []
        _ds_data = d.pop("ds_data")
        for ds_data_item_data in _ds_data:
            ds_data_item = DnssecDsData.from_dict(ds_data_item_data)

            ds_data.append(ds_data_item)

        key_data = []
        _key_data = d.pop("key_data")
        for key_data_item_data in _key_data:
            key_data_item = DnssecKeyData.from_dict(key_data_item_data)

            key_data.append(key_data_item)

        domain_dnssec = cls(
            ds_data=ds_data,
            key_data=key_data,
        )

        domain_dnssec.additional_properties = d
        return domain_dnssec

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
