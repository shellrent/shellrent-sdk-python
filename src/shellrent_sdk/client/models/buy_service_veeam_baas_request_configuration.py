from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="BuyServiceVeeamBaasRequestConfiguration")


@_attrs_define
class BuyServiceVeeamBaasRequestConfiguration:
    """Veeam BaaS configuration options"""

    cloud_connect_gb: int | Unset = UNSET
    """ Veeam Cloud Connect storage: quantity (in GB) of storage. """
    agent_server: int | Unset = UNSET
    """ Veeam Agent: number of "Server" workloads. """
    agent_workstation: int | Unset = UNSET
    """ Veeam Agent: number of "Workstation" workloads. """
    vbr_entplus_vm: int | Unset = UNSET
    """ Veeam Backup & Replication (VBR) Enterprise Plus: number of "VM in VMware/Hyper-V" workloads. """
    vbr_entplus_server: int | Unset = UNSET
    """ Veeam Backup & Replication (VBR) Enterprise Plus: number of "Server" workloads. """
    vbr_entplus_workstation: int | Unset = UNSET
    """ Veeam Backup & Replication (VBR) Enterprise Plus: number of "Workstation" workloads. """
    vbr_entplus_gb: int | Unset = UNSET
    """ Veeam Backup & Replication (VBR) Enterprise Plus: number of slots for "NAS" workloads. Each slot represents
    250 GB of storage. """
    vbr_standard_vm: int | Unset = UNSET
    """ Veeam Backup & Replication (VBR) Standard: number of "VM in VMware/Hyper-V" workloads. """
    vbr_standard_server: int | Unset = UNSET
    """ Veeam Backup & Replication (VBR) Standard: number of "Server" workloads. """
    vbr_standard_workstation: int | Unset = UNSET
    """ Veeam Backup & Replication (VBR) Standard: number of "Workstation" workloads. """
    vb365_users: int | Unset = UNSET
    """ Veeam Backup for Microsoft 365: number of Users. """
    cc_license_vm: int | Unset = UNSET
    """ Veeam Cloud Connect license: number of "VM in VMware/Hyper-V" workloads. """
    cc_license_server: int | Unset = UNSET
    """ Veeam Cloud Connect license: number of "Server" workloads. """

    def to_dict(self) -> dict[str, Any]:
        cloud_connect_gb = self.cloud_connect_gb

        agent_server = self.agent_server

        agent_workstation = self.agent_workstation

        vbr_entplus_vm = self.vbr_entplus_vm

        vbr_entplus_server = self.vbr_entplus_server

        vbr_entplus_workstation = self.vbr_entplus_workstation

        vbr_entplus_gb = self.vbr_entplus_gb

        vbr_standard_vm = self.vbr_standard_vm

        vbr_standard_server = self.vbr_standard_server

        vbr_standard_workstation = self.vbr_standard_workstation

        vb365_users = self.vb365_users

        cc_license_vm = self.cc_license_vm

        cc_license_server = self.cc_license_server

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if cloud_connect_gb is not UNSET:
            field_dict["cloud_connect_gb"] = cloud_connect_gb
        if agent_server is not UNSET:
            field_dict["agent_server"] = agent_server
        if agent_workstation is not UNSET:
            field_dict["agent_workstation"] = agent_workstation
        if vbr_entplus_vm is not UNSET:
            field_dict["vbr_entplus_vm"] = vbr_entplus_vm
        if vbr_entplus_server is not UNSET:
            field_dict["vbr_entplus_server"] = vbr_entplus_server
        if vbr_entplus_workstation is not UNSET:
            field_dict["vbr_entplus_workstation"] = vbr_entplus_workstation
        if vbr_entplus_gb is not UNSET:
            field_dict["vbr_entplus_gb"] = vbr_entplus_gb
        if vbr_standard_vm is not UNSET:
            field_dict["vbr_standard_vm"] = vbr_standard_vm
        if vbr_standard_server is not UNSET:
            field_dict["vbr_standard_server"] = vbr_standard_server
        if vbr_standard_workstation is not UNSET:
            field_dict["vbr_standard_workstation"] = vbr_standard_workstation
        if vb365_users is not UNSET:
            field_dict["vb365_users"] = vb365_users
        if cc_license_vm is not UNSET:
            field_dict["cc_license_vm"] = cc_license_vm
        if cc_license_server is not UNSET:
            field_dict["cc_license_server"] = cc_license_server

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        cloud_connect_gb = d.pop("cloud_connect_gb", UNSET)

        agent_server = d.pop("agent_server", UNSET)

        agent_workstation = d.pop("agent_workstation", UNSET)

        vbr_entplus_vm = d.pop("vbr_entplus_vm", UNSET)

        vbr_entplus_server = d.pop("vbr_entplus_server", UNSET)

        vbr_entplus_workstation = d.pop("vbr_entplus_workstation", UNSET)

        vbr_entplus_gb = d.pop("vbr_entplus_gb", UNSET)

        vbr_standard_vm = d.pop("vbr_standard_vm", UNSET)

        vbr_standard_server = d.pop("vbr_standard_server", UNSET)

        vbr_standard_workstation = d.pop("vbr_standard_workstation", UNSET)

        vb365_users = d.pop("vb365_users", UNSET)

        cc_license_vm = d.pop("cc_license_vm", UNSET)

        cc_license_server = d.pop("cc_license_server", UNSET)

        buy_service_veeam_baas_request_configuration = cls(
            cloud_connect_gb=cloud_connect_gb,
            agent_server=agent_server,
            agent_workstation=agent_workstation,
            vbr_entplus_vm=vbr_entplus_vm,
            vbr_entplus_server=vbr_entplus_server,
            vbr_entplus_workstation=vbr_entplus_workstation,
            vbr_entplus_gb=vbr_entplus_gb,
            vbr_standard_vm=vbr_standard_vm,
            vbr_standard_server=vbr_standard_server,
            vbr_standard_workstation=vbr_standard_workstation,
            vb365_users=vb365_users,
            cc_license_vm=cc_license_vm,
            cc_license_server=cc_license_server,
        )

        return buy_service_veeam_baas_request_configuration
