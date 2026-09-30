from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PecDomain")


@_attrs_define
class PecDomain:
    pec_domain_id: int
    purchase_id: int | None
    purchase_name: None | str
    purchase_status_code: None | str
    purchase_pec_owner_id: int | None
    domain: None | str
    provider_domain_id: None | str
    transfer_in: bool
    force_decertify_domain: bool
    aruba_public: bool
    shellrent_public: bool
    can_require_owner_change: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pec_domain_id = self.pec_domain_id

        purchase_id: int | None
        purchase_id = self.purchase_id

        purchase_name: None | str
        purchase_name = self.purchase_name

        purchase_status_code: None | str
        purchase_status_code = self.purchase_status_code

        purchase_pec_owner_id: int | None
        purchase_pec_owner_id = self.purchase_pec_owner_id

        domain: None | str
        domain = self.domain

        provider_domain_id: None | str
        provider_domain_id = self.provider_domain_id

        transfer_in = self.transfer_in

        force_decertify_domain = self.force_decertify_domain

        aruba_public = self.aruba_public

        shellrent_public = self.shellrent_public

        can_require_owner_change = self.can_require_owner_change

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pec_domain_id": pec_domain_id,
                "purchase_id": purchase_id,
                "purchase_name": purchase_name,
                "purchase_status_code": purchase_status_code,
                "purchase_pec_owner_id": purchase_pec_owner_id,
                "domain": domain,
                "provider_domain_id": provider_domain_id,
                "transfer_in": transfer_in,
                "force_decertify_domain": force_decertify_domain,
                "aruba_public": aruba_public,
                "shellrent_public": shellrent_public,
                "can_require_owner_change": can_require_owner_change,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        pec_domain_id = d.pop("pec_domain_id")

        def _parse_purchase_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        purchase_id = _parse_purchase_id(d.pop("purchase_id"))

        def _parse_purchase_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        purchase_name = _parse_purchase_name(d.pop("purchase_name"))

        def _parse_purchase_status_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        purchase_status_code = _parse_purchase_status_code(d.pop("purchase_status_code"))

        def _parse_purchase_pec_owner_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        purchase_pec_owner_id = _parse_purchase_pec_owner_id(d.pop("purchase_pec_owner_id"))

        def _parse_domain(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        domain = _parse_domain(d.pop("domain"))

        def _parse_provider_domain_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        provider_domain_id = _parse_provider_domain_id(d.pop("provider_domain_id"))

        transfer_in = d.pop("transfer_in")

        force_decertify_domain = d.pop("force_decertify_domain")

        aruba_public = d.pop("aruba_public")

        shellrent_public = d.pop("shellrent_public")

        can_require_owner_change = d.pop("can_require_owner_change")

        pec_domain = cls(
            pec_domain_id=pec_domain_id,
            purchase_id=purchase_id,
            purchase_name=purchase_name,
            purchase_status_code=purchase_status_code,
            purchase_pec_owner_id=purchase_pec_owner_id,
            domain=domain,
            provider_domain_id=provider_domain_id,
            transfer_in=transfer_in,
            force_decertify_domain=force_decertify_domain,
            aruba_public=aruba_public,
            shellrent_public=shellrent_public,
            can_require_owner_change=can_require_owner_change,
        )

        pec_domain.additional_properties = d
        return pec_domain

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
