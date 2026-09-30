from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BuyServiceCloudStorageRequest")


@_attrs_define
class BuyServiceCloudStorageRequest:
    service_id: int
    """ ID of the Service to buy """
    recurrence_id: int | Unset = UNSET
    """ ID of the Recurrence to assign to the purchased service """
    account_id: int | Unset = UNSET
    """ ID of the account of the user that will be the owner of the purchase (available to Resellers only) """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        service_id = self.service_id

        recurrence_id = self.recurrence_id

        account_id = self.account_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "service_id": service_id,
            }
        )
        if recurrence_id is not UNSET:
            field_dict["recurrence_id"] = recurrence_id
        if account_id is not UNSET:
            field_dict["account_id"] = account_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        service_id = d.pop("service_id")

        recurrence_id = d.pop("recurrence_id", UNSET)

        account_id = d.pop("account_id", UNSET)

        buy_service_cloud_storage_request = cls(
            service_id=service_id,
            recurrence_id=recurrence_id,
            account_id=account_id,
        )

        buy_service_cloud_storage_request.additional_properties = d
        return buy_service_cloud_storage_request

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
