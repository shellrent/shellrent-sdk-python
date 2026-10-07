from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="HostingModSecurityScan")


@_attrs_define
class HostingModSecurityScan:
    """Scan of the ModSecurity rules that generated errors or blocks on the hosting"""

    scan_id: int
    hosting_id: int | None
    """ Id of the hosting (`GET /api/v3/hostings/{hosting_id}`) """
    date_created: datetime.datetime
    error: None | str
    """ Error of the scan; null when it succeeded """
    rules_found: int
    """ Number of rules found by the scan: those that generated errors or blocks on the day of the scan """
    rules_excluded: int
    """ Number of rules found by the scan that are disabled on the hosting now (`included` true in `GET
    /api/v3/hostings/{hosting_id}/modsecurity/rules`) """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        scan_id = self.scan_id

        hosting_id: int | None
        hosting_id = self.hosting_id

        date_created = self.date_created.isoformat()

        error: None | str
        error = self.error

        rules_found = self.rules_found

        rules_excluded = self.rules_excluded

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "scan_id": scan_id,
                "hosting_id": hosting_id,
                "date_created": date_created,
                "error": error,
                "rules_found": rules_found,
                "rules_excluded": rules_excluded,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        scan_id = d.pop("scan_id")

        def _parse_hosting_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        hosting_id = _parse_hosting_id(d.pop("hosting_id"))

        date_created = datetime.datetime.fromisoformat(d.pop("date_created"))

        def _parse_error(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        error = _parse_error(d.pop("error"))

        rules_found = d.pop("rules_found")

        rules_excluded = d.pop("rules_excluded")

        hosting_mod_security_scan = cls(
            scan_id=scan_id,
            hosting_id=hosting_id,
            date_created=date_created,
            error=error,
            rules_found=rules_found,
            rules_excluded=rules_excluded,
        )

        hosting_mod_security_scan.additional_properties = d
        return hosting_mod_security_scan

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
