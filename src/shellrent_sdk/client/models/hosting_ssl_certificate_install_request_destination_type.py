from enum import StrEnum


class HostingSslCertificateInstallRequestDestinationType(StrEnum):
    ALL = "all"
    MAIL = "mail"
    WEB = "web"

    def __str__(self) -> str:
        return str(self.value)
