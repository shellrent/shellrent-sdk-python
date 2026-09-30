from enum import IntEnum


class BuyServiceCloudVpsRequestDataDISKQUANTITY(IntEnum):
    VALUE_20 = 20
    VALUE_25 = 25
    VALUE_30 = 30
    VALUE_35 = 35
    VALUE_40 = 40
    VALUE_45 = 45
    VALUE_50 = 50
    VALUE_55 = 55
    VALUE_60 = 60
    VALUE_65 = 65
    VALUE_70 = 70
    VALUE_75 = 75
    VALUE_80 = 80
    VALUE_85 = 85
    VALUE_90 = 90
    VALUE_95 = 95
    VALUE_100 = 100

    def __str__(self) -> str:
        return str(self.value)
