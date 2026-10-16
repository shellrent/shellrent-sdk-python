from enum import StrEnum


class DomainDnsRecordRequestType(StrEnum):
    A = "A"
    AAAA = "AAAA"
    CAA = "CAA"
    CNAME = "CNAME"
    MX = "MX"
    SPF = "SPF"
    SRV = "SRV"
    TLSA = "TLSA"
    TXT = "TXT"

    def __str__(self) -> str:
        return str(self.value)
