"""Calls the real API with the credentials in SHELLRENT_CLIENT_ID and SHELLRENT_CLIENT_SECRET
(and SHELLRENT_API_URL, if set); skipped without them."""

from __future__ import annotations

import os

import httpx
import pytest

from shellrent_sdk import ClientCredentials, create_client, unwrap
from shellrent_sdk.client.api.health import get_health
from shellrent_sdk.http import client_args

pytestmark = pytest.mark.skipif(
    not (os.environ.get("SHELLRENT_CLIENT_ID") and os.environ.get("SHELLRENT_CLIENT_SECRET")),
    reason="SHELLRENT_CLIENT_ID and SHELLRENT_CLIENT_SECRET are not set",
)


def test_gets_a_token() -> None:
    args = client_args(ClientCredentials.from_env())

    with httpx.Client(**args) as client:
        token = args["auth"].get_token(client)

    assert token


def test_get_health() -> None:
    with create_client() as client:
        health = unwrap(get_health.sync_detailed(client=client))

    assert health.error == 0
    assert health.data.status
