from enum import StrEnum


class ListOrdersType(StrEnum):
    P = "P"
    R = "R"

    def __str__(self) -> str:
        return str(self.value)
