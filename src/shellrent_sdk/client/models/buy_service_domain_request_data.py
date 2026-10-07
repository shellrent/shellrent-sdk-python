from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.buy_service_domain_request_data_contact_data import (
        BuyServiceDomainRequestDataContactData,
    )


T = TypeVar("T", bound="BuyServiceDomainRequestData")


@_attrs_define
class BuyServiceDomainRequestData:
    """Registration data of the domain: the contacts that its TLD requires and, for a transfer, the authcode"""

    contact_data: BuyServiceDomainRequestDataContactData
    """ Domain contact data. Values depend on the TLD requirements. """
    domain_authcode: str | Unset = UNSET
    """ Domain auth-info code (authcode). Required if the domain must be transferred. """

    def to_dict(self) -> dict[str, Any]:
        contact_data = self.contact_data.to_dict()

        domain_authcode = self.domain_authcode

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "contact_data": contact_data,
            }
        )
        if domain_authcode is not UNSET:
            field_dict["domain_authcode"] = domain_authcode

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.buy_service_domain_request_data_contact_data import (
            BuyServiceDomainRequestDataContactData,
        )

        d = dict(src_dict)
        contact_data = BuyServiceDomainRequestDataContactData.from_dict(d.pop("contact_data"))

        domain_authcode = d.pop("domain_authcode", UNSET)

        buy_service_domain_request_data = cls(
            contact_data=contact_data,
            domain_authcode=domain_authcode,
        )

        return buy_service_domain_request_data
