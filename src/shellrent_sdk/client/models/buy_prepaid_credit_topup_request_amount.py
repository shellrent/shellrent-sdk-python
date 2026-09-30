from enum import IntEnum


class BuyPrepaidCreditTopupRequestAmount(IntEnum):
    VALUE_50 = 50
    VALUE_100 = 100
    VALUE_150 = 150
    VALUE_200 = 200
    VALUE_300 = 300
    VALUE_500 = 500
    VALUE_800 = 800
    VALUE_1000 = 1000
    VALUE_1500 = 1500
    VALUE_2000 = 2000

    def __str__(self) -> str:
        return str(self.value)
