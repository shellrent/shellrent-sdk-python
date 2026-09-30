from __future__ import annotations

import io
import json
from pathlib import Path
from typing import Any

import httpx
import pytest

import shellrent_sdk.http
from shellrent_sdk import cli
from shellrent_sdk.http import RetryTransport
from tests.support import (
    API_URL,
    CLIENT_ID,
    CLIENT_SECRET,
    TOKEN_URL,
    FakeApi,
    Sleeps,
    body,
    error_response,
    health_response,
    token_response,
)


@pytest.fixture
def api(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> FakeApi:
    """The fake API behind the CLI, with the credentials in the environment."""
    monkeypatch.setenv("SHELLRENT_CLIENT_ID", CLIENT_ID)
    monkeypatch.setenv("SHELLRENT_CLIENT_SECRET", CLIENT_SECRET)
    monkeypatch.setenv("SHELLRENT_API_URL", API_URL)
    monkeypatch.setenv("SHELLRENT_TOKEN_CACHE", str(tmp_path / "cache"))
    monkeypatch.delenv("SHELLRENT_SCOPES", raising=False)

    fake = FakeApi()
    real_client_args = shellrent_sdk.http.client_args

    def client_args(*args: Any, **kwargs: Any) -> dict[str, Any]:
        result = real_client_args(*args, **kwargs)
        result["transport"] = RetryTransport(fake.transport(), sleep=Sleeps().sleep)
        return result

    monkeypatch.setattr(cli, "client_args", client_args)
    return fake


def run(capsys: pytest.CaptureFixture[str], *argv: str) -> tuple[int, str, str]:
    status = cli.main(list(argv))
    out, err = capsys.readouterr()
    assert CLIENT_SECRET not in out
    assert CLIENT_SECRET not in err
    return status, out, err


# shellrent api


def test_prints_the_body_and_exits_0(api: FakeApi, capsys: pytest.CaptureFixture[str]) -> None:
    api.responses += [token_response(), health_response()]

    status, out, err = run(capsys, "api", "get", "/api/health")

    assert status == 0
    assert json.loads(out)["data"] == {"status": "ok"}
    assert err == ""
    assert api.requests[1].method == "GET"
    assert str(api.requests[1].url) == f"{API_URL}/api/health"


def test_calls_any_path_with_its_query_string(
    api: FakeApi, capsys: pytest.CaptureFixture[str]
) -> None:
    api.responses += [token_response(), health_response()]

    status, _, _ = run(capsys, "api", "GET", "api/internal/v3/customers?page=2")

    assert status == 0
    assert str(api.requests[1].url) == f"{API_URL}/api/internal/v3/customers?page=2"


def test_http_errors_exit_1_with_the_body_on_stdout(
    api: FakeApi, capsys: pytest.CaptureFixture[str]
) -> None:
    api.responses += [token_response(), error_response(404, "Purchase not found")]

    status, out, err = run(capsys, "api", "GET", "/api/v3/purchases/1")

    assert status == 1
    assert json.loads(out)["message"] == "Purchase not found"
    assert err == "shellrent: HTTP 404 Not Found: Purchase not found\n"


def test_sends_data_given_as_text(api: FakeApi, capsys: pytest.CaptureFixture[str]) -> None:
    api.responses += [token_response(), health_response()]

    status, _, _ = run(capsys, "api", "POST", "/api/v3/orders/pay", "--data", '{"order_ids": [1]}')

    assert status == 0
    request = api.requests[1]
    assert request.method == "POST"
    assert request.headers["Content-Type"] == "application/json"
    assert body(request) == {"order_ids": [1]}


def test_sends_data_from_a_file(
    api: FakeApi, capsys: pytest.CaptureFixture[str], tmp_path: Path
) -> None:
    api.responses += [token_response(), health_response()]
    data = tmp_path / "body.json"
    data.write_text('{"order_ids": [2]}')

    status, _, _ = run(capsys, "api", "POST", "/api/v3/orders/pay", "--data", f"@{data}")

    assert status == 0
    assert body(api.requests[1]) == {"order_ids": [2]}


def test_sends_data_from_stdin(
    api: FakeApi, capsys: pytest.CaptureFixture[str], monkeypatch: pytest.MonkeyPatch
) -> None:
    api.responses += [token_response(), health_response()]
    monkeypatch.setattr("sys.stdin", io.TextIOWrapper(io.BytesIO(b'{"order_ids": [3]}')))

    status, _, _ = run(capsys, "api", "POST", "/api/v3/orders/pay", "-d", "-")

    assert status == 0
    assert body(api.requests[1]) == {"order_ids": [3]}


@pytest.mark.parametrize(
    ("argv", "message"),
    [
        (["api", "GET", "/x", "--data", "{not json"], "not valid JSON"),
        (
            ["api", "GET", "/x", "--data", "@/does/not/exist.json"],
            "cannot read /does/not/exist.json",
        ),
        (["api", "GET", "https://example.com/api/v3/purchases"], "not a URL"),
        (["api", "GET", "//example.com/api/v3/purchases"], "not a URL"),
        (["api", "G E T", "/x"], "invalid METHOD"),
    ],
)
def test_usage_errors_exit_2(
    api: FakeApi, capsys: pytest.CaptureFixture[str], argv: list[str], message: str
) -> None:
    status, out, err = run(capsys, *argv)

    assert status == 2
    assert out == ""
    assert message in err
    assert api.requests == []


def test_argument_errors_exit_2(capsys: pytest.CaptureFixture[str]) -> None:
    assert run(capsys, "api", "GET")[0] == 2
    assert run(capsys)[0] == 2


def test_missing_credentials_exit_2(
    api: FakeApi, capsys: pytest.CaptureFixture[str], monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.delenv("SHELLRENT_CLIENT_SECRET")

    status, out, err = run(capsys, "api", "GET", "/api/health")

    assert status == 2
    assert out == ""
    assert "SHELLRENT_CLIENT_SECRET" in err


def test_token_errors_exit_2(api: FakeApi, capsys: pytest.CaptureFixture[str]) -> None:
    api.responses += [
        httpx.Response(
            401,
            json={"error": "invalid_client", "error_description": "Client authentication failed"},
        )
    ]

    status, out, err = run(capsys, "api", "GET", "/api/health")

    assert status == 2
    assert out == ""
    assert err == (
        f"shellrent: The token endpoint {TOKEN_URL} answered HTTP 401: "
        "invalid_client (Client authentication failed)\n"
    )


def test_network_errors_exit_1(
    capsys: pytest.CaptureFixture[str], monkeypatch: pytest.MonkeyPatch, api: FakeApi
) -> None:
    def fail(request: httpx.Request) -> httpx.Response:
        raise httpx.ConnectError("Name or service not known", request=request)

    real_client_args = shellrent_sdk.http.client_args
    monkeypatch.setattr(
        cli,
        "client_args",
        lambda *a, **k: {**real_client_args(*a, **k), "transport": httpx.MockTransport(fail)},
    )

    status, _, err = run(capsys, "api", "GET", "/api/health")

    assert status == 1
    assert err == "shellrent: request failed: Name or service not known\n"


# shellrent token


def test_token_prints_a_token_from_the_cache(
    api: FakeApi, capsys: pytest.CaptureFixture[str], tmp_path: Path
) -> None:
    api.responses += [token_response("token-1")]

    assert run(capsys, "token") == (0, "token-1\n", "")
    assert run(capsys, "token") == (0, "token-1\n", "")
    assert len(api.requests) == 1
    [file] = (tmp_path / "cache").iterdir()
    assert CLIENT_SECRET not in file.read_text()


def test_the_cache_can_be_turned_off(
    api: FakeApi,
    capsys: pytest.CaptureFixture[str],
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    monkeypatch.setenv("SHELLRENT_TOKEN_CACHE", "off")
    api.responses += [token_response("token-1"), token_response("token-2")]

    assert run(capsys, "token")[1] == "token-1\n"
    assert run(capsys, "token")[1] == "token-2\n"
    assert not (tmp_path / "cache").exists()


def test_the_api_command_uses_the_cached_token(
    api: FakeApi, capsys: pytest.CaptureFixture[str]
) -> None:
    api.responses += [token_response("token-1"), health_response(), health_response()]

    run(capsys, "api", "GET", "/api/health")
    run(capsys, "api", "GET", "/api/health")

    assert len(api.token_requests) == 1


def test_version(capsys: pytest.CaptureFixture[str]) -> None:
    status, out, _ = run(capsys, "--version")

    assert status == 0
    assert out.startswith("shellrent ")
