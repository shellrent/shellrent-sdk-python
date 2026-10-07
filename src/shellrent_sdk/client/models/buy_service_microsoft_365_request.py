from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.buy_service_microsoft_365_request_data import BuyServiceMicrosoft365RequestData


T = TypeVar("T", bound="BuyServiceMicrosoft365Request")


@_attrs_define
class BuyServiceMicrosoft365Request:
    service_id: int
    """ ID of the Service to buy """
    data: BuyServiceMicrosoft365RequestData
    """ Microsoft 365 tenant of the subscription. All the data is checked before the order is created: with "select"
    the tenant must be one of the account (409 if it already has 2 active subscriptions of the same service); with
    "transfer" and "new" no tenant can have the domain prefix already, and at Microsoft the ".onmicrosoft.com"
    domain must exist ("transfer") or be available ("new"), otherwise 409. Send only the fields of the chosen
    option. """
    quantity: int | Unset = UNSET
    """ Number of seats (user licenses) to purchase. It must be between `quantity_min` and `quantity_max` of the
    chosen service, as listed by `GET /api/v3/shop/microsoft-365/services`. If omitted, `quantity_min` is used.
    Ignored for the services without `quantity_max`. """
    account_id: int | Unset = UNSET
    """ ID of the account of the user that will be the owner of the purchase (available to Resellers only) """

    def to_dict(self) -> dict[str, Any]:
        service_id = self.service_id

        data = self.data.to_dict()

        quantity = self.quantity

        account_id = self.account_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "service_id": service_id,
                "data": data,
            }
        )
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if account_id is not UNSET:
            field_dict["account_id"] = account_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.buy_service_microsoft_365_request_data import (
            BuyServiceMicrosoft365RequestData,
        )

        d = dict(src_dict)
        service_id = d.pop("service_id")

        data = BuyServiceMicrosoft365RequestData.from_dict(d.pop("data"))

        quantity = d.pop("quantity", UNSET)

        account_id = d.pop("account_id", UNSET)

        buy_service_microsoft_365_request = cls(
            service_id=service_id,
            data=data,
            quantity=quantity,
            account_id=account_id,
        )

        return buy_service_microsoft_365_request
