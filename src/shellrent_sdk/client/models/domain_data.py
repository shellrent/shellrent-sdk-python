from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DomainData")


@_attrs_define
class DomainData:
    """Data of the domain at the registry"""

    registry_status: None | str
    """ Status of the domain as the registry reports it, for example `ok`, `clientTransferProhibited` or
    `pendingDelete` """
    incoming_authcode: None | str
    """ Authcode given for the incoming transfer of the domain; null without the `domains:secrets` scope """
    outgoing_authcode: None | str
    """ Authcode to transfer the domain to another registrar; null without the `domains:secrets` scope """
    registry_nameservers: None | str
    """ Nameservers of the domain at the registry, as a text in the format of the registry (usually hostnames
    separated by commas) """
    registry_expiry: datetime.datetime | None
    """ Expiry of the domain at the registry """
    registry_created: datetime.datetime | None
    """ Registration of the domain at the registry """
    registry_updated: datetime.datetime | None
    """ Last update of the domain at the registry """
    registry_deletion: datetime.datetime | None
    """ Deletion of the domain at the registry, when the registry reports one """
    date_deactivation: datetime.datetime | None
    """ When these data were deactivated because the registrar no longer has the domain (for example after an
    outgoing transfer); null while they are active """
    identity_validation_status: None | str
    """ Status of the validation of the identity of the registrant: `VERIFIED`, `NOT_VERIFIED`, `PENDING` or
    `FAILED` """
    is_on_hold: bool
    """ Whether the domain is on hold at the registry (status `clientHold`) """
    transfer_wrong_authcode: bool | None
    """ Whether the incoming transfer failed because of a wrong authcode; null when not known """
    transfer_locked: bool | None
    """ Whether the incoming transfer failed because the domain is locked at the current registrar; null when not
    known """
    date_created: datetime.datetime
    """ When these data were recorded: a new version is recorded each time the data at the registry change """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        registry_status: None | str
        registry_status = self.registry_status

        incoming_authcode: None | str
        incoming_authcode = self.incoming_authcode

        outgoing_authcode: None | str
        outgoing_authcode = self.outgoing_authcode

        registry_nameservers: None | str
        registry_nameservers = self.registry_nameservers

        registry_expiry: None | str
        if isinstance(self.registry_expiry, datetime.datetime):
            registry_expiry = self.registry_expiry.isoformat()
        else:
            registry_expiry = self.registry_expiry

        registry_created: None | str
        if isinstance(self.registry_created, datetime.datetime):
            registry_created = self.registry_created.isoformat()
        else:
            registry_created = self.registry_created

        registry_updated: None | str
        if isinstance(self.registry_updated, datetime.datetime):
            registry_updated = self.registry_updated.isoformat()
        else:
            registry_updated = self.registry_updated

        registry_deletion: None | str
        if isinstance(self.registry_deletion, datetime.datetime):
            registry_deletion = self.registry_deletion.isoformat()
        else:
            registry_deletion = self.registry_deletion

        date_deactivation: None | str
        if isinstance(self.date_deactivation, datetime.datetime):
            date_deactivation = self.date_deactivation.isoformat()
        else:
            date_deactivation = self.date_deactivation

        identity_validation_status: None | str
        identity_validation_status = self.identity_validation_status

        is_on_hold = self.is_on_hold

        transfer_wrong_authcode: bool | None
        transfer_wrong_authcode = self.transfer_wrong_authcode

        transfer_locked: bool | None
        transfer_locked = self.transfer_locked

        date_created = self.date_created.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "registry_status": registry_status,
                "incoming_authcode": incoming_authcode,
                "outgoing_authcode": outgoing_authcode,
                "registry_nameservers": registry_nameservers,
                "registry_expiry": registry_expiry,
                "registry_created": registry_created,
                "registry_updated": registry_updated,
                "registry_deletion": registry_deletion,
                "date_deactivation": date_deactivation,
                "identity_validation_status": identity_validation_status,
                "is_on_hold": is_on_hold,
                "transfer_wrong_authcode": transfer_wrong_authcode,
                "transfer_locked": transfer_locked,
                "date_created": date_created,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_registry_status(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        registry_status = _parse_registry_status(d.pop("registry_status"))

        def _parse_incoming_authcode(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        incoming_authcode = _parse_incoming_authcode(d.pop("incoming_authcode"))

        def _parse_outgoing_authcode(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        outgoing_authcode = _parse_outgoing_authcode(d.pop("outgoing_authcode"))

        def _parse_registry_nameservers(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        registry_nameservers = _parse_registry_nameservers(d.pop("registry_nameservers"))

        def _parse_registry_expiry(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                registry_expiry_type_0 = datetime.datetime.fromisoformat(data)

                return registry_expiry_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        registry_expiry = _parse_registry_expiry(d.pop("registry_expiry"))

        def _parse_registry_created(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                registry_created_type_0 = datetime.datetime.fromisoformat(data)

                return registry_created_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        registry_created = _parse_registry_created(d.pop("registry_created"))

        def _parse_registry_updated(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                registry_updated_type_0 = datetime.datetime.fromisoformat(data)

                return registry_updated_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        registry_updated = _parse_registry_updated(d.pop("registry_updated"))

        def _parse_registry_deletion(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                registry_deletion_type_0 = datetime.datetime.fromisoformat(data)

                return registry_deletion_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        registry_deletion = _parse_registry_deletion(d.pop("registry_deletion"))

        def _parse_date_deactivation(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_deactivation_type_0 = datetime.datetime.fromisoformat(data)

                return date_deactivation_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        date_deactivation = _parse_date_deactivation(d.pop("date_deactivation"))

        def _parse_identity_validation_status(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        identity_validation_status = _parse_identity_validation_status(
            d.pop("identity_validation_status")
        )

        is_on_hold = d.pop("is_on_hold")

        def _parse_transfer_wrong_authcode(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        transfer_wrong_authcode = _parse_transfer_wrong_authcode(d.pop("transfer_wrong_authcode"))

        def _parse_transfer_locked(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        transfer_locked = _parse_transfer_locked(d.pop("transfer_locked"))

        date_created = datetime.datetime.fromisoformat(d.pop("date_created"))

        domain_data = cls(
            registry_status=registry_status,
            incoming_authcode=incoming_authcode,
            outgoing_authcode=outgoing_authcode,
            registry_nameservers=registry_nameservers,
            registry_expiry=registry_expiry,
            registry_created=registry_created,
            registry_updated=registry_updated,
            registry_deletion=registry_deletion,
            date_deactivation=date_deactivation,
            identity_validation_status=identity_validation_status,
            is_on_hold=is_on_hold,
            transfer_wrong_authcode=transfer_wrong_authcode,
            transfer_locked=transfer_locked,
            date_created=date_created,
        )

        domain_data.additional_properties = d
        return domain_data

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
