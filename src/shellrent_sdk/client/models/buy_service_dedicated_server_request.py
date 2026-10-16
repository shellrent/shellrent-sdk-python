from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.buy_service_dedicated_server_request_data import (
        BuyServiceDedicatedServerRequestData,
    )


T = TypeVar("T", bound="BuyServiceDedicatedServerRequest")


@_attrs_define
class BuyServiceDedicatedServerRequest:
    service_id: int
    """ ID of the Service to buy """
    data: BuyServiceDedicatedServerRequestData
    """ Dedicated Server configuration and template selection """
    recurrence_id: int | Unset = UNSET
    """ ID of the billing recurrence of the purchased service: one of the `recurrences_available` of the chosen
    service, as listed by `GET /api/v3/shop/dedicated-server`. If omitted, the default recurrence of the service
    (`recurrence`) is used. """
    account_id: int | Unset = UNSET
    """ ID of the account of the user that will be the owner of the purchase (available to Resellers only) """

    def to_dict(self) -> dict[str, Any]:
        service_id = self.service_id

        data = self.data.to_dict()

        recurrence_id = self.recurrence_id

        account_id = self.account_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "service_id": service_id,
                "data": data,
            }
        )
        if recurrence_id is not UNSET:
            field_dict["recurrence_id"] = recurrence_id
        if account_id is not UNSET:
            field_dict["account_id"] = account_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.buy_service_dedicated_server_request_data import (
            BuyServiceDedicatedServerRequestData,
        )

        d = dict(src_dict)
        service_id = d.pop("service_id")

        data = BuyServiceDedicatedServerRequestData.from_dict(d.pop("data"))

        recurrence_id = d.pop("recurrence_id", UNSET)

        account_id = d.pop("account_id", UNSET)

        buy_service_dedicated_server_request = cls(
            service_id=service_id,
            data=data,
            recurrence_id=recurrence_id,
            account_id=account_id,
        )

        return buy_service_dedicated_server_request
