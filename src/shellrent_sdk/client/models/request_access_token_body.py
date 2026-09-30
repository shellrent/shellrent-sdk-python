from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.o_auth_audience import OAuthAudience
from ..models.request_access_token_body_grant_type import RequestAccessTokenBodyGrantType
from ..types import UNSET, Unset

T = TypeVar("T", bound="RequestAccessTokenBody")


@_attrs_define
class RequestAccessTokenBody:
    grant_type: RequestAccessTokenBodyGrantType
    client_id: None | str | Unset = UNSET
    """ Client ID se non fornito tramite Authorization header Basic. """
    client_secret: None | str | Unset = UNSET
    """ Client secret se non fornito tramite Authorization header Basic. """
    scope: None | str | Unset = UNSET
    """ Scope separati da spazio. Se omesso: tutti gli scope assegnati al client. """
    audience: None | OAuthAudience | Unset = UNSET
    """ Se omessa: l'unica audience del client. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        grant_type = self.grant_type.value

        client_id: None | str | Unset
        if isinstance(self.client_id, Unset):
            client_id = UNSET
        else:
            client_id = self.client_id

        client_secret: None | str | Unset
        if isinstance(self.client_secret, Unset):
            client_secret = UNSET
        else:
            client_secret = self.client_secret

        scope: None | str | Unset
        if isinstance(self.scope, Unset):
            scope = UNSET
        else:
            scope = self.scope

        audience: None | str | Unset
        if isinstance(self.audience, Unset):
            audience = UNSET
        elif isinstance(self.audience, OAuthAudience):
            audience = self.audience.value
        else:
            audience = self.audience

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "grant_type": grant_type,
            }
        )
        if client_id is not UNSET:
            field_dict["client_id"] = client_id
        if client_secret is not UNSET:
            field_dict["client_secret"] = client_secret
        if scope is not UNSET:
            field_dict["scope"] = scope
        if audience is not UNSET:
            field_dict["audience"] = audience

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        grant_type = RequestAccessTokenBodyGrantType(d.pop("grant_type"))

        def _parse_client_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        client_id = _parse_client_id(d.pop("client_id", UNSET))

        def _parse_client_secret(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        client_secret = _parse_client_secret(d.pop("client_secret", UNSET))

        def _parse_scope(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        scope = _parse_scope(d.pop("scope", UNSET))

        def _parse_audience(data: object) -> None | OAuthAudience | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                audience_type_0 = OAuthAudience(data)

                return audience_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OAuthAudience | Unset, data)

        audience = _parse_audience(d.pop("audience", UNSET))

        request_access_token_body = cls(
            grant_type=grant_type,
            client_id=client_id,
            client_secret=client_secret,
            scope=scope,
            audience=audience,
        )

        request_access_token_body.additional_properties = d
        return request_access_token_body

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
