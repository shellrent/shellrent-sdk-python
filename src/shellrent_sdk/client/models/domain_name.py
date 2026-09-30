from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DomainName")


@_attrs_define
class DomainName:
    unicode: None | str
    punycode: None | str
    unicode_name: None | str
    punycode_name: None | str
    unicode_tld: None | str
    punycode_tld: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unicode: None | str
        unicode = self.unicode

        punycode: None | str
        punycode = self.punycode

        unicode_name: None | str
        unicode_name = self.unicode_name

        punycode_name: None | str
        punycode_name = self.punycode_name

        unicode_tld: None | str
        unicode_tld = self.unicode_tld

        punycode_tld: None | str
        punycode_tld = self.punycode_tld

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "unicode": unicode,
                "punycode": punycode,
                "unicode_name": unicode_name,
                "punycode_name": punycode_name,
                "unicode_tld": unicode_tld,
                "punycode_tld": punycode_tld,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_unicode(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        unicode = _parse_unicode(d.pop("unicode"))

        def _parse_punycode(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        punycode = _parse_punycode(d.pop("punycode"))

        def _parse_unicode_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        unicode_name = _parse_unicode_name(d.pop("unicode_name"))

        def _parse_punycode_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        punycode_name = _parse_punycode_name(d.pop("punycode_name"))

        def _parse_unicode_tld(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        unicode_tld = _parse_unicode_tld(d.pop("unicode_tld"))

        def _parse_punycode_tld(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        punycode_tld = _parse_punycode_tld(d.pop("punycode_tld"))

        domain_name = cls(
            unicode=unicode,
            punycode=punycode,
            unicode_name=unicode_name,
            punycode_name=punycode_name,
            unicode_tld=unicode_tld,
            punycode_tld=punycode_tld,
        )

        domain_name.additional_properties = d
        return domain_name

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
