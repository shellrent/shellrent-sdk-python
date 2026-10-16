from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.buy_service_domain_request_configuration import (
        BuyServiceDomainRequestConfiguration,
    )
    from ..models.buy_service_domain_request_data import BuyServiceDomainRequestData


T = TypeVar("T", bound="BuyServiceDomainRequest")


@_attrs_define
class BuyServiceDomainRequest:
    configuration: BuyServiceDomainRequestConfiguration
    """ Domain purchase configuration options """
    data: BuyServiceDomainRequestData
    """ Registration data of the domain: the contacts that its TLD requires and, for a transfer, the authcode """
    account_id: int | Unset = UNSET
    """ ID of the account of the user that will be the owner of the purchase (available to Resellers only) """

    def to_dict(self) -> dict[str, Any]:
        configuration = self.configuration.to_dict()

        data = self.data.to_dict()

        account_id = self.account_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "configuration": configuration,
                "data": data,
            }
        )
        if account_id is not UNSET:
            field_dict["account_id"] = account_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.buy_service_domain_request_configuration import (
            BuyServiceDomainRequestConfiguration,
        )
        from ..models.buy_service_domain_request_data import (
            BuyServiceDomainRequestData,
        )

        d = dict(src_dict)
        configuration = BuyServiceDomainRequestConfiguration.from_dict(d.pop("configuration"))

        data = BuyServiceDomainRequestData.from_dict(d.pop("data"))

        account_id = d.pop("account_id", UNSET)

        buy_service_domain_request = cls(
            configuration=configuration,
            data=data,
            account_id=account_id,
        )

        return buy_service_domain_request
