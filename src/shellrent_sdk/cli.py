"""The ``shellrent`` command, modelled on ``gh api``: calls any endpoint of the Shellrent APIs.

The credentials are read only from the environment: an option with the secret would show it in
``ps`` and in the shell history.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from collections.abc import Sequence
from pathlib import Path
from typing import Final
from urllib.parse import urlsplit

import httpx

from .auth import (
    ClientCredentials,
    FileTokenStore,
    MemoryTokenStore,
    OAuth2Auth,
    TokenError,
    TokenStore,
)
from .http import _package_version, client_args

__all__ = ["main"]

EXIT_OK: Final = 0
EXIT_HTTP_ERROR: Final = 1
EXIT_USAGE: Final = 2

_ENVIRONMENT_HELP: Final = """\
environment variables:
  SHELLRENT_CLIENT_ID      client ID (required)
  SHELLRENT_CLIENT_SECRET  client secret (required)
  SHELLRENT_SCOPES         scopes to request, separated by spaces or commas (default: all)
  SHELLRENT_API_URL        base URL of the API (default: https://api.shellrent.com)
  SHELLRENT_TOKEN_CACHE    directory of the token cache (default: $XDG_CACHE_HOME/shellrent-sdk
                           or ~/.cache/shellrent-sdk), or "off" not to cache the token

exit status:
  0 success, 1 HTTP error or failed request, 2 usage or authentication error
"""


class _UsageError(Exception):
    pass


def main(argv: Sequence[str] | None = None) -> int:
    """Runs the command with the arguments ``argv`` (default ``sys.argv[1:]``).

    Returns the exit status: 0 for a 2xx response, 1 for an HTTP error or a failed request,
    2 for a usage or authentication error.
    """
    parser = _parser()
    try:
        args = parser.parse_args(argv)
    except SystemExit as exc:  # --help, --version and usage errors.
        return exc.code if isinstance(exc.code, int) else EXIT_USAGE

    try:
        status: int = args.command(args)
    except _UsageError as exc:
        return _fail(f"error: {exc}", EXIT_USAGE)
    except TokenError as exc:
        return _fail(str(exc), EXIT_USAGE)
    except httpx.HTTPError as exc:
        return _fail(f"request failed: {exc}", EXIT_HTTP_ERROR)
    return status


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="shellrent",
        description="Call the Shellrent APIs.",
        epilog=_ENVIRONMENT_HELP,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s {_package_version()}")
    commands = parser.add_subparsers(title="commands", metavar="COMMAND", required=True)

    api = commands.add_parser(
        "api",
        help="send a request and print the body of the response",
        description=(
            "Send a request to PATH and print the body of the response on stdout. "
            "Any endpoint works, such as /api/v3/purchases or /api/internal/v3/...: "
            "the credentials decide which ones are allowed."
        ),
        epilog=_ENVIRONMENT_HELP,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    api.add_argument("method", metavar="METHOD", help="HTTP method, such as GET or POST")
    api.add_argument(
        "path", metavar="PATH", help="path of the endpoint, with the query string if any"
    )
    api.add_argument(
        "-d",
        "--data",
        metavar="JSON",
        help="JSON body of the request: the text itself, @FILE to read it from FILE, - to read it from stdin",
    )
    api.set_defaults(command=_api)

    token = commands.add_parser(
        "token",
        help="print a valid access token",
        description="Print a valid access token, from the cache if there is one.",
        epilog=_ENVIRONMENT_HELP,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    token.set_defaults(command=_token)
    return parser


def _api(args: argparse.Namespace) -> int:
    method = str(args.method).upper()
    if not method.isascii() or not method.isalpha():
        raise _UsageError(f"invalid METHOD: {args.method}")
    path = _path(args.path)
    body = _body(args.data) if args.data is not None else None
    credentials = _credentials()

    headers = {"Accept": "application/json, */*"}
    if body is not None:
        headers["Content-Type"] = "application/json"

    client, _ = _client(credentials)
    with client:
        response = client.request(method, path, content=body, headers=headers)

    _write_stdout(response.content)
    if response.is_success:
        return EXIT_OK
    return _fail(
        f"HTTP {response.status_code} {response.reason_phrase}{_api_message(response)}",
        EXIT_HTTP_ERROR,
    )


def _token(args: argparse.Namespace) -> int:
    client, auth = _client(_credentials())
    with client:
        token = auth.get_token(client)
    print(token)
    return EXIT_OK


def _client(credentials: ClientCredentials) -> tuple[httpx.Client, OAuth2Auth]:
    args = client_args(credentials, token_store=_token_store())
    return httpx.Client(**args), args["auth"]


def _credentials() -> ClientCredentials:
    try:
        return ClientCredentials.from_env()
    except ValueError as exc:
        raise _UsageError(str(exc)) from None


def _token_store() -> TokenStore:
    # Each run is a new process: without a file the token would be requested every time.
    setting = os.environ.get("SHELLRENT_TOKEN_CACHE", "")
    if setting.lower() == "off":
        return MemoryTokenStore()
    return FileTokenStore(setting or None)


def _path(path: str) -> str:
    # A URL would send the token to another host.
    parts = urlsplit(path)
    if parts.scheme or parts.netloc:
        raise _UsageError(f"PATH must be a path such as /api/v3/purchases, not a URL: {path}")
    return path if path.startswith("/") else f"/{path}"


def _body(data: str) -> bytes:
    if data == "-":
        content = sys.stdin.buffer.read()
    elif data.startswith("@"):
        try:
            content = Path(data[1:]).read_bytes()
        except OSError as exc:
            raise _UsageError(f"cannot read {data[1:]}: {exc.strerror}") from None
    else:
        content = data.encode()

    try:
        json.loads(content)
    except ValueError as exc:
        raise _UsageError(f"the data is not valid JSON: {exc}") from None
    return content


def _api_message(response: httpx.Response) -> str:
    """The message of the error envelope, if any."""
    try:
        body = response.json()
    except ValueError:
        return ""
    message = body.get("message") if isinstance(body, dict) else None
    return f": {message}" if isinstance(message, str) and message else ""


def _write_stdout(content: bytes) -> None:
    sys.stdout.flush()
    sys.stdout.buffer.write(content)
    if content and not content.endswith(b"\n") and sys.stdout.isatty():
        sys.stdout.buffer.write(b"\n")
    sys.stdout.buffer.flush()


def _fail(message: str, status: int) -> int:
    print(f"shellrent: {message}", file=sys.stderr)
    return status
