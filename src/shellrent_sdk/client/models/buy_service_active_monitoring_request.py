from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.buy_service_active_monitoring_request_data import (
        BuyServiceActiveMonitoringRequestData,
    )


T = TypeVar("T", bound="BuyServiceActiveMonitoringRequest")


@_attrs_define
class BuyServiceActiveMonitoringRequest:
    service_id: int
    """ ID of the Service to buy """
    account_id: int | Unset = UNSET
    """ ID of the account of the user that will be the owner of the purchase (available to Resellers only) """
    data: BuyServiceActiveMonitoringRequestData | Unset = UNSET
    """ Target to monitor with the Active Monitoring service """

    def to_dict(self) -> dict[str, Any]:
        service_id = self.service_id

        account_id = self.account_id

        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "service_id": service_id,
            }
        )
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.buy_service_active_monitoring_request_data import (
            BuyServiceActiveMonitoringRequestData,
        )

        d = dict(src_dict)
        service_id = d.pop("service_id")

        account_id = d.pop("account_id", UNSET)

        _data = d.pop("data", UNSET)
        data: BuyServiceActiveMonitoringRequestData | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = BuyServiceActiveMonitoringRequestData.from_dict(_data)

        buy_service_active_monitoring_request = cls(
            service_id=service_id,
            account_id=account_id,
            data=data,
        )

        return buy_service_active_monitoring_request
