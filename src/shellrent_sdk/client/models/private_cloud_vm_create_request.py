from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PrivateCloudVmCreateRequest")


@_attrs_define
class PrivateCloudVmCreateRequest:
    cpu: int
    ram: int
    disk: int
    server_configuration_id: int | Unset = UNSET
    """ Server configuration ID """
    template_id: int | Unset = UNSET
    """ Server template ID (OS) """
    template_vm_id: int | Unset = UNSET
    """ Template VM ID (optional alternative to configuration/template) """
    ip_address_id: int | Unset = UNSET
    """ Primary IP address ID """
    use_local_ip: bool | Unset = UNSET
    """ Use local IP instead of public IP """
    ssh_key_id: int | Unset = UNSET
    """ SSH key ID to associate with the VM """
    note: str | Unset = UNSET
    """ Optional note """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cpu = self.cpu

        ram = self.ram

        disk = self.disk

        server_configuration_id = self.server_configuration_id

        template_id = self.template_id

        template_vm_id = self.template_vm_id

        ip_address_id = self.ip_address_id

        use_local_ip = self.use_local_ip

        ssh_key_id = self.ssh_key_id

        note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cpu": cpu,
                "ram": ram,
                "disk": disk,
            }
        )
        if server_configuration_id is not UNSET:
            field_dict["server_configuration_id"] = server_configuration_id
        if template_id is not UNSET:
            field_dict["template_id"] = template_id
        if template_vm_id is not UNSET:
            field_dict["template_vm_id"] = template_vm_id
        if ip_address_id is not UNSET:
            field_dict["ip_address_id"] = ip_address_id
        if use_local_ip is not UNSET:
            field_dict["use_local_ip"] = use_local_ip
        if ssh_key_id is not UNSET:
            field_dict["ssh_key_id"] = ssh_key_id
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        cpu = d.pop("cpu")

        ram = d.pop("ram")

        disk = d.pop("disk")

        server_configuration_id = d.pop("server_configuration_id", UNSET)

        template_id = d.pop("template_id", UNSET)

        template_vm_id = d.pop("template_vm_id", UNSET)

        ip_address_id = d.pop("ip_address_id", UNSET)

        use_local_ip = d.pop("use_local_ip", UNSET)

        ssh_key_id = d.pop("ssh_key_id", UNSET)

        note = d.pop("note", UNSET)

        private_cloud_vm_create_request = cls(
            cpu=cpu,
            ram=ram,
            disk=disk,
            server_configuration_id=server_configuration_id,
            template_id=template_id,
            template_vm_id=template_vm_id,
            ip_address_id=ip_address_id,
            use_local_ip=use_local_ip,
            ssh_key_id=ssh_key_id,
            note=note,
        )

        private_cloud_vm_create_request.additional_properties = d
        return private_cloud_vm_create_request

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
