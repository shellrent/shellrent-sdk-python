from enum import StrEnum


class SslCertificateExportRequestFormat(StrEnum):
    CA = "CA"
    CA_PEM = "CA_PEM"
    CERT = "CERT"
    CERT_CA = "CERT_CA"
    CERT_CA_PEM = "CERT_CA_PEM"
    CERT_PEM = "CERT_PEM"
    HASH_SHA256 = "HASH_SHA256"
    HASH_SHA512 = "HASH_SHA512"
    MULTI_ZIP = "MULTI_ZIP"
    PK = "PK"
    PK_CERT_CA = "PK_CERT_CA"

    def __str__(self) -> str:
        return str(self.value)
