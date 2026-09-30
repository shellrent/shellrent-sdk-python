from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Country")


@_attrs_define
class Country:
    iso_code_2: str
    """ ie. IT """
    iso_code_3: str
    """ ie. ITA """
    country_name: str
    local_name: str
    phone_code: str
    """ +39, +44, ... """
    continent: str
    """ Europe, America, ... """
    region: str
    """ Macro region """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        iso_code_2 = self.iso_code_2

        iso_code_3 = self.iso_code_3

        country_name = self.country_name

        local_name = self.local_name

        phone_code = self.phone_code

        continent = self.continent

        region = self.region

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "iso_code_2": iso_code_2,
                "iso_code_3": iso_code_3,
                "country_name": country_name,
                "local_name": local_name,
                "phone_code": phone_code,
                "continent": continent,
                "region": region,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        iso_code_2 = d.pop("iso_code_2")

        iso_code_3 = d.pop("iso_code_3")

        country_name = d.pop("country_name")

        local_name = d.pop("local_name")

        phone_code = d.pop("phone_code")

        continent = d.pop("continent")

        region = d.pop("region")

        country = cls(
            iso_code_2=iso_code_2,
            iso_code_3=iso_code_3,
            country_name=country_name,
            local_name=local_name,
            phone_code=phone_code,
            continent=continent,
            region=region,
        )

        country.additional_properties = d
        return country

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
