from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="OAuthTokenResponse")


@_attrs_define
class OAuthTokenResponse:
    token_type: str
    expires_in: int
    access_token: str
    scope: str
    """ Elenco degli scope concessi separati da spazio """
    audience: str
    """ Audience associata al token """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        token_type = self.token_type

        expires_in = self.expires_in

        access_token = self.access_token

        scope = self.scope

        audience = self.audience

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "token_type": token_type,
                "expires_in": expires_in,
                "access_token": access_token,
                "scope": scope,
                "audience": audience,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        token_type = d.pop("token_type")

        expires_in = d.pop("expires_in")

        access_token = d.pop("access_token")

        scope = d.pop("scope")

        audience = d.pop("audience")

        o_auth_token_response = cls(
            token_type=token_type,
            expires_in=expires_in,
            access_token=access_token,
            scope=scope,
            audience=audience,
        )

        o_auth_token_response.additional_properties = d
        return o_auth_token_response

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
