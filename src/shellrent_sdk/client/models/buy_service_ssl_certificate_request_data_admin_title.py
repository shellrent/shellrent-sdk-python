from enum import StrEnum


class BuyServiceSslCertificateRequestDataAdminTitle(StrEnum):
    DR = "Dr"
    MISS = "Miss"
    MR = "Mr"
    MRS = "Mrs"
    MS = "Ms"
    REV = "Rev"

    def __str__(self) -> str:
        return str(self.value)
