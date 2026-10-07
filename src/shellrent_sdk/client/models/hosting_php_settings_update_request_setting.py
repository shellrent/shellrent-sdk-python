from enum import StrEnum


class HostingPhpSettingsUpdateRequestSetting(StrEnum):
    DISPLAY_ERRORS = "display_errors"
    MAX_EXECUTION_TIME = "max_execution_time"
    MAX_INPUT_TIME = "max_input_time"
    MEMORY_LIMIT = "memory_limit"
    OPCACHE_ENABLE = "opcache.enable"
    POST_MAX_SIZE = "post_max_size"
    UPLOAD_MAX_FILESIZE = "upload_max_filesize"

    def __str__(self) -> str:
        return str(self.value)
