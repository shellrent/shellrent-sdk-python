from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.hosting_php_settings_update_request_setting import (
    HostingPhpSettingsUpdateRequestSetting,
)

T = TypeVar("T", bound="HostingPhpSettingsUpdateRequest")


@_attrs_define
class HostingPhpSettingsUpdateRequest:
    setting: HostingPhpSettingsUpdateRequestSetting
    """ PHP directive to change """
    value: str
    """ New value of the directive. Suggested values: opcache.enable 1 or 0; display_errors On or Off; memory_limit
    from 64M to 512M (64M, 96M, 128M, 160M, 192M, 224M, 256M, 288M, 320M, 384M, 448M, 512M); post_max_size and
    upload_max_filesize from 1M to 512M (1M, 2M, 4M, 8M, 16M, 24M, 32M, 40M, 48M, 64M, 80M, 96M, 112M, 128M, 160M,
    192M, 224M, 256M, 512M); max_execution_time and max_input_time in seconds, from 10 to 600. Other values are
    accepted if they are numbers, optionally followed by M, between the smallest and the largest suggested value """

    def to_dict(self) -> dict[str, Any]:
        setting = self.setting.value

        value = self.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "setting": setting,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        setting = HostingPhpSettingsUpdateRequestSetting(d.pop("setting"))

        value = d.pop("value")

        hosting_php_settings_update_request = cls(
            setting=setting,
            value=value,
        )

        return hosting_php_settings_update_request
