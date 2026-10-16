from enum import StrEnum


class ServerPowerActionRequestAction(StrEnum):
    HARD_REBOOT = "hard_reboot"
    HARD_STOP = "hard_stop"
    REBOOT = "reboot"
    START = "start"
    STOP = "stop"

    def __str__(self) -> str:
        return str(self.value)
