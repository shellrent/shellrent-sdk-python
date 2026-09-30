from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HostingSslCertificateInstallRequest")


@_attrs_define
class HostingSslCertificateInstallRequest:
    ssl_certificate_id: int | None | Unset = UNSET
    destination_type: str | Unset = "web"
    cn_type: str | Unset = "NORMAL"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ssl_certificate_id: int | None | Unset
        if isinstance(self.ssl_certificate_id, Unset):
            ssl_certificate_id = UNSET
        else:
            ssl_certificate_id = self.ssl_certificate_id

        destination_type = self.destination_type

        cn_type = self.cn_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ssl_certificate_id is not UNSET:
            field_dict["ssl_certificate_id"] = ssl_certificate_id
        if destination_type is not UNSET:
            field_dict["destination_type"] = destination_type
        if cn_type is not UNSET:
            field_dict["cn_type"] = cn_type

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_ssl_certificate_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        ssl_certificate_id = _parse_ssl_certificate_id(d.pop("ssl_certificate_id", UNSET))

        destination_type = d.pop("destination_type", UNSET)

        cn_type = d.pop("cn_type", UNSET)

        hosting_ssl_certificate_install_request = cls(
            ssl_certificate_id=ssl_certificate_id,
            destination_type=destination_type,
            cn_type=cn_type,
        )

        hosting_ssl_certificate_install_request.additional_properties = d
        return hosting_ssl_certificate_install_request

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
