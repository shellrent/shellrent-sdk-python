from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="BuyServiceDomainRequestConfiguration")


@_attrs_define
class BuyServiceDomainRequestConfiguration:
    """Domain purchase configuration options"""

    domain_name: str | Unset = UNSET
    """ Domain complete name (with TLD extension), for example: "example.com" or "example.co.uk" """
    extension: str | Unset = UNSET
    """ TLD extension of the domain, for example: "com" or "co.uk" """

    def to_dict(self) -> dict[str, Any]:
        domain_name = self.domain_name

        extension = self.extension

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if domain_name is not UNSET:
            field_dict["domain_name"] = domain_name
        if extension is not UNSET:
            field_dict["extension"] = extension

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        domain_name = d.pop("domain_name", UNSET)

        extension = d.pop("extension", UNSET)

        buy_service_domain_request_configuration = cls(
            domain_name=domain_name,
            extension=extension,
        )

        return buy_service_domain_request_configuration
