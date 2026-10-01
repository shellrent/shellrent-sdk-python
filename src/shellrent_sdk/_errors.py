from __future__ import annotations

from collections.abc import Callable, Mapping
from typing import TYPE_CHECKING, Protocol, TypeVar, overload

from .client.errors import UnexpectedStatus
from .client.types import Response

if TYPE_CHECKING:
    from .client.models.api_error import ApiError

T = TypeVar("T")
T_co = TypeVar("T_co", covariant=True)


class ApiErrorLike(Protocol):
    """The error envelope of the API: the ``ApiError`` model of any generated client."""

    @property
    def error(self) -> int: ...

    @property
    def message(self) -> str | None: ...


E = TypeVar("E", bound=ApiErrorLike)


class _ResponseLike(Protocol[T_co]):
    """The ``Response`` of any generated client."""

    @property
    def status_code(self) -> int: ...

    @property
    def content(self) -> bytes: ...

    @property
    def headers(self) -> Mapping[str, str]: ...

    @property
    def parsed(self) -> T_co | None: ...


class ApiException(Exception):
    """The API answered with an error response documented in the specification.

    Attributes:
        status_code: HTTP status, such as 404.
        error: The error envelope, with ``message``: the ``ApiError`` of the generated client.
        headers: Headers of the response, such as ``Retry-After``.
        content: Body of the response.
    """

    def __init__(
        self, status_code: int, error: ApiErrorLike, headers: Mapping[str, str], content: bytes
    ) -> None:
        if error.message is None:
            super().__init__(f"HTTP {status_code}")
        else:
            super().__init__(f"HTTP {status_code}: {error.message}")
        self.status_code = status_code
        self.error = error
        self.headers = headers
        self.content = content


@overload
def unwrap(
    response: Response[T | ApiError],
    *,
    error_type: type[ApiError] | None = None,
    unexpected_status_type: Callable[[int, bytes], Exception] | None = None,
) -> T: ...


@overload
def unwrap(
    response: _ResponseLike[T | E],
    *,
    error_type: type[E],
    unexpected_status_type: Callable[[int, bytes], Exception] | None = None,
) -> T: ...


def unwrap(
    response: _ResponseLike[object],
    *,
    error_type: type[ApiErrorLike] | None = None,
    unexpected_status_type: Callable[[int, bytes], Exception] | None = None,
) -> object:
    """Returns the parsed body of a successful response and raises an exception for the others.

    Takes the result of the ``sync_detailed()`` and ``asyncio_detailed()`` functions::

        purchase = unwrap(get_purchase.sync_detailed(123, client=client))

    Args:
        response: The response of a generated function.
        error_type: The ``ApiError`` model of the generated client; default the one of
            ``shellrent_sdk.client``. In a direct call mypy cannot tell the error envelope from the
            envelope of the body, so another generated client wraps ``unwrap()`` with its own types::

                def unwrap(response: Response[T | ApiError]) -> T:
                    return shellrent_sdk.unwrap(
                        response, error_type=ApiError, unexpected_status_type=UnexpectedStatus
                    )

        unexpected_status_type: The ``UnexpectedStatus`` class of the generated client; default the
            one of ``shellrent_sdk.client``. Each generated client has its own: another client passes
            it, so that ``unwrap()`` raises the same exception as its generated functions.

    Raises:
        ApiException: An error response documented in the specification (``error_type``).
        UnexpectedStatus: Any other response outside 2xx, or without a parsed body
            (``unexpected_status_type``).
    """
    if error_type is None:
        # Imported here: importing the models takes a while, and the CLI does not need them.
        from .client.models.api_error import ApiError

        error_type = ApiError

    parsed = response.parsed
    if isinstance(parsed, error_type):
        raise ApiException(response.status_code, parsed, response.headers, response.content)
    if parsed is None or not 200 <= response.status_code < 300:
        if unexpected_status_type is None:
            unexpected_status_type = UnexpectedStatus
        raise unexpected_status_type(response.status_code, response.content)
    return parsed
