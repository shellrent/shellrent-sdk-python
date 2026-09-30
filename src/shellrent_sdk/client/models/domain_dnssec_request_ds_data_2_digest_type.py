from enum import IntEnum


class DomainDnssecRequestDsData2DigestType(IntEnum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_4 = 4

    def __str__(self) -> str:
        return str(self.value)
