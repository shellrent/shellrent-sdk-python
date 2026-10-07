from enum import StrEnum


class HostingCronjobCreateRequestRequestProtocol(StrEnum):
    HTTP = "http"
    HTTPS = "https"

    def __str__(self) -> str:
        return str(self.value)
