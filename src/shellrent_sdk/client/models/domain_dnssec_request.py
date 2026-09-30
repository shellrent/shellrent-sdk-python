from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domain_dnssec_request_ds_data_1 import DomainDnssecRequestDsData1
    from ..models.domain_dnssec_request_ds_data_2 import DomainDnssecRequestDsData2
    from ..models.domain_dnssec_request_key_data_256_item import DomainDnssecRequestKeyData256Item
    from ..models.domain_dnssec_request_key_data_257_item import DomainDnssecRequestKeyData257Item


T = TypeVar("T", bound="DomainDnssecRequest")


@_attrs_define
class DomainDnssecRequest:
    zone_ttl: int
    ds_data_1: DomainDnssecRequestDsData1
    """ DS DATA first record """
    ds_data_2: DomainDnssecRequestDsData2
    """ DS DATA second record """
    key_data_256: list[DomainDnssecRequestKeyData256Item] | Unset = UNSET
    """ KEY DATA 256 records """
    key_data_257: list[DomainDnssecRequestKeyData257Item] | Unset = UNSET
    """ KEY DATA 257 records """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        zone_ttl = self.zone_ttl

        ds_data_1 = self.ds_data_1.to_dict()

        ds_data_2 = self.ds_data_2.to_dict()

        key_data_256: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.key_data_256, Unset):
            key_data_256 = []
            for key_data_256_item_data in self.key_data_256:
                key_data_256_item = key_data_256_item_data.to_dict()
                key_data_256.append(key_data_256_item)

        key_data_257: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.key_data_257, Unset):
            key_data_257 = []
            for key_data_257_item_data in self.key_data_257:
                key_data_257_item = key_data_257_item_data.to_dict()
                key_data_257.append(key_data_257_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "zone_ttl": zone_ttl,
                "ds_data_1": ds_data_1,
                "ds_data_2": ds_data_2,
            }
        )
        if key_data_256 is not UNSET:
            field_dict["key_data_256"] = key_data_256
        if key_data_257 is not UNSET:
            field_dict["key_data_257"] = key_data_257

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.domain_dnssec_request_ds_data_1 import (
            DomainDnssecRequestDsData1,
        )
        from ..models.domain_dnssec_request_ds_data_2 import (
            DomainDnssecRequestDsData2,
        )
        from ..models.domain_dnssec_request_key_data_256_item import (
            DomainDnssecRequestKeyData256Item,
        )
        from ..models.domain_dnssec_request_key_data_257_item import (
            DomainDnssecRequestKeyData257Item,
        )

        d = dict(src_dict)
        zone_ttl = d.pop("zone_ttl")

        ds_data_1 = DomainDnssecRequestDsData1.from_dict(d.pop("ds_data_1"))

        ds_data_2 = DomainDnssecRequestDsData2.from_dict(d.pop("ds_data_2"))

        _key_data_256 = d.pop("key_data_256", UNSET)
        key_data_256: list[DomainDnssecRequestKeyData256Item] | Unset = UNSET
        if _key_data_256 is not UNSET:
            key_data_256 = []
            for key_data_256_item_data in _key_data_256:
                key_data_256_item = DomainDnssecRequestKeyData256Item.from_dict(
                    key_data_256_item_data
                )

                key_data_256.append(key_data_256_item)

        _key_data_257 = d.pop("key_data_257", UNSET)
        key_data_257: list[DomainDnssecRequestKeyData257Item] | Unset = UNSET
        if _key_data_257 is not UNSET:
            key_data_257 = []
            for key_data_257_item_data in _key_data_257:
                key_data_257_item = DomainDnssecRequestKeyData257Item.from_dict(
                    key_data_257_item_data
                )

                key_data_257.append(key_data_257_item)

        domain_dnssec_request = cls(
            zone_ttl=zone_ttl,
            ds_data_1=ds_data_1,
            ds_data_2=ds_data_2,
            key_data_256=key_data_256,
            key_data_257=key_data_257,
        )

        domain_dnssec_request.additional_properties = d
        return domain_dnssec_request

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
