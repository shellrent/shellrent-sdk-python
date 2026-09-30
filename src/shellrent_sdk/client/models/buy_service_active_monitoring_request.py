from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

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
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        service_id = self.service_id

        account_id = self.account_id

        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
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

        buy_service_active_monitoring_request.additional_properties = d
        return buy_service_active_monitoring_request

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
