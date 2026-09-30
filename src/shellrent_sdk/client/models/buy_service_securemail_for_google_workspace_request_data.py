from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="BuyServiceSecuremailForGoogleWorkspaceRequestData")


@_attrs_define
class BuyServiceSecuremailForGoogleWorkspaceRequestData:
    email_domain: str
    """ Domain name for the emails to be protected """
    super_admin_email: str
    """ Email address of the Google Workspace superadmin """
    oauth2_json_file: int
    """ ID of the uploaded file (first file, extension: "json") """
    key_json_file: int
    """ ID of the uploaded file (second file, extension: "json") """

    def to_dict(self) -> dict[str, Any]:
        email_domain = self.email_domain

        super_admin_email = self.super_admin_email

        oauth2_json_file = self.oauth2_json_file

        key_json_file = self.key_json_file

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "email_domain": email_domain,
                "super_admin_email": super_admin_email,
                "oauth2_json_file": oauth2_json_file,
                "key_json_file": key_json_file,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        email_domain = d.pop("email_domain")

        super_admin_email = d.pop("super_admin_email")

        oauth2_json_file = d.pop("oauth2_json_file")

        key_json_file = d.pop("key_json_file")

        buy_service_securemail_for_google_workspace_request_data = cls(
            email_domain=email_domain,
            super_admin_email=super_admin_email,
            oauth2_json_file=oauth2_json_file,
            key_json_file=key_json_file,
        )

        return buy_service_securemail_for_google_workspace_request_data
