from __future__ import annotations

import asyncio
import json
from typing import Any

import httpx
import pytest

import shellrent_sdk._factory
import shellrent_sdk.http
from shellrent_sdk import ApiException, UnexpectedStatus, create_client, unwrap
from shellrent_sdk.client import AuthenticatedClient
from shellrent_sdk.client.api.billing import download_invoice_pdf
from shellrent_sdk.client.api.health import get_health
from shellrent_sdk.client.api.hosting import get_hosting_antivirus
from shellrent_sdk.client.api.purchases import get_purchase, list_tasks
from shellrent_sdk.client.api.shop import pay_orders
from shellrent_sdk.client.models import (
    ApiError,
    HealthStatusResponse,
    OrderPayRequest,
    Payment,
)
from shellrent_sdk.http import RetryTransport, default_user_agent
from tests.support import (
    API_URL,
    CLIENT_ID,
    TOKEN_URL,
    FakeApi,
    Sleeps,
    credentials,
    error_response,
    health_response,
    token_response,
)


@pytest.fixture
def api(monkeypatch: pytest.MonkeyPatch) -> FakeApi:
    """The fake API, behind the transport of the clients made by create_client()."""
    fake = FakeApi()
    real_client_args = shellrent_sdk.http.client_args

    def client_args(*args: Any, **kwargs: Any) -> dict[str, Any]:
        result = real_client_args(*args, **kwargs)
        if "transport" in result:
            result["transport"] = RetryTransport(
                fake.transport(), fake.transport(), sleep=Sleeps().sleep
            )
        else:
            result["transport"] = fake.transport()
        return result

    monkeypatch.setattr(shellrent_sdk._factory, "client_args", client_args)
    return fake


def test_creates_the_generated_client() -> None:
    client = create_client(credentials())

    assert isinstance(client, AuthenticatedClient)
    assert client.raise_on_unexpected_status is True
    assert client.get_httpx_client().base_url == httpx.URL(API_URL)
    assert client.get_httpx_client().timeout == httpx.Timeout(30.0)


def test_reads_the_credentials_from_the_environment(
    monkeypatch: pytest.MonkeyPatch, api: FakeApi
) -> None:
    monkeypatch.setenv("SHELLRENT_CLIENT_ID", "env-id")
    monkeypatch.setenv("SHELLRENT_CLIENT_SECRET", "env-secret")
    monkeypatch.setenv("SHELLRENT_API_URL", "https://api.staging.test")
    api.responses += [token_response(), health_response()]

    get_health.sync(client=create_client())

    assert [str(r.url) for r in api.requests] == [
        "https://api.staging.test/oauth/token",
        "https://api.staging.test/api/health",
    ]


def test_calls_the_api_with_token_and_user_agent(api: FakeApi) -> None:
    api.responses += [token_response("token-1"), health_response()]

    health = get_health.sync(client=create_client(credentials()))

    assert isinstance(health, HealthStatusResponse)
    assert health.data.status == "ok"
    token_request, api_request = api.requests
    assert str(token_request.url) == TOKEN_URL
    assert api_request.headers["Authorization"] == "Bearer token-1"
    assert api_request.headers["User-Agent"] == default_user_agent()
    assert token_request.headers["User-Agent"] == default_user_agent()


def test_works_with_the_async_functions(api: FakeApi) -> None:
    api.responses += [token_response("token-1"), health_response(), health_response()]
    client = create_client(credentials())

    async def run() -> None:
        async with client:
            await get_health.asyncio(client=client)

    asyncio.run(run())
    get_health.sync(client=client)
    assert len(api.token_requests) == 1


def test_retries_429(api: FakeApi) -> None:
    api.responses += [
        token_response(),
        error_response(429, "Too Many Requests", headers={"Retry-After": "1"}),
        health_response(),
    ]

    health = get_health.sync(client=create_client(credentials()))

    assert isinstance(health, HealthStatusResponse)


def test_documented_errors_are_returned_as_api_error(api: FakeApi) -> None:
    api.responses += [token_response(), error_response(404, "Purchase not found")]

    result = get_purchase.sync(123, client=create_client(credentials()))

    assert isinstance(result, ApiError)
    assert result.message == "Purchase not found"
    assert result.data is None
    assert result.meta is None


def test_unwrap_returns_the_parsed_body(api: FakeApi) -> None:
    api.responses += [token_response(), health_response()]

    health: HealthStatusResponse = unwrap(
        get_health.sync_detailed(client=create_client(credentials()))
    )

    assert health.data.status == "ok"


