from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.microsoft_365_tenant import Microsoft365Tenant


T = TypeVar("T", bound="Microsoft365")


@_attrs_define
class Microsoft365:
    microsoft365_id: int
    purchase_id: int
    tenant_id: int | None
    service_name: None | str
    purchase_name: None | str
    supplier_code: None | str
    supplier_status: None | str
    order_code: None | str
    order_reference: None | str
    order_status: None | str
    order_need_submit: bool
    autorenew_enabled: bool
    is_trial: bool
    subscription_activation_date: datetime.date | None
    subscription_expiry_date: datetime.date | None
    tenant: Microsoft365Tenant | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.microsoft_365_tenant import Microsoft365Tenant

        microsoft365_id = self.microsoft365_id

        purchase_id = self.purchase_id

        tenant_id: int | None
        tenant_id = self.tenant_id

        service_name: None | str
        service_name = self.service_name

        purchase_name: None | str
        purchase_name = self.purchase_name

        supplier_code: None | str
        supplier_code = self.supplier_code

        supplier_status: None | str
        supplier_status = self.supplier_status

        order_code: None | str
        order_code = self.order_code

        order_reference: None | str
        order_reference = self.order_reference

        order_status: None | str
        order_status = self.order_status

        order_need_submit = self.order_need_submit

        autorenew_enabled = self.autorenew_enabled

        is_trial = self.is_trial

        subscription_activation_date: None | str
        if isinstance(self.subscription_activation_date, datetime.date):
            subscription_activation_date = self.subscription_activation_date.isoformat()
        else:
            subscription_activation_date = self.subscription_activation_date

        subscription_expiry_date: None | str
        if isinstance(self.subscription_expiry_date, datetime.date):
            subscription_expiry_date = self.subscription_expiry_date.isoformat()
        else:
            subscription_expiry_date = self.subscription_expiry_date

        tenant: dict[str, Any] | None
        if isinstance(self.tenant, Microsoft365Tenant):
            tenant = self.tenant.to_dict()
        else:
            tenant = self.tenant

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "microsoft365_id": microsoft365_id,
                "purchase_id": purchase_id,
                "tenant_id": tenant_id,
                "service_name": service_name,
                "purchase_name": purchase_name,
                "supplier_code": supplier_code,
                "supplier_status": supplier_status,
                "order_code": order_code,
                "order_reference": order_reference,
                "order_status": order_status,
                "order_need_submit": order_need_submit,
                "autorenew_enabled": autorenew_enabled,
                "is_trial": is_trial,
                "subscription_activation_date": subscription_activation_date,
                "subscription_expiry_date": subscription_expiry_date,
                "tenant": tenant,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.microsoft_365_tenant import Microsoft365Tenant

        d = dict(src_dict)
        microsoft365_id = d.pop("microsoft365_id")

        purchase_id = d.pop("purchase_id")

        def _parse_tenant_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        tenant_id = _parse_tenant_id(d.pop("tenant_id"))

        def _parse_service_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        service_name = _parse_service_name(d.pop("service_name"))

        def _parse_purchase_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        purchase_name = _parse_purchase_name(d.pop("purchase_name"))

        def _parse_supplier_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        supplier_code = _parse_supplier_code(d.pop("supplier_code"))

        def _parse_supplier_status(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        supplier_status = _parse_supplier_status(d.pop("supplier_status"))

        def _parse_order_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        order_code = _parse_order_code(d.pop("order_code"))

        def _parse_order_reference(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        order_reference = _parse_order_reference(d.pop("order_reference"))

        def _parse_order_status(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        order_status = _parse_order_status(d.pop("order_status"))

        order_need_submit = d.pop("order_need_submit")

        autorenew_enabled = d.pop("autorenew_enabled")

        is_trial = d.pop("is_trial")

        def _parse_subscription_activation_date(data: object) -> datetime.date | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                subscription_activation_date_type_0 = datetime.date.fromisoformat(data)

                return subscription_activation_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None, data)

        subscription_activation_date = _parse_subscription_activation_date(
            d.pop("subscription_activation_date")
        )

        def _parse_subscription_expiry_date(data: object) -> datetime.date | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                subscription_expiry_date_type_0 = datetime.date.fromisoformat(data)

                return subscription_expiry_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None, data)

        subscription_expiry_date = _parse_subscription_expiry_date(
            d.pop("subscription_expiry_date")
        )

        def _parse_tenant(data: object) -> Microsoft365Tenant | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                tenant_type_0 = Microsoft365Tenant.from_dict(data)

                return tenant_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Microsoft365Tenant | None, data)

        tenant = _parse_tenant(d.pop("tenant"))

        microsoft_365 = cls(
            microsoft365_id=microsoft365_id,
            purchase_id=purchase_id,
            tenant_id=tenant_id,
            service_name=service_name,
            purchase_name=purchase_name,
            supplier_code=supplier_code,
            supplier_status=supplier_status,
            order_code=order_code,
            order_reference=order_reference,
            order_status=order_status,
            order_need_submit=order_need_submit,
            autorenew_enabled=autorenew_enabled,
            is_trial=is_trial,
            subscription_activation_date=subscription_activation_date,
            subscription_expiry_date=subscription_expiry_date,
            tenant=tenant,
        )

        microsoft_365.additional_properties = d
        return microsoft_365

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
