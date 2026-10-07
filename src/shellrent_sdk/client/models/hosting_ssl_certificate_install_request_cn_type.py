from enum import StrEnum


class HostingSslCertificateInstallRequestCnType(StrEnum):
    NORMAL = "NORMAL"
    WILDCARD = "WILDCARD"

    def __str__(self) -> str:
        return str(self.value)
