"""Error responses of the real API; skipped without SHELLRENT_CLIENT_ID and SHELLRENT_CLIENT_SECRET.

The credentials need the purchases:read scope.
"""

from __future__ import annotations

import os

import pytest

from shellrent_sdk import ApiException, create_client, unwrap
from shellrent_sdk.client.api.purchases import get_purchase

pytestmark = pytest.mark.skipif(
    not (os.environ.get("SHELLRENT_CLIENT_ID") and os.environ.get("SHELLRENT_CLIENT_SECRET")),
    reason="SHELLRENT_CLIENT_ID and SHELLRENT_CLIENT_SECRET are not set",
)

#: No purchase has this ID.
MISSING_PURCHASE_ID = 2_147_483_647


def test_a_missing_purchase_raises_api_exception_404() -> None:
    with create_client() as client, pytest.raises(ApiException) as info:
        unwrap(get_purchase.sync_detailed(MISSING_PURCHASE_ID, client=client))

    assert info.value.status_code == 404
    assert info.value.error.error > 0
    assert info.value.error.message
