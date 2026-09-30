from enum import StrEnum


class RequestAccessTokenBodyGrantType(StrEnum):
    CLIENT_CREDENTIALS = "client_credentials"

    def __str__(self) -> str:
        return str(self.value)
