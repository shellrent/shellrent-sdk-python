from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.buy_service_veeam_baas_request_configuration import (
        BuyServiceVeeamBaasRequestConfiguration,
    )


T = TypeVar("T", bound="BuyServiceVeeamBaasRequest")


@_attrs_define
class BuyServiceVeeamBaasRequest:
    configuration: BuyServiceVeeamBaasRequestConfiguration | Unset = UNSET
    """ Veeam BaaS configuration. Every field is optional: an omitted workload quantity counts as 0, and an omitted
    configuration is the same as an empty object. The limits of each workload quantity depend on the corresponding
    workload service: a value outside them is rejected with a validation error (code 1000) that states the limit in
    `meta.errors`. """
    account_id: int | Unset = UNSET
    """ ID of the account of the user that will be the owner of the purchase (available to Resellers only) """

    def to_dict(self) -> dict[str, Any]:
        configuration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.configuration, Unset):
            configuration = self.configuration.to_dict()

        account_id = self.account_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if configuration is not UNSET:
            field_dict["configuration"] = configuration
        if account_id is not UNSET:
            field_dict["account_id"] = account_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.buy_service_veeam_baas_request_configuration import (
            BuyServiceVeeamBaasRequestConfiguration,
        )

        d = dict(src_dict)
        _configuration = d.pop("configuration", UNSET)
        configuration: BuyServiceVeeamBaasRequestConfiguration | Unset
        if isinstance(_configuration, Unset):
            configuration = UNSET
        else:
            configuration = BuyServiceVeeamBaasRequestConfiguration.from_dict(_configuration)

        account_id = d.pop("account_id", UNSET)

        buy_service_veeam_baas_request = cls(
            configuration=configuration,
            account_id=account_id,
        )

        return buy_service_veeam_baas_request
