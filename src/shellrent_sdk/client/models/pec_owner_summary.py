from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PecOwnerSummary")


@_attrs_define
class PecOwnerSummary:
    pec_owner_id: int | None
    owner_legal_entity_type: None | str
    admin_first_name: None | str
    admin_last_name: None | str
    admin_email: None | str
    admin_fiscal_code: None | str
    admin_vat_number: None | str
    company_name: None | str
    company_email: None | str
    company_fiscal_code: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pec_owner_id: int | None
        pec_owner_id = self.pec_owner_id

        owner_legal_entity_type: None | str
        owner_legal_entity_type = self.owner_legal_entity_type

        admin_first_name: None | str
        admin_first_name = self.admin_first_name

        admin_last_name: None | str
        admin_last_name = self.admin_last_name

        admin_email: None | str
        admin_email = self.admin_email

        admin_fiscal_code: None | str
        admin_fiscal_code = self.admin_fiscal_code

        admin_vat_number: None | str
        admin_vat_number = self.admin_vat_number

        company_name: None | str
        company_name = self.company_name

        company_email: None | str
        company_email = self.company_email

        company_fiscal_code: None | str
        company_fiscal_code = self.company_fiscal_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pec_owner_id": pec_owner_id,
                "owner_legal_entity_type": owner_legal_entity_type,
                "admin_first_name": admin_first_name,
                "admin_last_name": admin_last_name,
                "admin_email": admin_email,
                "admin_fiscal_code": admin_fiscal_code,
                "admin_vat_number": admin_vat_number,
                "company_name": company_name,
                "company_email": company_email,
                "company_fiscal_code": company_fiscal_code,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_pec_owner_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        pec_owner_id = _parse_pec_owner_id(d.pop("pec_owner_id"))

        def _parse_owner_legal_entity_type(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        owner_legal_entity_type = _parse_owner_legal_entity_type(d.pop("owner_legal_entity_type"))

        def _parse_admin_first_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        admin_first_name = _parse_admin_first_name(d.pop("admin_first_name"))

        def _parse_admin_last_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        admin_last_name = _parse_admin_last_name(d.pop("admin_last_name"))

        def _parse_admin_email(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        admin_email = _parse_admin_email(d.pop("admin_email"))

        def _parse_admin_fiscal_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        admin_fiscal_code = _parse_admin_fiscal_code(d.pop("admin_fiscal_code"))

        def _parse_admin_vat_number(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        admin_vat_number = _parse_admin_vat_number(d.pop("admin_vat_number"))

        def _parse_company_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        company_name = _parse_company_name(d.pop("company_name"))

        def _parse_company_email(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        company_email = _parse_company_email(d.pop("company_email"))

        def _parse_company_fiscal_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        company_fiscal_code = _parse_company_fiscal_code(d.pop("company_fiscal_code"))

        pec_owner_summary = cls(
            pec_owner_id=pec_owner_id,
            owner_legal_entity_type=owner_legal_entity_type,
            admin_first_name=admin_first_name,
            admin_last_name=admin_last_name,
            admin_email=admin_email,
            admin_fiscal_code=admin_fiscal_code,
            admin_vat_number=admin_vat_number,
            company_name=company_name,
            company_email=company_email,
            company_fiscal_code=company_fiscal_code,
        )

        pec_owner_summary.additional_properties = d
        return pec_owner_summary

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
