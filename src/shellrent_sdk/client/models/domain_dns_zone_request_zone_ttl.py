from enum import IntEnum


class DomainDnsZoneRequestZoneTtl(IntEnum):
    VALUE_3600 = 3600
    VALUE_14400 = 14400
    VALUE_28800 = 28800
    VALUE_57600 = 57600
    VALUE_86400 = 86400

    def __str__(self) -> str:
        return str(self.value)
