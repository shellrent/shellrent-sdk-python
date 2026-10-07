from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.pec_owner_summary import PecOwnerSummary


T = TypeVar("T", bound="PecOwnerChange")


@_attrs_define
class PecOwnerChange:
    """Request to change the owner of a PEC mailbox or of a PEC domain, with its documents and its status"""

    owner_change_id: int | None
    pec_id: int | None
    """ Id of the PEC mailbox of the request (`GET /api/v3/pec-mailboxes/{pec_id}`); null for the requests of a PEC
    domain """
    pec_domain_id: int | None
    """ Id of the PEC domain of the request (`GET /api/v3/pec-domains/{pec_domain_id}`); null for the requests of a
    mailbox """
    status_code: None | str
    """ Status of the request: `PENDENT` (documents not sent yet), `PENDENT_APPROVAL` (waiting for our approval),
    `APPROVED` or `REJECTED` """
    rejection_reason: None | str
    """ Reason of the rejection; null unless the request was rejected """
    submission_date: datetime.datetime | None
    """ When the documents were sent; null until they are """
    acceptance_date: datetime.datetime | None
    """ When the request was approved """
    rejection_date: datetime.datetime | None
    """ When the request was rejected """
    has_identity_document: bool
    """ Whether the request has the identity document """
    has_contract_document: bool
    """ Whether the request has the contract """
    has_order_module_document: bool
    """ Whether the request has the order form """
    owner_old: PecOwnerSummary
    """ Owner (titolare) of a PEC mailbox or domain: the person and, for organizations, the data of the
    organization; all the fields are null when there is no owner """
    owner_new: PecOwnerSummary
    """ Owner (titolare) of a PEC mailbox or domain: the person and, for organizations, the data of the
    organization; all the fields are null when there is no owner """
    date_created: datetime.datetime | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        owner_change_id: int | None
        owner_change_id = self.owner_change_id

        pec_id: int | None
        pec_id = self.pec_id

        pec_domain_id: int | None
        pec_domain_id = self.pec_domain_id

        status_code: None | str
        status_code = self.status_code

        rejection_reason: None | str
        rejection_reason = self.rejection_reason

        submission_date: None | str
        if isinstance(self.submission_date, datetime.datetime):
            submission_date = self.submission_date.isoformat()
        else:
            submission_date = self.submission_date

        acceptance_date: None | str
        if isinstance(self.acceptance_date, datetime.datetime):
            acceptance_date = self.acceptance_date.isoformat()
        else:
            acceptance_date = self.acceptance_date

        rejection_date: None | str
        if isinstance(self.rejection_date, datetime.datetime):
            rejection_date = self.rejection_date.isoformat()
        else:
            rejection_date = self.rejection_date

        has_identity_document = self.has_identity_document

        has_contract_document = self.has_contract_document

        has_order_module_document = self.has_order_module_document

        owner_old = self.owner_old.to_dict()

        owner_new = self.owner_new.to_dict()

        date_created: None | str
        if isinstance(self.date_created, datetime.datetime):
            date_created = self.date_created.isoformat()
        else:
            date_created = self.date_created

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "owner_change_id": owner_change_id,
                "pec_id": pec_id,
                "pec_domain_id": pec_domain_id,
                "status_code": status_code,
                "rejection_reason": rejection_reason,
                "submission_date": submission_date,
                "acceptance_date": acceptance_date,
                "rejection_date": rejection_date,
                "has_identity_document": has_identity_document,
                "has_contract_document": has_contract_document,
                "has_order_module_document": has_order_module_document,
                "owner_old": owner_old,
                "owner_new": owner_new,
                "date_created": date_created,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.pec_owner_summary import PecOwnerSummary

        d = dict(src_dict)

        def _parse_owner_change_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        owner_change_id = _parse_owner_change_id(d.pop("owner_change_id"))

        def _parse_pec_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        pec_id = _parse_pec_id(d.pop("pec_id"))

        def _parse_pec_domain_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        pec_domain_id = _parse_pec_domain_id(d.pop("pec_domain_id"))

        def _parse_status_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        status_code = _parse_status_code(d.pop("status_code"))

        def _parse_rejection_reason(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        rejection_reason = _parse_rejection_reason(d.pop("rejection_reason"))

        def _parse_submission_date(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                submission_date_type_0 = datetime.datetime.fromisoformat(data)

                return submission_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        submission_date = _parse_submission_date(d.pop("submission_date"))

        def _parse_acceptance_date(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                acceptance_date_type_0 = datetime.datetime.fromisoformat(data)

                return acceptance_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        acceptance_date = _parse_acceptance_date(d.pop("acceptance_date"))

        def _parse_rejection_date(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                rejection_date_type_0 = datetime.datetime.fromisoformat(data)

                return rejection_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        rejection_date = _parse_rejection_date(d.pop("rejection_date"))

        has_identity_document = d.pop("has_identity_document")

        has_contract_document = d.pop("has_contract_document")

        has_order_module_document = d.pop("has_order_module_document")

        owner_old = PecOwnerSummary.from_dict(d.pop("owner_old"))

        owner_new = PecOwnerSummary.from_dict(d.pop("owner_new"))

        def _parse_date_created(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_created_type_0 = datetime.datetime.fromisoformat(data)

                return date_created_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        date_created = _parse_date_created(d.pop("date_created"))

        pec_owner_change = cls(
            owner_change_id=owner_change_id,
            pec_id=pec_id,
            pec_domain_id=pec_domain_id,
            status_code=status_code,
            rejection_reason=rejection_reason,
            submission_date=submission_date,
            acceptance_date=acceptance_date,
            rejection_date=rejection_date,
            has_identity_document=has_identity_document,
            has_contract_document=has_contract_document,
            has_order_module_document=has_order_module_document,
            owner_old=owner_old,
            owner_new=owner_new,
            date_created=date_created,
        )

        pec_owner_change.additional_properties = d
        return pec_owner_change

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
