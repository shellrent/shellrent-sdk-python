from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.hosting_php_setting import HostingPhpSetting


T = TypeVar("T", bound="Hosting")


@_attrs_define
class Hosting:
    """Hosting of the account: a main hosting, bought with a purchase, or one of its subdomains"""

    hosting_id: int
    purchase_id: int | None
    """ Id of the purchase of the hosting (`GET /api/v3/purchases/{purchase_id}`); null for a subdomain, which
    belongs to the purchase of its main hosting """
    parent_hosting_id: int | None
    """ Id of the main hosting of a subdomain (`GET /api/v3/hostings/{hosting_id}`); null for a main hosting """
    is_primary: bool
    """ Whether it is a main hosting; false for a subdomain (`POST /api/v3/hostings/{hosting_id}/subdomains`) """
    host_name: None | str
    """ Host name, in Unicode: the hostname of a main hosting (usually its domain), the level name of a subdomain
    (for example `blog`) """
    host_name_idna: None | str
    """ `host_name` in punycode """
    full_name: None | str
    """ Full hostname, in Unicode: for a subdomain, the level name followed by the hostname of the main hosting """
    full_name_idna: None | str
    """ `full_name` in punycode """
    domain_full_name: None | str
    """ Hostname on the domain of the purchase, in Unicode: the domain for a main hosting, the subdomain of the
    domain for a subdomain """
    domain_full_name_idna: None | str
    """ `domain_full_name` in punycode """
    php_version: None | str
    """ PHP version of the hosting, for example `8.3` (`PATCH /api/v3/hostings/{hosting_id}/php-version`); null or
    empty when not set """
    http_version: str
    """ HTTP version of the hosting: 1 for HTTP/1.1, 2 for HTTP/2 (`PATCH /api/v3/hostings/{hosting_id}/http-
    version`) """
    file_protection_enabled: bool
    """ Whether the file protection is enabled (`PATCH /api/v3/hostings/{hosting_id}/file-protection`) """
    php_settings: list[HostingPhpSetting]
    """ PHP directives changed on the hosting (`PATCH /api/v3/hostings/{hosting_id}/php-settings`): the others have
    the default value of the web server """
    is_active: bool
    """ Whether the hosting is active: always true, since deleted subdomains are not returned """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hosting_id = self.hosting_id

        purchase_id: int | None
        purchase_id = self.purchase_id

        parent_hosting_id: int | None
        parent_hosting_id = self.parent_hosting_id

        is_primary = self.is_primary

        host_name: None | str
        host_name = self.host_name

        host_name_idna: None | str
        host_name_idna = self.host_name_idna

        full_name: None | str
        full_name = self.full_name

        full_name_idna: None | str
        full_name_idna = self.full_name_idna

        domain_full_name: None | str
        domain_full_name = self.domain_full_name

        domain_full_name_idna: None | str
        domain_full_name_idna = self.domain_full_name_idna

        php_version: None | str
        php_version = self.php_version

        http_version = self.http_version

        file_protection_enabled = self.file_protection_enabled

        php_settings = []
        for php_settings_item_data in self.php_settings:
            php_settings_item = php_settings_item_data.to_dict()
            php_settings.append(php_settings_item)

        is_active = self.is_active

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hosting_id": hosting_id,
                "purchase_id": purchase_id,
                "parent_hosting_id": parent_hosting_id,
                "is_primary": is_primary,
                "host_name": host_name,
                "host_name_idna": host_name_idna,
                "full_name": full_name,
                "full_name_idna": full_name_idna,
                "domain_full_name": domain_full_name,
                "domain_full_name_idna": domain_full_name_idna,
                "php_version": php_version,
                "http_version": http_version,
                "file_protection_enabled": file_protection_enabled,
                "php_settings": php_settings,
                "is_active": is_active,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.hosting_php_setting import HostingPhpSetting

        d = dict(src_dict)
        hosting_id = d.pop("hosting_id")

        def _parse_purchase_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        purchase_id = _parse_purchase_id(d.pop("purchase_id"))

        def _parse_parent_hosting_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        parent_hosting_id = _parse_parent_hosting_id(d.pop("parent_hosting_id"))

        is_primary = d.pop("is_primary")

        def _parse_host_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        host_name = _parse_host_name(d.pop("host_name"))

        def _parse_host_name_idna(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        host_name_idna = _parse_host_name_idna(d.pop("host_name_idna"))

        def _parse_full_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        full_name = _parse_full_name(d.pop("full_name"))

        def _parse_full_name_idna(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        full_name_idna = _parse_full_name_idna(d.pop("full_name_idna"))

        def _parse_domain_full_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        domain_full_name = _parse_domain_full_name(d.pop("domain_full_name"))

        def _parse_domain_full_name_idna(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        domain_full_name_idna = _parse_domain_full_name_idna(d.pop("domain_full_name_idna"))

        def _parse_php_version(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        php_version = _parse_php_version(d.pop("php_version"))

        http_version = d.pop("http_version")

        file_protection_enabled = d.pop("file_protection_enabled")

        php_settings = []
        _php_settings = d.pop("php_settings")
        for php_settings_item_data in _php_settings:
            php_settings_item = HostingPhpSetting.from_dict(php_settings_item_data)

            php_settings.append(php_settings_item)

        is_active = d.pop("is_active")

        hosting = cls(
            hosting_id=hosting_id,
            purchase_id=purchase_id,
            parent_hosting_id=parent_hosting_id,
            is_primary=is_primary,
            host_name=host_name,
            host_name_idna=host_name_idna,
            full_name=full_name,
            full_name_idna=full_name_idna,
            domain_full_name=domain_full_name,
            domain_full_name_idna=domain_full_name_idna,
            php_version=php_version,
            http_version=http_version,
            file_protection_enabled=file_protection_enabled,
            php_settings=php_settings,
            is_active=is_active,
        )

        hosting.additional_properties = d
        return hosting

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