def test_unwrap_raises_api_exception(api: FakeApi) -> None:
    api.responses += [
        token_response(),
        error_response(404, "Purchase not found", headers={"X-Request-Id": "abc"}),
    ]

    with pytest.raises(ApiException) as info:
        unwrap(get_purchase.sync_detailed(123, client=create_client(credentials())))

    assert info.value.status_code == 404
    assert info.value.error.message == "Purchase not found"
    assert info.value.headers["X-Request-Id"] == "abc"
    assert str(info.value) == "HTTP 404: Purchase not found"


def test_undocumented_status_codes_raise_unexpected_status(api: FakeApi) -> None:
    api.responses += [token_response(), error_response(503, "Maintenance")]

    with pytest.raises(UnexpectedStatus) as info:
        get_purchase.sync(123, client=create_client(credentials()))

    assert info.value.status_code == 503


def test_inline_envelopes_accept_null_message_and_meta(api: FakeApi) -> None:
    body = {"error": 0, "message": None, "data": None, "meta": None}
    api.responses += [
        token_response(),
        httpx.Response(200, json=body),
        httpx.Response(200, json=body),
    ]
    client = create_client(credentials())

    # Nothing to pay: the total is 0.00.
    payment = unwrap(pay_orders.sync_detailed(client=client, body=OrderPayRequest(order_ids=[1])))
    antivirus = unwrap(get_hosting_antivirus.sync_detailed(1, client=client))

    assert (payment.data, payment.message, payment.meta) == (None, None, None)
    assert (antivirus.data, antivirus.message, antivirus.meta) == (None, None, None)


def test_list_tasks_sends_only_the_parameters_with_a_default(api: FakeApi) -> None:
    body: dict[str, Any] = {
        "error": 0,
        "message": None,
        "data": [],
        "meta": {"total": 0, "count": 0, "pages": 0, "page": 1, "per_page": 15},
    }
    api.responses += [token_response(), httpx.Response(200, json=body)]

    unwrap(list_tasks.sync_detailed(client=create_client(credentials())))

    assert dict(api.api_requests[0].url.params) == {
        "alive_only": "true",
        "page": "1",
        "per_page": "15",
    }


def test_downloads_return_the_bytes(api: FakeApi) -> None:
    pdf = b"%PDF-1.7 binary \x00\xff"
    api.responses += [
        token_response(),
        httpx.Response(
            200,
            content=pdf,
            headers={
                "Content-Type": "application/pdf",
                "Content-Disposition": 'attachment; filename="1.pdf"',
            },
        ),
    ]

    response = download_invoice_pdf.sync_detailed(1, client=create_client(credentials()))
    file = unwrap(response)

    assert file.payload.read() == pdf
    assert response.headers["Content-Disposition"] == 'attachment; filename="1.pdf"'


def test_a_429_after_the_retries_raises_api_exception(api: FakeApi) -> None:
    too_many_requests = error_response(429, "Too Many Requests", headers={"Retry-After": "1"})
    api.responses += [token_response(), too_many_requests, too_many_requests, too_many_requests]

    with pytest.raises(ApiException) as info:
        unwrap(get_purchase.sync_detailed(123, client=create_client(credentials())))

    assert info.value.status_code == 429
    assert info.value.headers["Retry-After"] == "1"
    assert len(api.api_requests) == 3


def test_without_retry(api: FakeApi) -> None:
    api.responses += [
        token_response(),
        error_response(429, "Too Many Requests", headers={"Retry-After": "1"}),
    ]

    with pytest.raises(ApiException) as info:
        unwrap(get_purchase.sync_detailed(123, client=create_client(credentials(), retry=False)))

    assert info.value.status_code == 429
    assert len(api.api_requests) == 1
    assert CLIENT_ID not in str(info.value)


PAYMENT = {
    "payment_id": 7,
    "payment_method": "prepaid_credit",
    "payment_code": "PAY-7",
    "amount_total": {"amount": 12.2, "currency": "EUR"},
    "amount_payed": {"amount": 12.2, "currency": "EUR"},
    "date_payment": "2026-09-30T12:00:00+02:00",
    "payed": True,
    "prepaid_credit_operations": [],
    "provider_data": None,
}


def test_pay_orders_returns_the_payment(api: FakeApi) -> None:
    body = {"error": 0, "message": "", "data": PAYMENT, "meta": {}}
    api.responses += [token_response(), httpx.Response(200, json=body)]
    order = OrderPayRequest(order_ids=[1, 2], use_prepaid_credit=True)

    result = unwrap(pay_orders.sync_detailed(client=create_client(credentials()), body=order))

    assert isinstance(result.data, Payment)
    assert result.data.payment_id == 7
    assert json.loads(api.api_requests[0].content) == {
        "order_ids": [1, 2],
        "use_prepaid_credit": True,
    }
