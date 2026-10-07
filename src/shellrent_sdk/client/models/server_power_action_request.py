from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.server_power_action_request_action import ServerPowerActionRequestAction

T = TypeVar("T", bound="ServerPowerActionRequest")


@_attrs_define
class ServerPowerActionRequest:
    action: ServerPowerActionRequestAction
    """ Power action: physical servers only have `reboot`. Whether it is possible can be checked first with the
    matching check of the server, for example `GET /api/v3/servers/{server_id}/can-hard-reboot` """

    def to_dict(self) -> dict[str, Any]:
        action = self.action.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "action": action,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        action = ServerPowerActionRequestAction(d.pop("action"))

        server_power_action_request = cls(
            action=action,
        )

        return server_power_action_request
