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


T = TypeVar("T", bound="Domain")


@_attrs_define
class Domain:
    domain_id: int
    tld_id: int
    domain_name: DomainName
    dns_type: DnsType
    dns_account: None | str
    nameservers: list[str]
    domain_data: DomainData | None
    contacts_count: int
    dnssec_enabled: bool
    date_info_last: datetime.datetime | None
    date_dns_check: datetime.datetime | None
    vanity_nameserver_enabled: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.domain_data import DomainData

        domain_id = self.domain_id

        tld_id = self.tld_id

        domain_name = self.domain_name.to_dict()

        dns_type = self.dns_type.to_dict()

        dns_account: None | str
        dns_account = self.dns_account

        nameservers = self.nameservers

        domain_data: dict[str, Any] | None
        if isinstance(self.domain_data, DomainData):
            domain_data = self.domain_data.to_dict()
        else:
            domain_data = self.domain_data

        contacts_count = self.contacts_count

        dnssec_enabled = self.dnssec_enabled

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
                "dnssec_enabled": dnssec_enabled,
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

        nameservers = cast(list[str], d.pop("nameservers"))

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

        dnssec_enabled = d.pop("dnssec_enabled")

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
            dnssec_enabled=dnssec_enabled,
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
