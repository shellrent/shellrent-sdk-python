from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="BuyServiceSecuremailForGoogleWorkspaceRequestConfiguration")


@_attrs_define
class BuyServiceSecuremailForGoogleWorkspaceRequestConfiguration:
    """SecureMail for Google Workspace configuration options"""

    service_quantity: int | Unset = UNSET
    """ Number of mailboxes to protect. """

    def to_dict(self) -> dict[str, Any]:
        service_quantity = self.service_quantity

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if service_quantity is not UNSET:
            field_dict["SERVICE_QUANTITY"] = service_quantity

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        service_quantity = d.pop("SERVICE_QUANTITY", UNSET)

        buy_service_securemail_for_google_workspace_request_configuration = cls(
            service_quantity=service_quantity,
        )

        return buy_service_securemail_for_google_workspace_request_configuration
