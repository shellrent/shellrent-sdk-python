from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="HostingSslCertificate")


@_attrs_define
class HostingSslCertificate:
    hosting_ssl_certificate_id: int
    hosting_id: int
    ssl_certificate_id: int | None
    lets_encrypt_id: int | None
    external_certificate_id: int | None
    cn_type: None | str
    installation_date: datetime.datetime | None
    https_rewrite: bool | None
    destination_type: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hosting_ssl_certificate_id = self.hosting_ssl_certificate_id

        hosting_id = self.hosting_id

        ssl_certificate_id: int | None
        ssl_certificate_id = self.ssl_certificate_id

        lets_encrypt_id: int | None
        lets_encrypt_id = self.lets_encrypt_id

        external_certificate_id: int | None
        external_certificate_id = self.external_certificate_id

        cn_type: None | str
        cn_type = self.cn_type

        installation_date: None | str
        if isinstance(self.installation_date, datetime.datetime):
            installation_date = self.installation_date.isoformat()
        else:
            installation_date = self.installation_date

        https_rewrite: bool | None
        https_rewrite = self.https_rewrite

        destination_type: None | str
        destination_type = self.destination_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hosting_ssl_certificate_id": hosting_ssl_certificate_id,
                "hosting_id": hosting_id,
                "ssl_certificate_id": ssl_certificate_id,
                "lets_encrypt_id": lets_encrypt_id,
                "external_certificate_id": external_certificate_id,
                "cn_type": cn_type,
                "installation_date": installation_date,
                "https_rewrite": https_rewrite,
                "destination_type": destination_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        hosting_ssl_certificate_id = d.pop("hosting_ssl_certificate_id")

        hosting_id = d.pop("hosting_id")

        def _parse_ssl_certificate_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        ssl_certificate_id = _parse_ssl_certificate_id(d.pop("ssl_certificate_id"))

        def _parse_lets_encrypt_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        lets_encrypt_id = _parse_lets_encrypt_id(d.pop("lets_encrypt_id"))

        def _parse_external_certificate_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        external_certificate_id = _parse_external_certificate_id(d.pop("external_certificate_id"))

        def _parse_cn_type(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        cn_type = _parse_cn_type(d.pop("cn_type"))

        def _parse_installation_date(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                installation_date_type_0 = datetime.datetime.fromisoformat(data)

                return installation_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        installation_date = _parse_installation_date(d.pop("installation_date"))

        def _parse_https_rewrite(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        https_rewrite = _parse_https_rewrite(d.pop("https_rewrite"))

        def _parse_destination_type(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        destination_type = _parse_destination_type(d.pop("destination_type"))

        hosting_ssl_certificate = cls(
            hosting_ssl_certificate_id=hosting_ssl_certificate_id,
            hosting_id=hosting_id,
            ssl_certificate_id=ssl_certificate_id,
            lets_encrypt_id=lets_encrypt_id,
            external_certificate_id=external_certificate_id,
            cn_type=cn_type,
            installation_date=installation_date,
            https_rewrite=https_rewrite,
            destination_type=destination_type,
        )

        hosting_ssl_certificate.additional_properties = d
        return hosting_ssl_certificate

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
