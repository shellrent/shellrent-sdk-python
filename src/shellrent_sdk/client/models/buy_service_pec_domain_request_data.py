from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.buy_service_pec_domain_request_data_legal_entity import (
    BuyServicePecDomainRequestDataLegalEntity,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="BuyServicePecDomainRequestData")


@_attrs_define
class BuyServicePecDomainRequestData:
    domain_name: str | Unset = UNSET
    """ Domain complete name (with TLD extension), for example: "example.com" or "example.co.uk" """
    legal_entity: BuyServicePecDomainRequestDataLegalEntity | Unset = UNSET
    """ Legal entity of the PEC owner """
    owner: int | Unset = UNSET
    """ Id of the PEC owner, if it already exists """
    admin_first_name: str | Unset = UNSET
    """ First name of the PEC owner """
    admin_last_name: str | Unset = UNSET
    """ Last name of the PEC owner """
    admin_email: str | Unset = UNSET
    """ Email of the PEC owner """
    admin_fiscal_code: str | Unset = UNSET
    """ Fiscal code of the PEC owner """
    admin_post_code: str | Unset = UNSET
    """ Post code of the PEC owner """
    admin_address: str | Unset = UNSET
    """ Address of the PEC owner """
    admin_city: str | Unset = UNSET
    """ City of the PEC owner """
    admin_province: str | Unset = UNSET
    """ Province of the PEC owner """
    admin_phone: str | Unset = UNSET
    """ Phone of the PEC owner """
    cellphone: str | Unset = UNSET
    """ Cellphone of the PEC owner """
    admin_pec_country: str | Unset = UNSET
    """ Country of the PEC owner """
    company_name: str | Unset = UNSET
    """ Name of the company """
    company_fiscal_code: str | Unset = UNSET
    """ Fiscal code of the company """
    admin_vat_number: str | Unset = UNSET
    """ Vat number of the company """
    company_email: str | Unset = UNSET
    """ Email of the company """
    company_address: str | Unset = UNSET
    """ Address of the company """
    company_post_code: str | Unset = UNSET
    """ Post code of the company """
    company_city: str | Unset = UNSET
    """ City of the company """
    company_province: str | Unset = UNSET
    """ Province of the company """
    company_phone: str | Unset = UNSET
    """ Phone of the company """
    company_pec_country: str | Unset = UNSET
    """ Country of the company """
    transferin_document: int | Unset = UNSET
    """ ID of the uploaded file (first file, extension: "pdf") Required only for transfer """
    transferin_contract: int | Unset = UNSET
    """ ID of the uploaded file (first file, extension: "pdf") Required only for transfer """
    transferin_identity_document: int | Unset = UNSET
    """ ID of the uploaded file (first file, extension: "pdf") Required only for transfer """

    def to_dict(self) -> dict[str, Any]:
        domain_name = self.domain_name

        legal_entity: str | Unset = UNSET
        if not isinstance(self.legal_entity, Unset):
            legal_entity = self.legal_entity.value

        owner = self.owner

        admin_first_name = self.admin_first_name

        admin_last_name = self.admin_last_name

        admin_email = self.admin_email

        admin_fiscal_code = self.admin_fiscal_code

        admin_post_code = self.admin_post_code

        admin_address = self.admin_address

        admin_city = self.admin_city

        admin_province = self.admin_province

        admin_phone = self.admin_phone

        cellphone = self.cellphone

        admin_pec_country = self.admin_pec_country

        company_name = self.company_name

        company_fiscal_code = self.company_fiscal_code

        admin_vat_number = self.admin_vat_number

        company_email = self.company_email

        company_address = self.company_address

        company_post_code = self.company_post_code

        company_city = self.company_city

        company_province = self.company_province

        company_phone = self.company_phone

        company_pec_country = self.company_pec_country

        transferin_document = self.transferin_document

        transferin_contract = self.transferin_contract

        transferin_identity_document = self.transferin_identity_document

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if domain_name is not UNSET:
            field_dict["domain_name"] = domain_name
        if legal_entity is not UNSET:
            field_dict["legal_entity"] = legal_entity
        if owner is not UNSET:
            field_dict["owner"] = owner
        if admin_first_name is not UNSET:
            field_dict["admin_first_name"] = admin_first_name
        if admin_last_name is not UNSET:
            field_dict["admin_last_name"] = admin_last_name
        if admin_email is not UNSET:
            field_dict["admin_email"] = admin_email
        if admin_fiscal_code is not UNSET:
            field_dict["admin_fiscal_code"] = admin_fiscal_code
        if admin_post_code is not UNSET:
            field_dict["admin_post_code"] = admin_post_code
        if admin_address is not UNSET:
            field_dict["admin_address"] = admin_address
        if admin_city is not UNSET:
            field_dict["admin_city"] = admin_city
        if admin_province is not UNSET:
            field_dict["admin_province"] = admin_province
        if admin_phone is not UNSET:
            field_dict["admin_phone"] = admin_phone
        if cellphone is not UNSET:
            field_dict["cellphone"] = cellphone
        if admin_pec_country is not UNSET:
            field_dict["admin_pec_country"] = admin_pec_country
        if company_name is not UNSET:
            field_dict["company_name"] = company_name
        if company_fiscal_code is not UNSET:
            field_dict["company_fiscal_code"] = company_fiscal_code
        if admin_vat_number is not UNSET:
            field_dict["admin_vat_number"] = admin_vat_number
        if company_email is not UNSET:
            field_dict["company_email"] = company_email
        if company_address is not UNSET:
            field_dict["company_address"] = company_address
        if company_post_code is not UNSET:
            field_dict["company_post_code"] = company_post_code
        if company_city is not UNSET:
            field_dict["company_city"] = company_city
        if company_province is not UNSET:
            field_dict["company_province"] = company_province
        if company_phone is not UNSET:
            field_dict["company_phone"] = company_phone
        if company_pec_country is not UNSET:
            field_dict["company_pec_country"] = company_pec_country
        if transferin_document is not UNSET:
            field_dict["transferin_document"] = transferin_document
        if transferin_contract is not UNSET:
            field_dict["transferin_contract"] = transferin_contract
        if transferin_identity_document is not UNSET:
            field_dict["transferin_identity_document"] = transferin_identity_document

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        domain_name = d.pop("domain_name", UNSET)

        _legal_entity = d.pop("legal_entity", UNSET)
        legal_entity: BuyServicePecDomainRequestDataLegalEntity | Unset
        if isinstance(_legal_entity, Unset):
            legal_entity = UNSET
        else:
            legal_entity = BuyServicePecDomainRequestDataLegalEntity(_legal_entity)

        owner = d.pop("owner", UNSET)

        admin_first_name = d.pop("admin_first_name", UNSET)

        admin_last_name = d.pop("admin_last_name", UNSET)

        admin_email = d.pop("admin_email", UNSET)

        admin_fiscal_code = d.pop("admin_fiscal_code", UNSET)

        admin_post_code = d.pop("admin_post_code", UNSET)

        admin_address = d.pop("admin_address", UNSET)

        admin_city = d.pop("admin_city", UNSET)

        admin_province = d.pop("admin_province", UNSET)

        admin_phone = d.pop("admin_phone", UNSET)

        cellphone = d.pop("cellphone", UNSET)

        admin_pec_country = d.pop("admin_pec_country", UNSET)

        company_name = d.pop("company_name", UNSET)

        company_fiscal_code = d.pop("company_fiscal_code", UNSET)

        admin_vat_number = d.pop("admin_vat_number", UNSET)

        company_email = d.pop("company_email", UNSET)

        company_address = d.pop("company_address", UNSET)

        company_post_code = d.pop("company_post_code", UNSET)

        company_city = d.pop("company_city", UNSET)

        company_province = d.pop("company_province", UNSET)

        company_phone = d.pop("company_phone", UNSET)

        company_pec_country = d.pop("company_pec_country", UNSET)

        transferin_document = d.pop("transferin_document", UNSET)

        transferin_contract = d.pop("transferin_contract", UNSET)

        transferin_identity_document = d.pop("transferin_identity_document", UNSET)

        buy_service_pec_domain_request_data = cls(
            domain_name=domain_name,
            legal_entity=legal_entity,
            owner=owner,
            admin_first_name=admin_first_name,
            admin_last_name=admin_last_name,
            admin_email=admin_email,
            admin_fiscal_code=admin_fiscal_code,
            admin_post_code=admin_post_code,
            admin_address=admin_address,
            admin_city=admin_city,
            admin_province=admin_province,
            admin_phone=admin_phone,
            cellphone=cellphone,
            admin_pec_country=admin_pec_country,
            company_name=company_name,
            company_fiscal_code=company_fiscal_code,
            admin_vat_number=admin_vat_number,
            company_email=company_email,
            company_address=company_address,
            company_post_code=company_post_code,
            company_city=company_city,
            company_province=company_province,
            company_phone=company_phone,
            company_pec_country=company_pec_country,
            transferin_document=transferin_document,
            transferin_contract=transferin_contract,
            transferin_identity_document=transferin_identity_document,
        )

        return buy_service_pec_domain_request_data
