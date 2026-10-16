from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="PecMailboxOwnerChangeCreateRequest")


@_attrs_define
class PecMailboxOwnerChangeCreateRequest:
    owner_id: int
    """ ID of an existing PEC owner profile to assign to the mailbox """
    contract_upload_id: int
    """ ID of contract document uploaded with `POST /api/v3/uploads` """
    identity_document_upload_id: int
    """ ID of identity document uploaded with `POST /api/v3/uploads` """
    order_module_upload_id: int
    """ ID of order module document uploaded with `POST /api/v3/uploads` """

    def to_dict(self) -> dict[str, Any]:
        owner_id = self.owner_id

        contract_upload_id = self.contract_upload_id

        identity_document_upload_id = self.identity_document_upload_id

        order_module_upload_id = self.order_module_upload_id

        field_dict: dict[str, Any] = {}

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

        return pec_mailbox_owner_change_create_request
