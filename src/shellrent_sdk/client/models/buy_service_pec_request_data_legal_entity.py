from enum import StrEnum


class BuyServicePecRequestDataLegalEntity(StrEnum):
    AZIENDA = "AZIENDA"
    DITTA_INDIVIDUALE = "DITTA_INDIVIDUALE"
    LIBERO_PROFESSIONISTA = "LIBERO_PROFESSIONISTA"
    NO_PROFIT = "NO_PROFIT"
    PRIVATO = "PRIVATO"
    PUBBLICA_AMMINISTRAZIONE = "PUBBLICA_AMMINISTRAZIONE"

    def __str__(self) -> str:
        return str(self.value)
