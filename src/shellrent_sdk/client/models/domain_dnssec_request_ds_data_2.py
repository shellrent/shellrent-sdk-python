from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domain_dnssec_request_ds_data_2_digest_type import (
    DomainDnssecRequestDsData2DigestType,
)

T = TypeVar("T", bound="DomainDnssecRequestDsData2")


@_attrs_define
class DomainDnssecRequestDsData2:
    """DS DATA second record"""

    key_tag: int
    algorithm: int
    digest_type: DomainDnssecRequestDsData2DigestType
    digest: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key_tag = self.key_tag

        algorithm = self.algorithm

        digest_type = self.digest_type.value

        digest = self.digest

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key_tag": key_tag,
                "algorithm": algorithm,
                "digest_type": digest_type,
                "digest": digest,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        key_tag = d.pop("key_tag")

        algorithm = d.pop("algorithm")

        digest_type = DomainDnssecRequestDsData2DigestType(d.pop("digest_type"))

        digest = d.pop("digest")

        domain_dnssec_request_ds_data_2 = cls(
            key_tag=key_tag,
            algorithm=algorithm,
            digest_type=digest_type,
            digest=digest,
        )

        domain_dnssec_request_ds_data_2.additional_properties = d
        return domain_dnssec_request_ds_data_2

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
