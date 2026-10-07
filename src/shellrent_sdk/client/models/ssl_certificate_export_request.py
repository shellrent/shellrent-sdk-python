from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.ssl_certificate_export_request_format import SslCertificateExportRequestFormat
from ..types import UNSET, Unset

T = TypeVar("T", bound="SslCertificateExportRequest")


@_attrs_define
class SslCertificateExportRequest:
    format_: SslCertificateExportRequestFormat
    """ Export format: one of the codes of `GET /api/v3/ssl-certificates/{ssl_certificate_id}/export-formats`, which
    lists the formats available for the certificate """
    current_passphrase: str | Unset = UNSET
    """ Passphrase of the current private key, if it is protected by one """
    passphrase: str | Unset = UNSET
    """ Passphrase that protects the exported file, for the formats that require it (see requires_passphrase in the
    export formats). If omitted, current_passphrase is used """

    def to_dict(self) -> dict[str, Any]:
        format_ = self.format_.value

        current_passphrase = self.current_passphrase

        passphrase = self.passphrase

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "format": format_,
            }
        )
        if current_passphrase is not UNSET:
            field_dict["current_passphrase"] = current_passphrase
        if passphrase is not UNSET:
            field_dict["passphrase"] = passphrase

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        format_ = SslCertificateExportRequestFormat(d.pop("format"))

        current_passphrase = d.pop("current_passphrase", UNSET)

        passphrase = d.pop("passphrase", UNSET)

        ssl_certificate_export_request = cls(
            format_=format_,
            current_passphrase=current_passphrase,
            passphrase=passphrase,
        )

        return ssl_certificate_export_request
