from enum import StrEnum


class ListSmsSmsStatus(StrEnum):
    ACCOMPLISHED = "ACCOMPLISHED"
    CANCELLED = "CANCELLED"
    DRAFT = "DRAFT"
    PROCESSING = "PROCESSING"

    def __str__(self) -> str:
        return str(self.value)
