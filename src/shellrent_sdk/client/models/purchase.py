from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.account import Account
    from ..models.account_billing import AccountBilling
    from ..models.amount import Amount
    from ..models.billing_data import BillingData
    from ..models.purchase_name import PurchaseName
    from ..models.purchase_provisioning_status import PurchaseProvisioningStatus
    from ..models.purchase_status import PurchaseStatus
    from ..models.recurrence import Recurrence
    from ..models.service import Service
    from ..models.task import Task


T = TypeVar("T", bound="Purchase")


@_attrs_define
class Purchase:
    purchase_id: int
    """ ID of purchase """
    account: Account | None
    """ Account information of the user owner of the purchase. NULL if the purchase is not billed to a Reseller. """
    service: Service
    billing: AccountBilling
    recurrence: Recurrence
    recurrence_default: Recurrence
    purchase_id_primary: int | None
    """ ID of primary purchase if this is an additional purchase. """
    purchase_status: PurchaseStatus
    purchase_provisioning_status: PurchaseProvisioningStatus
    purchase_name: PurchaseName
    activation_quantity: int
    """ Quantity (instances) purchased. """
    quantity: int
    """ Current purchase quantity (instances). """
    activation_price: Amount
    renew_price: Amount | None
    """ Renew price (applied on recurring purchases only). """
    restore_price: Amount | None
    """ Restore/reactivation price (applied on domains only). """
    date_activation: datetime.date | None
    """ Purchase date. """
    date_activation_start: datetime.date | None
    """ Date when the activation started. """
    date_expiry: datetime.date | None
    """ Purchase expiration date (applied on recurring purchases only). """
    date_dismission: datetime.date | None
    """ Purchase dismission date. """
    do_not_renew: bool
    """ Tells if purchase has to be renewed. """
    suspended: bool
    """ Tells if purchase is currently suspended. """
    comment: str
    """ User comment (will be included in invoice description). """
    billing_data: BillingData
    tasks: list[Task]
    """ Tasks currently running on the purchase. """
    purchase_additionals: list[int]
    """ Collection of IDs of active additional purchases for this purchase. """
    domain_id: int | None
    """ ID of the domain associated with this purchase. """
    server_id: int | None
    """ ID of the server associated with this purchase. """
    ssl_certificate_id: int | None
    """ ID of the SSL certificate associated with this purchase. """
    pec_id: int | None
    """ ID of the PEC associated with this purchase. """
    pec_domain_id: int | None
    """ ID of the PEC domain associated with this purchase. """
    hosting_id: int | None
    """ ID of the web hosting associated with this purchase. """
    monitoring_id: int | None
    """ ID of the monitoring service associated with this purchase. """
    license_id: int | None
    """ ID of the license associated with this purchase. """
    microsoft365_id: int | None
    """ ID of the Microsoft 365 subscription associated with this purchase. """
    securemail_id: int | None
    """ ID of the SecureMail by LibraESVA associated with this purchase. """
    cloud_storage_id: int | None
    """ ID of the cloud storage associated with this purchase. """
    object_storage_id: int | None
    """ ID of the object storage associated with this purchase. """
    veeam_baas_id: int | None
    """ ID of the Veeam Backup as a Service associated with this purchase. """
    date_created: datetime.datetime
    """ Datetime when the purchase was first created. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.account import Account
        from ..models.amount import Amount

        purchase_id = self.purchase_id

        account: dict[str, Any] | None
        if isinstance(self.account, Account):
            account = self.account.to_dict()
        else:
            account = self.account

        service = self.service.to_dict()

        billing = self.billing.to_dict()

        recurrence = self.recurrence.to_dict()

        recurrence_default = self.recurrence_default.to_dict()

        purchase_id_primary: int | None
        purchase_id_primary = self.purchase_id_primary

        purchase_status = self.purchase_status.to_dict()

        purchase_provisioning_status = self.purchase_provisioning_status.to_dict()

        purchase_name = self.purchase_name.to_dict()

        activation_quantity = self.activation_quantity

        quantity = self.quantity

        activation_price = self.activation_price.to_dict()

        renew_price: dict[str, Any] | None
        if isinstance(self.renew_price, Amount):
            renew_price = self.renew_price.to_dict()
        else:
            renew_price = self.renew_price

        restore_price: dict[str, Any] | None
        if isinstance(self.restore_price, Amount):
            restore_price = self.restore_price.to_dict()
        else:
            restore_price = self.restore_price

        date_activation: None | str
        if isinstance(self.date_activation, datetime.date):
            date_activation = self.date_activation.isoformat()
        else:
            date_activation = self.date_activation

        date_activation_start: None | str
        if isinstance(self.date_activation_start, datetime.date):
            date_activation_start = self.date_activation_start.isoformat()
        else:
            date_activation_start = self.date_activation_start

        date_expiry: None | str
        if isinstance(self.date_expiry, datetime.date):
            date_expiry = self.date_expiry.isoformat()
        else:
            date_expiry = self.date_expiry

        date_dismission: None | str
        if isinstance(self.date_dismission, datetime.date):
            date_dismission = self.date_dismission.isoformat()
        else:
            date_dismission = self.date_dismission

        do_not_renew = self.do_not_renew

        suspended = self.suspended

        comment = self.comment

        billing_data = self.billing_data.to_dict()

        tasks = []
        for tasks_item_data in self.tasks:
            tasks_item = tasks_item_data.to_dict()
            tasks.append(tasks_item)

        purchase_additionals = self.purchase_additionals

        domain_id: int | None
        domain_id = self.domain_id

        server_id: int | None
        server_id = self.server_id

        ssl_certificate_id: int | None
        ssl_certificate_id = self.ssl_certificate_id

        pec_id: int | None
        pec_id = self.pec_id

        pec_domain_id: int | None
        pec_domain_id = self.pec_domain_id

        hosting_id: int | None
        hosting_id = self.hosting_id

        monitoring_id: int | None
        monitoring_id = self.monitoring_id

        license_id: int | None
        license_id = self.license_id

        microsoft365_id: int | None
        microsoft365_id = self.microsoft365_id

        securemail_id: int | None
        securemail_id = self.securemail_id

        cloud_storage_id: int | None
        cloud_storage_id = self.cloud_storage_id

        object_storage_id: int | None
        object_storage_id = self.object_storage_id

        veeam_baas_id: int | None
        veeam_baas_id = self.veeam_baas_id

        date_created = self.date_created.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "purchase_id": purchase_id,
                "account": account,
                "service": service,
                "billing": billing,
                "recurrence": recurrence,
                "recurrence_default": recurrence_default,
                "purchase_id_primary": purchase_id_primary,
                "purchase_status": purchase_status,
                "purchase_provisioning_status": purchase_provisioning_status,
                "purchase_name": purchase_name,
                "activation_quantity": activation_quantity,
                "quantity": quantity,
                "activation_price": activation_price,
                "renew_price": renew_price,
                "restore_price": restore_price,
                "date_activation": date_activation,
                "date_activation_start": date_activation_start,
                "date_expiry": date_expiry,
                "date_dismission": date_dismission,
                "do_not_renew": do_not_renew,
                "suspended": suspended,
                "comment": comment,
                "billing_data": billing_data,
                "tasks": tasks,
                "purchase_additionals": purchase_additionals,
                "domain_id": domain_id,
                "server_id": server_id,
                "ssl_certificate_id": ssl_certificate_id,
                "pec_id": pec_id,
                "pec_domain_id": pec_domain_id,
                "hosting_id": hosting_id,
                "monitoring_id": monitoring_id,
                "license_id": license_id,
                "microsoft365_id": microsoft365_id,
                "securemail_id": securemail_id,
                "cloud_storage_id": cloud_storage_id,
                "object_storage_id": object_storage_id,
                "veeam_baas_id": veeam_baas_id,
                "date_created": date_created,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.account import Account
        from ..models.account_billing import AccountBilling
        from ..models.amount import Amount
        from ..models.billing_data import BillingData
        from ..models.purchase_name import PurchaseName
        from ..models.purchase_provisioning_status import (
            PurchaseProvisioningStatus,
        )
        from ..models.purchase_status import PurchaseStatus
        from ..models.recurrence import Recurrence
        from ..models.service import Service
        from ..models.task import Task

        d = dict(src_dict)
        purchase_id = d.pop("purchase_id")

        def _parse_account(data: object) -> Account | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                account_type_0 = Account.from_dict(data)

                return account_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Account | None, data)

        account = _parse_account(d.pop("account"))

        service = Service.from_dict(d.pop("service"))

        billing = AccountBilling.from_dict(d.pop("billing"))

        recurrence = Recurrence.from_dict(d.pop("recurrence"))

        recurrence_default = Recurrence.from_dict(d.pop("recurrence_default"))

        def _parse_purchase_id_primary(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        purchase_id_primary = _parse_purchase_id_primary(d.pop("purchase_id_primary"))

        purchase_status = PurchaseStatus.from_dict(d.pop("purchase_status"))

        purchase_provisioning_status = PurchaseProvisioningStatus.from_dict(
            d.pop("purchase_provisioning_status")
        )

        purchase_name = PurchaseName.from_dict(d.pop("purchase_name"))

        activation_quantity = d.pop("activation_quantity")

        quantity = d.pop("quantity")

        activation_price = Amount.from_dict(d.pop("activation_price"))

        def _parse_renew_price(data: object) -> Amount | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                renew_price_type_0 = Amount.from_dict(data)

                return renew_price_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Amount | None, data)

        renew_price = _parse_renew_price(d.pop("renew_price"))

        def _parse_restore_price(data: object) -> Amount | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                restore_price_type_0 = Amount.from_dict(data)

                return restore_price_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Amount | None, data)

        restore_price = _parse_restore_price(d.pop("restore_price"))

        def _parse_date_activation(data: object) -> datetime.date | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_activation_type_0 = datetime.date.fromisoformat(data)

                return date_activation_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None, data)

        date_activation = _parse_date_activation(d.pop("date_activation"))

        def _parse_date_activation_start(data: object) -> datetime.date | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_activation_start_type_0 = datetime.date.fromisoformat(data)

                return date_activation_start_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None, data)

        date_activation_start = _parse_date_activation_start(d.pop("date_activation_start"))

        def _parse_date_expiry(data: object) -> datetime.date | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_expiry_type_0 = datetime.date.fromisoformat(data)

                return date_expiry_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None, data)

        date_expiry = _parse_date_expiry(d.pop("date_expiry"))

        def _parse_date_dismission(data: object) -> datetime.date | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_dismission_type_0 = datetime.date.fromisoformat(data)

                return date_dismission_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None, data)

        date_dismission = _parse_date_dismission(d.pop("date_dismission"))

        do_not_renew = d.pop("do_not_renew")

        suspended = d.pop("suspended")

        comment = d.pop("comment")

        billing_data = BillingData.from_dict(d.pop("billing_data"))

        tasks = []
        _tasks = d.pop("tasks")
        for tasks_item_data in _tasks:
            tasks_item = Task.from_dict(tasks_item_data)

            tasks.append(tasks_item)

        purchase_additionals = cast(list[int], d.pop("purchase_additionals"))

        def _parse_domain_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        domain_id = _parse_domain_id(d.pop("domain_id"))

        def _parse_server_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        server_id = _parse_server_id(d.pop("server_id"))

        def _parse_ssl_certificate_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        ssl_certificate_id = _parse_ssl_certificate_id(d.pop("ssl_certificate_id"))

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

        def _parse_hosting_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        hosting_id = _parse_hosting_id(d.pop("hosting_id"))

        def _parse_monitoring_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        monitoring_id = _parse_monitoring_id(d.pop("monitoring_id"))

        def _parse_license_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        license_id = _parse_license_id(d.pop("license_id"))

        def _parse_microsoft365_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        microsoft365_id = _parse_microsoft365_id(d.pop("microsoft365_id"))

        def _parse_securemail_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        securemail_id = _parse_securemail_id(d.pop("securemail_id"))

        def _parse_cloud_storage_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        cloud_storage_id = _parse_cloud_storage_id(d.pop("cloud_storage_id"))

        def _parse_object_storage_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        object_storage_id = _parse_object_storage_id(d.pop("object_storage_id"))

        def _parse_veeam_baas_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        veeam_baas_id = _parse_veeam_baas_id(d.pop("veeam_baas_id"))

        date_created = datetime.datetime.fromisoformat(d.pop("date_created"))

        purchase = cls(
            purchase_id=purchase_id,
            account=account,
            service=service,
            billing=billing,
            recurrence=recurrence,
            recurrence_default=recurrence_default,
            purchase_id_primary=purchase_id_primary,
            purchase_status=purchase_status,
            purchase_provisioning_status=purchase_provisioning_status,
            purchase_name=purchase_name,
            activation_quantity=activation_quantity,
            quantity=quantity,
            activation_price=activation_price,
            renew_price=renew_price,
            restore_price=restore_price,
            date_activation=date_activation,
            date_activation_start=date_activation_start,
            date_expiry=date_expiry,
            date_dismission=date_dismission,
            do_not_renew=do_not_renew,
            suspended=suspended,
            comment=comment,
            billing_data=billing_data,
            tasks=tasks,
            purchase_additionals=purchase_additionals,
            domain_id=domain_id,
            server_id=server_id,
            ssl_certificate_id=ssl_certificate_id,
            pec_id=pec_id,
            pec_domain_id=pec_domain_id,
            hosting_id=hosting_id,
            monitoring_id=monitoring_id,
            license_id=license_id,
            microsoft365_id=microsoft365_id,
            securemail_id=securemail_id,
            cloud_storage_id=cloud_storage_id,
            object_storage_id=object_storage_id,
            veeam_baas_id=veeam_baas_id,
            date_created=date_created,
        )

        purchase.additional_properties = d
        return purchase

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
