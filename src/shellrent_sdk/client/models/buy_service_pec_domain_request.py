from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.buy_service_pec_domain_request_data import BuyServicePecDomainRequestData


T = TypeVar("T", bound="BuyServicePecDomainRequest")


@_attrs_define
class BuyServicePecDomainRequest:
    data: BuyServicePecDomainRequestData
    """ Domain to activate for PEC (certified email, "Posta Elettronica Certificata") and data of its owner; the
    `transferin_*` documents only for a transfer """
    account_id: int | Unset = UNSET
    """ ID of the account of the user that will be the owner of the purchase (available to Resellers only) """

    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_dict()

        account_id = self.account_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "data": data,
            }
        )
        if account_id is not UNSET:
            field_dict["account_id"] = account_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.buy_service_pec_domain_request_data import (
            BuyServicePecDomainRequestData,
        )

        d = dict(src_dict)
        data = BuyServicePecDomainRequestData.from_dict(d.pop("data"))

        account_id = d.pop("account_id", UNSET)

        buy_service_pec_domain_request = cls(
            data=data,
            account_id=account_id,
        )

        return buy_service_pec_domain_request
