from enum import StrEnum


class SmsCreateRequestQuality(StrEnum):
    PREMIUM = "PREMIUM"
    STANDARD = "STANDARD"

    def __str__(self) -> str:
        return str(self.value)
