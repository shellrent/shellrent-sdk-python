from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.country import Country
    from ..models.legal_entity import LegalEntity
    from ..models.tax_regime import TaxRegime


T = TypeVar("T", bound="AccountBilling")


@_attrs_define
class AccountBilling:
    account_billing_id: int
    legal_entity: LegalEntity
    tax_regime: TaxRegime
    organization: None | str
    name: None | str
    surname: None | str
    address: str
    city: str
    state: str
    postal_code: str
    country: Country
    gender: None | str
    birth_date: datetime.date | None
    birth_place: None | str
    phone: str
    vat_number: None | str
    is_vat_group: bool
    fiscal_code: str
    edocument_pec: None | str
    edocument_code: None | str
    exporter_expiry: datetime.date | None
    exporter_number: None | str
    exporter_date: datetime.date | None
    is_split_payment: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_billing_id = self.account_billing_id

        legal_entity = self.legal_entity.to_dict()

        tax_regime = self.tax_regime.to_dict()

        organization: None | str
        organization = self.organization

        name: None | str
        name = self.name

        surname: None | str
        surname = self.surname

        address = self.address

        city = self.city

        state = self.state

        postal_code = self.postal_code

        country = self.country.to_dict()

        gender: None | str
        gender = self.gender

        birth_date: None | str
        if isinstance(self.birth_date, datetime.date):
            birth_date = self.birth_date.isoformat()
        else:
            birth_date = self.birth_date

        birth_place: None | str
        birth_place = self.birth_place

        phone = self.phone

        vat_number: None | str
        vat_number = self.vat_number

        is_vat_group = self.is_vat_group

        fiscal_code = self.fiscal_code

        edocument_pec: None | str
        edocument_pec = self.edocument_pec

        edocument_code: None | str
        edocument_code = self.edocument_code

        exporter_expiry: None | str
        if isinstance(self.exporter_expiry, datetime.date):
            exporter_expiry = self.exporter_expiry.isoformat()
        else:
            exporter_expiry = self.exporter_expiry

        exporter_number: None | str
        exporter_number = self.exporter_number

        exporter_date: None | str
        if isinstance(self.exporter_date, datetime.date):
            exporter_date = self.exporter_date.isoformat()
        else:
            exporter_date = self.exporter_date

        is_split_payment = self.is_split_payment

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "account_billing_id": account_billing_id,
                "legal_entity": legal_entity,
                "tax_regime": tax_regime,
                "organization": organization,
                "name": name,
                "surname": surname,
                "address": address,
                "city": city,
                "state": state,
                "postal_code": postal_code,
                "country": country,
                "gender": gender,
                "birth_date": birth_date,
                "birth_place": birth_place,
                "phone": phone,
                "vat_number": vat_number,
                "is_vat_group": is_vat_group,
                "fiscal_code": fiscal_code,
                "edocument_pec": edocument_pec,
                "edocument_code": edocument_code,
                "exporter_expiry": exporter_expiry,
                "exporter_number": exporter_number,
                "exporter_date": exporter_date,
                "is_split_payment": is_split_payment,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.country import Country
        from ..models.legal_entity import LegalEntity
        from ..models.tax_regime import TaxRegime

        d = dict(src_dict)
        account_billing_id = d.pop("account_billing_id")

        legal_entity = LegalEntity.from_dict(d.pop("legal_entity"))

        tax_regime = TaxRegime.from_dict(d.pop("tax_regime"))

        def _parse_organization(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        organization = _parse_organization(d.pop("organization"))

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        def _parse_surname(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        surname = _parse_surname(d.pop("surname"))

        address = d.pop("address")

        city = d.pop("city")

        state = d.pop("state")

        postal_code = d.pop("postal_code")

        country = Country.from_dict(d.pop("country"))

        def _parse_gender(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        gender = _parse_gender(d.pop("gender"))

        def _parse_birth_date(data: object) -> datetime.date | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                birth_date_type_0 = datetime.date.fromisoformat(data)

                return birth_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None, data)

        birth_date = _parse_birth_date(d.pop("birth_date"))

        def _parse_birth_place(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        birth_place = _parse_birth_place(d.pop("birth_place"))

        phone = d.pop("phone")

        def _parse_vat_number(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        vat_number = _parse_vat_number(d.pop("vat_number"))

        is_vat_group = d.pop("is_vat_group")

        fiscal_code = d.pop("fiscal_code")

        def _parse_edocument_pec(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        edocument_pec = _parse_edocument_pec(d.pop("edocument_pec"))

        def _parse_edocument_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        edocument_code = _parse_edocument_code(d.pop("edocument_code"))

        def _parse_exporter_expiry(data: object) -> datetime.date | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                exporter_expiry_type_0 = datetime.date.fromisoformat(data)

                return exporter_expiry_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None, data)

        exporter_expiry = _parse_exporter_expiry(d.pop("exporter_expiry"))

        def _parse_exporter_number(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        exporter_number = _parse_exporter_number(d.pop("exporter_number"))

        def _parse_exporter_date(data: object) -> datetime.date | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                exporter_date_type_0 = datetime.date.fromisoformat(data)

                return exporter_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None, data)

        exporter_date = _parse_exporter_date(d.pop("exporter_date"))

        is_split_payment = d.pop("is_split_payment")

        account_billing = cls(
            account_billing_id=account_billing_id,
            legal_entity=legal_entity,
            tax_regime=tax_regime,
            organization=organization,
            name=name,
            surname=surname,
            address=address,
            city=city,
            state=state,
            postal_code=postal_code,
            country=country,
            gender=gender,
            birth_date=birth_date,
            birth_place=birth_place,
            phone=phone,
            vat_number=vat_number,
            is_vat_group=is_vat_group,
            fiscal_code=fiscal_code,
            edocument_pec=edocument_pec,
            edocument_code=edocument_code,
            exporter_expiry=exporter_expiry,
            exporter_number=exporter_number,
            exporter_date=exporter_date,
            is_split_payment=is_split_payment,
        )

        account_billing.additional_properties = d
        return account_billing

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
