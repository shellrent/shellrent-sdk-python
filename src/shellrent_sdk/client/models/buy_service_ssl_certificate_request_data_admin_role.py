from enum import StrEnum


class BuyServiceSslCertificateRequestDataAdminRole(StrEnum):
    BUSINESS_OWNER = "Business Owner"
    COMPANY_DIRECTOR = "Company Director"
    PRESIDENT = "President"
    WEBSITE_OWNER = "Website Owner"

    def __str__(self) -> str:
        return str(self.value)
