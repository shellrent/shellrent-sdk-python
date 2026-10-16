from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.dns_type import DnsType
    from ..models.domain_data import DomainData
    from ..models.domain_name import DomainName
    from ..models.domain_nameserver import DomainNameserver


T = TypeVar("T", bound="Domain")


@_attrs_define
class Domain:
    """Domain of the account, with its nameservers and its data at the registry"""

    domain_id: int
    tld_id: int
    """ Id of the TLD of the domain (`GET /api/v3/tlds/{tld_id}`) """
    domain_name: DomainName
    """ Name of a domain, whole and split into name and extension, in Unicode and in punycode """
    dns_type: DnsType
    """ Nameserver type of a domain, which decides where its DNS zone is managed """
    dns_account: None | str
    """ Email of the Cloudflare account that manages the DNS zone, with the Cloudflare nameservers; null with the
    other nameserver types, and when the zone is on our own Cloudflare account """
    nameservers: list[DomainNameserver]
    """ Nameservers of the domain; `sort` gives their order """
    domain_data: DomainData | None
    """ Data of the domain at the registry; null when there are none """
    contacts_count: int
    """ Number of active contacts of the domain """
    date_info_last: datetime.datetime | None
    """ When the data of the domain were last requested from the registry """
    date_dns_check: datetime.datetime | None
    """ When the DNS zone and the DNSSEC of the domain were last checked """
    vanity_nameserver_enabled: bool
    """ Whether the domain uses vanity nameservers: our nameservers with hostnames of the domain itself (for example
    `ns1.example.com`) """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.domain_data import DomainData

        domain_id = self.domain_id

        tld_id = self.tld_id

        domain_name = self.domain_name.to_dict()

        dns_type = self.dns_type.to_dict()

        dns_account: None | str
        dns_account = self.dns_account

        nameservers = []
        for nameservers_item_data in self.nameservers:
            nameservers_item = nameservers_item_data.to_dict()
            nameservers.append(nameservers_item)

        domain_data: dict[str, Any] | None
        if isinstance(self.domain_data, DomainData):
            domain_data = self.domain_data.to_dict()
        else:
            domain_data = self.domain_data

        contacts_count = self.contacts_count

        date_info_last: None | str
        if isinstance(self.date_info_last, datetime.datetime):
            date_info_last = self.date_info_last.isoformat()
        else:
            date_info_last = self.date_info_last

        date_dns_check: None | str
        if isinstance(self.date_dns_check, datetime.datetime):
            date_dns_check = self.date_dns_check.isoformat()
        else:
            date_dns_check = self.date_dns_check

        vanity_nameserver_enabled = self.vanity_nameserver_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "domain_id": domain_id,
                "tld_id": tld_id,
                "domain_name": domain_name,
                "dns_type": dns_type,
                "dns_account": dns_account,
                "nameservers": nameservers,
                "domain_data": domain_data,
                "contacts_count": contacts_count,
                "date_info_last": date_info_last,
                "date_dns_check": date_dns_check,
                "vanity_nameserver_enabled": vanity_nameserver_enabled,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.dns_type import DnsType
        from ..models.domain_data import DomainData
        from ..models.domain_name import DomainName
        from ..models.domain_nameserver import DomainNameserver

        d = dict(src_dict)
        domain_id = d.pop("domain_id")

        tld_id = d.pop("tld_id")

        domain_name = DomainName.from_dict(d.pop("domain_name"))

        dns_type = DnsType.from_dict(d.pop("dns_type"))

        def _parse_dns_account(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        dns_account = _parse_dns_account(d.pop("dns_account"))

        nameservers = []
        _nameservers = d.pop("nameservers")
        for nameservers_item_data in _nameservers:
            nameservers_item = DomainNameserver.from_dict(nameservers_item_data)

            nameservers.append(nameservers_item)

        def _parse_domain_data(data: object) -> DomainData | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                domain_data_type_0 = DomainData.from_dict(data)

                return domain_data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DomainData | None, data)

        domain_data = _parse_domain_data(d.pop("domain_data"))

        contacts_count = d.pop("contacts_count")

        def _parse_date_info_last(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_info_last_type_0 = datetime.datetime.fromisoformat(data)

                return date_info_last_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        date_info_last = _parse_date_info_last(d.pop("date_info_last"))

        def _parse_date_dns_check(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_dns_check_type_0 = datetime.datetime.fromisoformat(data)

                return date_dns_check_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        date_dns_check = _parse_date_dns_check(d.pop("date_dns_check"))

        vanity_nameserver_enabled = d.pop("vanity_nameserver_enabled")

        domain = cls(
            domain_id=domain_id,
            tld_id=tld_id,
            domain_name=domain_name,
            dns_type=dns_type,
            dns_account=dns_account,
            nameservers=nameservers,
            domain_data=domain_data,
            contacts_count=contacts_count,
            date_info_last=date_info_last,
            date_dns_check=date_dns_check,
            vanity_nameserver_enabled=vanity_nameserver_enabled,
        )

        domain.additional_properties = d
        return domain

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
