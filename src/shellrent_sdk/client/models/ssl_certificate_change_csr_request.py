from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="SslCertificateChangeCsrRequest")


@_attrs_define
class SslCertificateChangeCsrRequest:
    csr: str
    """ Custom CSR in PEM format, verified with the certificate supplier; sending the current CSR changes nothing
    """

    def to_dict(self) -> dict[str, Any]:
        csr = self.csr

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "csr": csr,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        csr = d.pop("csr")

        ssl_certificate_change_csr_request = cls(
            csr=csr,
        )

        return ssl_certificate_change_csr_request
