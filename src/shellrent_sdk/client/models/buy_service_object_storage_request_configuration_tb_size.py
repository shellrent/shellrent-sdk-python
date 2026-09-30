from enum import IntEnum


class BuyServiceObjectStorageRequestConfigurationTbSize(IntEnum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_10 = 10
    VALUE_15 = 15
    VALUE_20 = 20
    VALUE_25 = 25
    VALUE_30 = 30
    VALUE_35 = 35
    VALUE_40 = 40
    VALUE_45 = 45
    VALUE_50 = 50

    def __str__(self) -> str:
        return str(self.value)
