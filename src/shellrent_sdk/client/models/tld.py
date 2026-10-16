from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.country import Country
    from ..models.tld_contact_specification import TldContactSpecification


T = TypeVar("T", bound="Tld")


@_attrs_define
class Tld:
    """TLD (domain extension), with the rules for the names and for the contacts of its domains"""

    tld_id: int
    extension: str
    """ Extension without the leading dot, in Unicode (for example `it` or `co.uk`) """
    punycode: str
    """ Extension in punycode """
    country: Country | None
    """ Country of the TLD, for the country-code TLDs (ccTLD); null for the others """
    char_min: int | None
    """ Minimum length of the name, without the extension """
    char_max: int | None
    """ Maximum length of the name, without the extension """
    hyphen_allowed: bool
    """ Whether the name can contain hyphens """
    number_allowed: bool
    """ Whether the name can contain numbers """
    punycode_allowed: bool
    """ Whether the name can contain international characters (IDN) """
    dnssec_enabled: bool
    """ Whether the TLD supports DNSSEC """
    rdap_enabled: bool
    """ Whether the availability of the names is checked with RDAP """
    rdap_url: None | str
    """ URL of the RDAP service used for the TLD; null when not set """
    contact_data: list[TldContactSpecification]
    """ Fields of the contact data of the domains of the TLD, with their type and allowed values (the authcode
    excluded) """
    update_contact_r: bool | None
    """ Whether the registrant contact (`R`) can be changed (`PATCH
    /api/v3/domains/{domain_id}/contacts/{domain_contact_id}`) """
    update_contact_a: bool | None
    """ Whether the administrative contact (`A`) can be changed """
    update_contact_t: bool | None
    """ Whether the technical contact (`T`) can be changed """
    update_contact_o: bool | None
    """ Whether the organization contact (`O`) can be changed """
    update_contact_additional: bool
    """ Whether a change of the contacts must also send the additional data of the TLD to the registry """
    update_contact_transfer: bool
    """ Whether a transfer must also send the additional data of the TLD to the registry """
    transfer_authcode: bool
    """ Whether the transfer of a domain of the TLD requires the authcode """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.country import Country

        tld_id = self.tld_id

        extension = self.extension

        punycode = self.punycode

        country: dict[str, Any] | None
        if isinstance(self.country, Country):
            country = self.country.to_dict()
        else:
            country = self.country

        char_min: int | None
        char_min = self.char_min

        char_max: int | None
        char_max = self.char_max

        hyphen_allowed = self.hyphen_allowed

        number_allowed = self.number_allowed

        punycode_allowed = self.punycode_allowed

        dnssec_enabled = self.dnssec_enabled

        rdap_enabled = self.rdap_enabled

        rdap_url: None | str
        rdap_url = self.rdap_url

        contact_data = []
        for contact_data_item_data in self.contact_data:
            contact_data_item = contact_data_item_data.to_dict()
            contact_data.append(contact_data_item)

        update_contact_r: bool | None
        update_contact_r = self.update_contact_r

        update_contact_a: bool | None
        update_contact_a = self.update_contact_a

        update_contact_t: bool | None
        update_contact_t = self.update_contact_t

        update_contact_o: bool | None
        update_contact_o = self.update_contact_o

        update_contact_additional = self.update_contact_additional

        update_contact_transfer = self.update_contact_transfer

        transfer_authcode = self.transfer_authcode

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tld_id": tld_id,
                "extension": extension,
                "punycode": punycode,
                "country": country,
                "char_min": char_min,
                "char_max": char_max,
                "hyphen_allowed": hyphen_allowed,
                "number_allowed": number_allowed,
                "punycode_allowed": punycode_allowed,
                "dnssec_enabled": dnssec_enabled,
                "rdap_enabled": rdap_enabled,
                "rdap_url": rdap_url,
                "contact_data": contact_data,
                "update_contact_r": update_contact_r,
                "update_contact_a": update_contact_a,
                "update_contact_t": update_contact_t,
                "update_contact_o": update_contact_o,
                "update_contact_additional": update_contact_additional,
                "update_contact_transfer": update_contact_transfer,
                "transfer_authcode": transfer_authcode,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.country import Country
        from ..models.tld_contact_specification import TldContactSpecification

        d = dict(src_dict)
        tld_id = d.pop("tld_id")

        extension = d.pop("extension")

        punycode = d.pop("punycode")

        def _parse_country(data: object) -> Country | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                country_type_0 = Country.from_dict(data)

                return country_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Country | None, data)

        country = _parse_country(d.pop("country"))

        def _parse_char_min(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        char_min = _parse_char_min(d.pop("char_min"))

        def _parse_char_max(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        char_max = _parse_char_max(d.pop("char_max"))

        hyphen_allowed = d.pop("hyphen_allowed")

        number_allowed = d.pop("number_allowed")

        punycode_allowed = d.pop("punycode_allowed")

        dnssec_enabled = d.pop("dnssec_enabled")

        rdap_enabled = d.pop("rdap_enabled")

        def _parse_rdap_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        rdap_url = _parse_rdap_url(d.pop("rdap_url"))

        contact_data = []
        _contact_data = d.pop("contact_data")
        for contact_data_item_data in _contact_data:
            contact_data_item = TldContactSpecification.from_dict(contact_data_item_data)

            contact_data.append(contact_data_item)

        def _parse_update_contact_r(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        update_contact_r = _parse_update_contact_r(d.pop("update_contact_r"))

        def _parse_update_contact_a(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        update_contact_a = _parse_update_contact_a(d.pop("update_contact_a"))

        def _parse_update_contact_t(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        update_contact_t = _parse_update_contact_t(d.pop("update_contact_t"))

        def _parse_update_contact_o(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        update_contact_o = _parse_update_contact_o(d.pop("update_contact_o"))

        update_contact_additional = d.pop("update_contact_additional")

        update_contact_transfer = d.pop("update_contact_transfer")

        transfer_authcode = d.pop("transfer_authcode")

        tld = cls(
            tld_id=tld_id,
            extension=extension,
            punycode=punycode,
            country=country,
            char_min=char_min,
            char_max=char_max,
            hyphen_allowed=hyphen_allowed,
            number_allowed=number_allowed,
            punycode_allowed=punycode_allowed,
            dnssec_enabled=dnssec_enabled,
            rdap_enabled=rdap_enabled,
            rdap_url=rdap_url,
            contact_data=contact_data,
            update_contact_r=update_contact_r,
            update_contact_a=update_contact_a,
            update_contact_t=update_contact_t,
            update_contact_o=update_contact_o,
            update_contact_additional=update_contact_additional,
            update_contact_transfer=update_contact_transfer,
            transfer_authcode=transfer_authcode,
        )

        tld.additional_properties = d
        return tld

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
