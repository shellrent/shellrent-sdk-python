from enum import StrEnum


class OAuthAudience(StrEnum):
    API_INTERNAL = "api-internal"
    API_PUBLIC = "api-public"

    def __str__(self) -> str:
        return str(self.value)
