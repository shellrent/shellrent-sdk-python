from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domain_contact_data import DomainContactData


T = TypeVar("T", bound="DomainContact")


@_attrs_define
class DomainContact:
    """Contact of a domain at the registry, with its data"""

    domain_contact_id: int
    domain_id: int
    """ Id of the domain (`GET /api/v3/domains/{domain_id}`) """
    type_: str
    """ Role of the contact: `R` (registrant), `A` (administrative), `T` (technical) or `O` (organization) """
    to_sync: bool | None
    """ Whether the contact has changes not yet sent to the registry (`POST
    /api/v3/domains/{domain_id}/contacts/synchronizations`) """
    contact_data: list[DomainContactData]
    """ Data of the contact, one item per field """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        domain_contact_id = self.domain_contact_id

        domain_id = self.domain_id

        type_ = self.type_

        to_sync: bool | None
        to_sync = self.to_sync

        contact_data = []
        for contact_data_item_data in self.contact_data:
            contact_data_item = contact_data_item_data.to_dict()
            contact_data.append(contact_data_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "domain_contact_id": domain_contact_id,
                "domain_id": domain_id,
                "type": type_,
                "to_sync": to_sync,
                "contact_data": contact_data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.domain_contact_data import DomainContactData

        d = dict(src_dict)
        domain_contact_id = d.pop("domain_contact_id")

        domain_id = d.pop("domain_id")

        type_ = d.pop("type")

        def _parse_to_sync(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        to_sync = _parse_to_sync(d.pop("to_sync"))

        contact_data = []
        _contact_data = d.pop("contact_data")
        for contact_data_item_data in _contact_data:
            contact_data_item = DomainContactData.from_dict(contact_data_item_data)

            contact_data.append(contact_data_item)

        domain_contact = cls(
            domain_contact_id=domain_contact_id,
            domain_id=domain_id,
            type_=type_,
            to_sync=to_sync,
            contact_data=contact_data,
        )

        domain_contact.additional_properties = d
        return domain_contact

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
