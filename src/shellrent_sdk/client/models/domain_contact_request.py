from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.domain_contact_request_contact_data_item import (
        DomainContactRequestContactDataItem,
    )


T = TypeVar("T", bound="DomainContactRequest")


@_attrs_define
class DomainContactRequest:
    contact_data: list[DomainContactRequestContactDataItem]
    """ Fields to change, one item per field; the fields not sent keep their value """

    def to_dict(self) -> dict[str, Any]:
        contact_data = []
        for contact_data_item_data in self.contact_data:
            contact_data_item = contact_data_item_data.to_dict()
            contact_data.append(contact_data_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "contact_data": contact_data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.domain_contact_request_contact_data_item import (
            DomainContactRequestContactDataItem,
        )

        d = dict(src_dict)
        contact_data = []
        _contact_data = d.pop("contact_data")
        for contact_data_item_data in _contact_data:
            contact_data_item = DomainContactRequestContactDataItem.from_dict(
                contact_data_item_data
            )

            contact_data.append(contact_data_item)

        domain_contact_request = cls(
            contact_data=contact_data,
        )

        return domain_contact_request
