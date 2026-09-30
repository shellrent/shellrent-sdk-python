from enum import IntEnum


class DomainDnssecRequestKeyData256ItemAlgorithm(IntEnum):
    VALUE_8 = 8
    VALUE_13 = 13

    def __str__(self) -> str:
        return str(self.value)
