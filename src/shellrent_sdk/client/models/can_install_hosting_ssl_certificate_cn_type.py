from enum import StrEnum


class CanInstallHostingSslCertificateCnType(StrEnum):
    NORMAL = "NORMAL"
    WILDCARD = "WILDCARD"

    def __str__(self) -> str:
        return str(self.value)
