from enum import StrEnum


class HostingCronjobCreateRequestHttpRequestMethod(StrEnum):
    GET = "GET"
    POST = "POST"

    def __str__(self) -> str:
        return str(self.value)
