from enum import StrEnum


class HostingSslCertificateCanInstallReason(StrEnum):
    ALREADY_INSTALLED = "ALREADY_INSTALLED"
    CNAME_MISSING = "CNAME_MISSING"
    HOSTING_NOT_ACTIVE = "HOSTING_NOT_ACTIVE"
    LIMIT_REACHED = "LIMIT_REACHED"
    MAIL_NOT_SUPPORTED = "MAIL_NOT_SUPPORTED"
    OPERATION_RUNNING = "OPERATION_RUNNING"

    def __str__(self) -> str:
        return str(self.value)
