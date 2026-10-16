from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PecDomain")


@_attrs_define
class PecDomain:
    """Domain certified for PEC (certified email, Posta Elettronica Certificata), whose mailboxes have its name after the
    `@`

    """

    pec_domain_id: int
    purchase_id: int | None
    """ Id of the purchase of the PEC domain (`GET /api/v3/purchases/{purchase_id}`) """
    purchase_name: None | str
    """ Name of the purchase object, as `purchase_name.object_name` of the purchase """
    purchase_status_code: None | str
    """ Status code of the purchase, for example `DELIVERED_V2` or `NEW_V2` (not active yet) """
    purchase_pec_owner_id: int | None
    """ Id of the current owner of the PEC domain, as `pec_owner_id` in the owner changes """
    domain: None | str
    provider_domain_id: None | str
    """ Id of the domain at Aruba, the PEC provider; null until the domain is certified there """
    transfer_in: bool | None
    """ Whether the PEC domain already existed at the provider and was transferred to us (incoming transfer) """
    force_decertify_domain: bool
    """ Whether the activation is stopped because the provider refused to certify the domain: the domain must be
    decertified first """
    aruba_public: bool
    """ Whether it is a public PEC domain of Aruba, shared by many customers (for example `pec.it`) """
    shellrent_public: bool
    """ Whether it is one of our public PEC domains, shared by many customers (for example `postacert.eu`) """
    can_require_owner_change: bool
    """ Whether an owner change can be requested now (`POST /api/v3/pec-domains/{pec_domain_id}/owner-changes`):
    false when the purchase is not active, when another request was not approved or when the domain is not at the
    provider yet """
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

        transfer_in: bool | None
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

        def _parse_transfer_in(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        transfer_in = _parse_transfer_in(d.pop("transfer_in"))

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
