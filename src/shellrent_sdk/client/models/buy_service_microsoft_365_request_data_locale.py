from enum import StrEnum


class BuyServiceMicrosoft365RequestDataLocale(StrEnum):
    EN_GB = "en_GB"
    EN_US = "en_US"
    IT_IT = "it_IT"

    def __str__(self) -> str:
        return str(self.value)
