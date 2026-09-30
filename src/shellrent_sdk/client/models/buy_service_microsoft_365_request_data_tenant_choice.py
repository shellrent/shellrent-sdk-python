from enum import StrEnum


class BuyServiceMicrosoft365RequestDataTenantChoice(StrEnum):
    NEW = "new"
    SELECT = "select"
    TRANSFER = "transfer"

    def __str__(self) -> str:
        return str(self.value)
