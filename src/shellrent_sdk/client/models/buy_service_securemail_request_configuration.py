from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="BuyServiceSecuremailRequestConfiguration")


@_attrs_define
class BuyServiceSecuremailRequestConfiguration:
    """SecureMail configuration options"""

    secure_mail_hosting: int | Unset = UNSET
    """ Active Hosting purchase ID for which you are requesting to secure the email service. """

    def to_dict(self) -> dict[str, Any]:
        secure_mail_hosting = self.secure_mail_hosting

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if secure_mail_hosting is not UNSET:
            field_dict["SECURE_MAIL_HOSTING"] = secure_mail_hosting

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        secure_mail_hosting = d.pop("SECURE_MAIL_HOSTING", UNSET)

        buy_service_securemail_request_configuration = cls(
            secure_mail_hosting=secure_mail_hosting,
        )

        return buy_service_securemail_request_configuration
