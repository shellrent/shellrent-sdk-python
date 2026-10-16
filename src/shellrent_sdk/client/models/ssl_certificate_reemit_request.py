from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SslCertificateReemitRequest")


@_attrs_define
class SslCertificateReemitRequest:
    private_key: str | Unset = UNSET
    """ Custom private key in PEM format, without passphrase. Omit it, or send an empty string or the current key,
    to keep the current one """
    csr_key: str | Unset = UNSET
    """ Custom CSR in PEM format, verified with the certificate supplier. Omit it, or send an empty string or the
    current CSR, to keep the current one """

    def to_dict(self) -> dict[str, Any]:
        private_key = self.private_key

        csr_key = self.csr_key

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if private_key is not UNSET:
            field_dict["private_key"] = private_key
        if csr_key is not UNSET:
            field_dict["csr_key"] = csr_key

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        private_key = d.pop("private_key", UNSET)

        csr_key = d.pop("csr_key", UNSET)

        ssl_certificate_reemit_request = cls(
            private_key=private_key,
            csr_key=csr_key,
        )

        return ssl_certificate_reemit_request
