from enum import StrEnum


class CanInstallHostingSslCertificateDestinationType(StrEnum):
    ALL = "all"
    MAIL = "mail"
    WEB = "web"

    def __str__(self) -> str:
        return str(self.value)
