"""unwrap() with the models of another generated client, such as the one of shellrent-internal-sdk."""

from __future__ import annotations

from collections.abc import MutableMapping
from http import HTTPStatus
from io import BytesIO
from typing import Generic, TypeVar, assert_type

import pytest
from attrs import define

from shellrent_sdk import ApiException, unwrap
from shellrent_sdk.client.models import ApiError
from shellrent_sdk.client.types import File, Response

T = TypeVar("T")


# The types of another generated client, with the same shape as those of shellrent_sdk.client.
@define
class OtherResponse(Generic[T]):
    status_code: HTTPStatus
    content: bytes
    headers: MutableMapping[str, str]
    parsed: T | None


@define
class OtherApiError:
    error: int
    message: str | None


@define
class OtherStatus:
    error: int
    message: str | None
    data: str


def other_unwrap(response: OtherResponse[T | OtherApiError]) -> T:
    """The wrapper of the other client, as in the docstring of unwrap()."""
    return unwrap(response, error_type=OtherApiError)


def test_unwrap_raises_api_exception_for_the_api_error_of_another_client() -> None:
    error = OtherApiError(error=404, message="Not found")
    response: OtherResponse[OtherStatus | OtherApiError] = OtherResponse(
        HTTPStatus.NOT_FOUND, b"{}", {"X-Request-Id": "abc"}, error
    )

    with pytest.raises(ApiException) as info:
        other_unwrap(response)

    assert info.value.status_code == 404
    assert info.value.error is error
    assert info.value.headers["X-Request-Id"] == "abc"
    assert str(info.value) == "HTTP 404: Not found"


def test_unwrap_returns_the_body_of_another_client() -> None:
    status = OtherStatus(error=0, message=None, data="ok")
    response: OtherResponse[OtherStatus | OtherApiError] = OtherResponse(
        HTTPStatus.OK, b"{}", {}, status
    )

    assert assert_type(other_unwrap(response), OtherStatus) is status


def test_api_exception_without_message() -> None:
    response: OtherResponse[OtherStatus | OtherApiError] = OtherResponse(
        HTTPStatus.CONFLICT, b"{}", {}, OtherApiError(error=409, message=None)
    )

    with pytest.raises(ApiException) as info:
        other_unwrap(response)

    assert str(info.value) == "HTTP 409"


def test_the_api_error_of_shellrent_sdk_is_the_default() -> None:
    file = File(payload=BytesIO(b"%PDF"))
    response: Response[File | ApiError] = Response(HTTPStatus.OK, b"%PDF", {}, file)
    error: Response[File | ApiError] = Response(
        HTTPStatus.NOT_FOUND,
        b"{}",
        {},
        ApiError(error=404, message="Not found", data=None, meta=None),
    )

    assert assert_type(unwrap(response), File) is file
    assert assert_type(unwrap(response, error_type=ApiError), File) is file
    with pytest.raises(ApiException):
        unwrap(error, error_type=ApiError)
