from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, TypeVar

from .client.errors import UnexpectedStatus
from .client.types import Response

if TYPE_CHECKING:
    from .client.models.api_error import ApiError

T = TypeVar("T")


class ApiException(Exception):
    """The API answered with an error response documented in the specification.

    Attributes:
        status_code: HTTP status, such as 404.
        error: The error envelope, with ``message``.
        headers: Headers of the response, such as ``Retry-After``.
        content: Body of the response.
    """

    def __init__(
        self, status_code: int, error: ApiError, headers: Mapping[str, str], content: bytes
    ) -> None:
        super().__init__(f"HTTP {status_code}: {error.message}")
        self.status_code = status_code
        self.error = error
        self.headers = headers
        self.content = content


def unwrap(response: Response[T | ApiError]) -> T:
    """Returns the parsed body of a successful response and raises an exception for the others.

    Takes the result of the ``sync_detailed()`` and ``asyncio_detailed()`` functions::

        purchase = unwrap(get_purchase.sync_detailed(123, client=client))

    Raises:
        ApiException: An error response documented in the specification (``ApiError``).
        UnexpectedStatus: Any other response outside 2xx, or without a parsed body.
    """
    # Imported here: importing the models takes a while, and the CLI does not need them.
    from .client.models.api_error import ApiError

    parsed = response.parsed
    if isinstance(parsed, ApiError):
        raise ApiException(response.status_code, parsed, response.headers, response.content)
    if parsed is None or not 200 <= response.status_code < 300:
        raise UnexpectedStatus(response.status_code, response.content)
    return parsed
