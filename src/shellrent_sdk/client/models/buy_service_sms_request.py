from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="BuyServiceSmsRequest")


@_attrs_define
class BuyServiceSmsRequest:
    service_id: int
    """ ID of the Service to buy """
    account_id: int | Unset = UNSET
    """ ID of the account of the user that will be the owner of the purchase (available to Resellers only) """

    def to_dict(self) -> dict[str, Any]:
        service_id = self.service_id

        account_id = self.account_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "service_id": service_id,
            }
        )
        if account_id is not UNSET:
            field_dict["account_id"] = account_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        service_id = d.pop("service_id")

        account_id = d.pop("account_id", UNSET)

        buy_service_sms_request = cls(
            service_id=service_id,
            account_id=account_id,
        )

        return buy_service_sms_request
