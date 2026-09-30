from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="JwkKey")


@_attrs_define
class JwkKey:
    kid: str
    kty: str
    alg: str
    use: str
    n: str
    """ Modulo base64url """
    e: str
    """ Esponente base64url """
    status: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kid = self.kid

        kty = self.kty

        alg = self.alg

        use = self.use

        n = self.n

        e = self.e

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kid": kid,
                "kty": kty,
                "alg": alg,
                "use": use,
                "n": n,
                "e": e,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        kid = d.pop("kid")

        kty = d.pop("kty")

        alg = d.pop("alg")

        use = d.pop("use")

        n = d.pop("n")

        e = d.pop("e")

        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        jwk_key = cls(
            kid=kid,
            kty=kty,
            alg=alg,
            use=use,
            n=n,
            e=e,
            status=status,
        )

        jwk_key.additional_properties = d
        return jwk_key

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
