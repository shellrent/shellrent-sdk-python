from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SslCertificate")


@_attrs_define
class SslCertificate:
    ssl_certificate_id: int
    purchase_id: int
    domain_name: None | str
    cn_type: None | str
    validation_type: None | str
    san_max: int
    can_reissue: bool
    validation_method: None | str
    valid_to: datetime.datetime | None
    csr_md5_hash: None | str
    csr_sha256_hash: None | str
    certificate_status: None | str
    approver_email: None | str
    admin_first_name: None | str
    admin_last_name: None | str
    admin_organization: None | str
    admin_role: None | str
    admin_email: None | str
    admin_phone_cc: None | str
    admin_phone_number: None | str
    admin_address: None | str
    admin_city: None | str
    admin_state: None | str
    admin_postal_code: None | str
    admin_country: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ssl_certificate_id = self.ssl_certificate_id

        purchase_id = self.purchase_id

        domain_name: None | str
        domain_name = self.domain_name

        cn_type: None | str
        cn_type = self.cn_type

        validation_type: None | str
        validation_type = self.validation_type

        san_max = self.san_max

        can_reissue = self.can_reissue

        validation_method: None | str
        validation_method = self.validation_method

        valid_to: None | str
        if isinstance(self.valid_to, datetime.datetime):
            valid_to = self.valid_to.isoformat()
        else:
            valid_to = self.valid_to

        csr_md5_hash: None | str
        csr_md5_hash = self.csr_md5_hash

        csr_sha256_hash: None | str
        csr_sha256_hash = self.csr_sha256_hash

        certificate_status: None | str
        certificate_status = self.certificate_status

        approver_email: None | str
        approver_email = self.approver_email

        admin_first_name: None | str
        admin_first_name = self.admin_first_name

        admin_last_name: None | str
        admin_last_name = self.admin_last_name

        admin_organization: None | str
        admin_organization = self.admin_organization

        admin_role: None | str
        admin_role = self.admin_role

        admin_email: None | str
        admin_email = self.admin_email

        admin_phone_cc: None | str
        admin_phone_cc = self.admin_phone_cc

        admin_phone_number: None | str
        admin_phone_number = self.admin_phone_number

        admin_address: None | str
        admin_address = self.admin_address

        admin_city: None | str
        admin_city = self.admin_city

        admin_state: None | str
        admin_state = self.admin_state

        admin_postal_code: None | str
        admin_postal_code = self.admin_postal_code

        admin_country: None | str
        admin_country = self.admin_country

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ssl_certificate_id": ssl_certificate_id,
                "purchase_id": purchase_id,
                "domain_name": domain_name,
                "cn_type": cn_type,
                "validation_type": validation_type,
                "san_max": san_max,
                "can_reissue": can_reissue,
                "validation_method": validation_method,
                "valid_to": valid_to,
                "csr_md5_hash": csr_md5_hash,
                "csr_sha256_hash": csr_sha256_hash,
                "certificate_status": certificate_status,
                "approver_email": approver_email,
                "admin_first_name": admin_first_name,
                "admin_last_name": admin_last_name,
                "admin_organization": admin_organization,
                "admin_role": admin_role,
                "admin_email": admin_email,
                "admin_phone_cc": admin_phone_cc,
                "admin_phone_number": admin_phone_number,
                "admin_address": admin_address,
                "admin_city": admin_city,
                "admin_state": admin_state,
                "admin_postal_code": admin_postal_code,
                "admin_country": admin_country,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        ssl_certificate_id = d.pop("ssl_certificate_id")

        purchase_id = d.pop("purchase_id")

        def _parse_domain_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        domain_name = _parse_domain_name(d.pop("domain_name"))

        def _parse_cn_type(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        cn_type = _parse_cn_type(d.pop("cn_type"))

        def _parse_validation_type(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        validation_type = _parse_validation_type(d.pop("validation_type"))

        san_max = d.pop("san_max")

        can_reissue = d.pop("can_reissue")

        def _parse_validation_method(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        validation_method = _parse_validation_method(d.pop("validation_method"))

        def _parse_valid_to(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                valid_to_type_0 = datetime.datetime.fromisoformat(data)

                return valid_to_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        valid_to = _parse_valid_to(d.pop("valid_to"))

        def _parse_csr_md5_hash(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        csr_md5_hash = _parse_csr_md5_hash(d.pop("csr_md5_hash"))

        def _parse_csr_sha256_hash(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        csr_sha256_hash = _parse_csr_sha256_hash(d.pop("csr_sha256_hash"))

        def _parse_certificate_status(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        certificate_status = _parse_certificate_status(d.pop("certificate_status"))

        def _parse_approver_email(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        approver_email = _parse_approver_email(d.pop("approver_email"))

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

        def _parse_admin_organization(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        admin_organization = _parse_admin_organization(d.pop("admin_organization"))

        def _parse_admin_role(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        admin_role = _parse_admin_role(d.pop("admin_role"))

        def _parse_admin_email(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        admin_email = _parse_admin_email(d.pop("admin_email"))

        def _parse_admin_phone_cc(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        admin_phone_cc = _parse_admin_phone_cc(d.pop("admin_phone_cc"))

        def _parse_admin_phone_number(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        admin_phone_number = _parse_admin_phone_number(d.pop("admin_phone_number"))

        def _parse_admin_address(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        admin_address = _parse_admin_address(d.pop("admin_address"))

        def _parse_admin_city(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        admin_city = _parse_admin_city(d.pop("admin_city"))

        def _parse_admin_state(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        admin_state = _parse_admin_state(d.pop("admin_state"))

        def _parse_admin_postal_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        admin_postal_code = _parse_admin_postal_code(d.pop("admin_postal_code"))

        def _parse_admin_country(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        admin_country = _parse_admin_country(d.pop("admin_country"))

        ssl_certificate = cls(
            ssl_certificate_id=ssl_certificate_id,
            purchase_id=purchase_id,
            domain_name=domain_name,
            cn_type=cn_type,
            validation_type=validation_type,
            san_max=san_max,
            can_reissue=can_reissue,
            validation_method=validation_method,
            valid_to=valid_to,
            csr_md5_hash=csr_md5_hash,
            csr_sha256_hash=csr_sha256_hash,
            certificate_status=certificate_status,
            approver_email=approver_email,
            admin_first_name=admin_first_name,
            admin_last_name=admin_last_name,
            admin_organization=admin_organization,
            admin_role=admin_role,
            admin_email=admin_email,
            admin_phone_cc=admin_phone_cc,
            admin_phone_number=admin_phone_number,
            admin_address=admin_address,
            admin_city=admin_city,
            admin_state=admin_state,
            admin_postal_code=admin_postal_code,
            admin_country=admin_country,
        )

        ssl_certificate.additional_properties = d
        return ssl_certificate

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
