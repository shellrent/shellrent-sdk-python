from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.buy_service_securemail_for_microsoft_365_request_configuration import (
        BuyServiceSecuremailForMicrosoft365RequestConfiguration,
    )
    from ..models.buy_service_securemail_for_microsoft_365_request_data import (
        BuyServiceSecuremailForMicrosoft365RequestData,
    )


T = TypeVar("T", bound="BuyServiceSecuremailForMicrosoft365Request")


@_attrs_define
class BuyServiceSecuremailForMicrosoft365Request:
    configuration: BuyServiceSecuremailForMicrosoft365RequestConfiguration
    """ SecureMail for Microsoft 365 configuration options """
    data: BuyServiceSecuremailForMicrosoft365RequestData
    account_id: int | Unset = UNSET
    """ ID of the account of the user that will be the owner of the purchase (available to Resellers only) """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        configuration = self.configuration.to_dict()

        data = self.data.to_dict()

        account_id = self.account_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
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
        from ..models.buy_service_securemail_for_microsoft_365_request_configuration import (
            BuyServiceSecuremailForMicrosoft365RequestConfiguration,
        )
        from ..models.buy_service_securemail_for_microsoft_365_request_data import (
            BuyServiceSecuremailForMicrosoft365RequestData,
        )

        d = dict(src_dict)
        configuration = BuyServiceSecuremailForMicrosoft365RequestConfiguration.from_dict(
            d.pop("configuration")
        )

        data = BuyServiceSecuremailForMicrosoft365RequestData.from_dict(d.pop("data"))

        account_id = d.pop("account_id", UNSET)

        buy_service_securemail_for_microsoft_365_request = cls(
            configuration=configuration,
            data=data,
            account_id=account_id,
        )

        buy_service_securemail_for_microsoft_365_request.additional_properties = d
        return buy_service_securemail_for_microsoft_365_request

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
