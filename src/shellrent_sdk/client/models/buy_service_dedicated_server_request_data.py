from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="BuyServiceDedicatedServerRequestData")


@_attrs_define
class BuyServiceDedicatedServerRequestData:
    """Dedicated Server configuration and template selection"""

    server_configuration_code: str
    """ One of the server Templates compatible with the "Dedicated Server" service to buy """
    server_template_code: str
    """ One of the server Operative Systems (OS) compatible with the "Dedicated Server" service to buy and with the
    chosen server Template """

    def to_dict(self) -> dict[str, Any]:
        server_configuration_code = self.server_configuration_code

        server_template_code = self.server_template_code

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "SERVER_CONFIGURATION_CODE": server_configuration_code,
                "SERVER_TEMPLATE_CODE": server_template_code,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        server_configuration_code = d.pop("SERVER_CONFIGURATION_CODE")

        server_template_code = d.pop("SERVER_TEMPLATE_CODE")

        buy_service_dedicated_server_request_data = cls(
            server_configuration_code=server_configuration_code,
            server_template_code=server_template_code,
        )

        return buy_service_dedicated_server_request_data
