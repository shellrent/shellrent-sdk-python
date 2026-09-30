from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PecMailboxOwnerChangeCreateRequest")


@_attrs_define
class PecMailboxOwnerChangeCreateRequest:
    owner_id: int
    """ ID of an existing PEC owner profile to assign to the mailbox """
    contract_upload_id: int
    """ ID of contract document uploaded with /api/v3/upload """
    identity_document_upload_id: int
    """ ID of identity document uploaded with /api/v3/upload """
    order_module_upload_id: int
    """ ID of order module document uploaded with /api/v3/upload """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        owner_id = self.owner_id

        contract_upload_id = self.contract_upload_id

        identity_document_upload_id = self.identity_document_upload_id

        order_module_upload_id = self.order_module_upload_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "owner_id": owner_id,
                "contract_upload_id": contract_upload_id,
                "identity_document_upload_id": identity_document_upload_id,
                "order_module_upload_id": order_module_upload_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        owner_id = d.pop("owner_id")

        contract_upload_id = d.pop("contract_upload_id")

        identity_document_upload_id = d.pop("identity_document_upload_id")

        order_module_upload_id = d.pop("order_module_upload_id")

        pec_mailbox_owner_change_create_request = cls(
            owner_id=owner_id,
            contract_upload_id=contract_upload_id,
            identity_document_upload_id=identity_document_upload_id,
            order_module_upload_id=order_module_upload_id,
        )

        pec_mailbox_owner_change_create_request.additional_properties = d
        return pec_mailbox_owner_change_create_request

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
