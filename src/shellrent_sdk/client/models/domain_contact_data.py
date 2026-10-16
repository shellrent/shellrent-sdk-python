from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DomainContactData")


@_attrs_define
class DomainContactData:
    """Field of the data of a domain contact"""

    data_field: str
    """ Code of the field, for example `FIRST_NAME`, `EMAIL` or `DOT_IT_ENTITY_TYPE` (see `contact_data` of `GET
    /api/v3/tlds/{tld_id}`) """
    data_value: None | str
    """ Value of the field; for `PHONE_PREFIX` and `FAX_PREFIX`, the id of the country of the prefix; for
    `BIRTHDAY`, a date `YYYY-MM-DD` """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data_field = self.data_field

        data_value: None | str
        data_value = self.data_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data_field": data_field,
                "data_value": data_value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        data_field = d.pop("data_field")

        def _parse_data_value(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        data_value = _parse_data_value(d.pop("data_value"))

        domain_contact_data = cls(
            data_field=data_field,
            data_value=data_value,
        )

        domain_contact_data.additional_properties = d
        return domain_contact_data

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
