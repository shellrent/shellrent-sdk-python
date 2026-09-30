from enum import StrEnum


class BuyServiceCpanelLicenseRequestDataInstallationType(StrEnum):
    EXTERNAL_INSTALLATION_TYPE = "external_installation_type"
    INTERNAL_INSTALLATION_TYPE = "internal_installation_type"

    def __str__(self) -> str:
        return str(self.value)
