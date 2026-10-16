from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="PrivateCloudVmCreateRequest")


@_attrs_define
class PrivateCloudVmCreateRequest:
    """Virtual machine to create on the private cloud: `template_vm_id` to copy a template VM, otherwise both
    `server_configuration_id` and `template_id`; and either `ip_address_id` or `use_local_ip` true, not both

    """

    cpu: int
    """ Number of CPU cores (vCPUs) of the virtual machine: between `min_vm_cpu` and `max_vm_cpu` of `GET
    /api/v3/servers/{server_id}/private-cloud`, and within the vCPUs still free on the private cloud """
    ram: int
    """ RAM of the virtual machine, in MB: between `min_vm_ram` and `max_vm_ram` of `GET
    /api/v3/servers/{server_id}/private-cloud`, and within the RAM still free on the private cloud """
    disk: int
    """ Disk space of the virtual machine, in GB: between `min_vm_disk` and `max_vm_disk` of `GET
    /api/v3/servers/{server_id}/private-cloud`, within the disk and backup space still free on the private cloud
    and, with `template_vm_id`, not lower than the disk of the template VM """
    server_configuration_id: int | Unset = UNSET
    """ Server configuration ID """
    template_id: int | Unset = UNSET
    """ Server template ID (OS) """
    template_vm_id: int | Unset = UNSET
    """ Template VM ID (optional alternative to configuration/template) """
    ip_address_id: int | Unset = UNSET
    """ Primary IP address ID """
    use_local_ip: bool | Unset = False
    """ Use local IP instead of public IP """
    ssh_key_id: int | Unset = UNSET
    """ SSH key ID to associate with the VM """
    note: str | Unset = UNSET
    """ Optional note """

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

        return private_cloud_vm_create_request
