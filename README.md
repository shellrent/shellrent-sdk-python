# Shellrent Python SDK

[![CI](https://github.com/shellrent/shellrent-sdk-python/actions/workflows/ci.yml/badge.svg)](https://github.com/shellrent/shellrent-sdk-python/actions/workflows/ci.yml)

Official Python SDK for the [Shellrent](https://www.shellrent.com) public API: domains, hosting,
servers, storage, SSL certificates, purchases and billing.

The functions and the models are generated from the OpenAPI specification with
[openapi-python-client](https://github.com/openapi-generators/openapi-python-client); the SDK adds
OAuth2 authentication, token caching, retries on rate limits and the `shellrent` command.

## Requirements

Python 3.11 or later.

## Installation

```bash
pip install shellrent-sdk
```

With [uv](https://docs.astral.sh/uv/):

```bash
uv add shellrent-sdk
```

## Authentication

The API uses OAuth2 with the client credentials grant. Create the client with the ID and the secret
of your API client:

```python
from shellrent_sdk import ClientCredentials, create_client

client = create_client(ClientCredentials("your-client-id", "your-client-secret"))
```

The SDK requests an access token on the first call, sends it with every request and requests a new
one shortly before it expires (tokens last 10 minutes). If the API answers 401, the SDK requests a
new token and sends the request once more.

By default the token has every scope assigned to the client and the only audience of the client.
To request less, or to choose the audience of a client that has more than one:

```python
credentials = ClientCredentials(
    "your-client-id",
    "your-client-secret",
    scopes=["purchases:read", "billing:read"],
    audience="api-public",
)
```

`create_client()` without credentials, like `ClientCredentials.from_env()`, reads them from these
environment variables:

| Variable | Value |
| --- | --- |
| `SHELLRENT_CLIENT_ID` | required |
| `SHELLRENT_CLIENT_SECRET` | required |
| `SHELLRENT_SCOPES` | optional, separated by spaces or commas |
| `SHELLRENT_API_URL` | optional, default `https://api.shellrent.com` |

To use another environment, such as staging, set `SHELLRENT_API_URL` or pass `api_url=` to
`ClientCredentials`: both the token and the API calls then go to that URL. `repr()` of the
credentials never shows the secret.

## Token cache

By default each client keeps its token in memory (`MemoryTokenStore`). To share the token between
processes, such as the workers of a web application or scripts run by cron, pass a `FileTokenStore`:
this saves a token request per process and keeps you within the limit of the token endpoint
(5 requests every 15 seconds).

```python
from shellrent_sdk import FileTokenStore, create_client

# $XDG_CACHE_HOME/shellrent-sdk, or ~/.cache/shellrent-sdk
client = create_client(token_store=FileTokenStore())

# In a web application the home directory of the server user may not be writable:
client = create_client(token_store=FileTokenStore("/var/cache/myapp/shellrent"))
```

`FileTokenStore` creates its directory readable by its owner only (0700) and writes each token
atomically to a file with mode 0600. The client secret is never cached.

Any object with the methods of the `TokenStore` protocol works as well: `get(key)`, returning `None`
for missing or expired keys, `set(key, value, ttl)` and `delete(key)`. Django's cache has them already
(`create_client(token_store=django.core.cache.cache)`); for Redis:

```python
class RedisTokenStore:
    def __init__(self, redis):
        self.redis = redis

    def get(self, key):
        value = self.redis.get(key)
        return value.decode() if value is not None else None

    def set(self, key, value, ttl):
        self.redis.set(key, value, ex=ttl)

    def delete(self, key):
        self.redis.delete(key)
```

## Usage

The operations are in `shellrent_sdk.client.api`: one package per tag of the specification, one
module per `operationId`, in snake case. For example `listPurchases`, tagged `Purchases`, is
`shellrent_sdk.client.api.purchases.list_purchases`. The packages are `account`, `billing`,
`domains`, `health`, `hosting`, `license_`, `monitoring`, `o_auth`, `payment`, `pec`, `purchases`,
`server`, `shop`, `sms`, `ssl` and `storage`; the models are in `shellrent_sdk.client.models`.

Each module has four functions with the same arguments: `sync()` and `asyncio()` return the parsed
body, `sync_detailed()` and `asyncio_detailed()` return a `Response` that also has `status_code`,
`headers` and the raw `content`. Path parameters are positional, the others keyword-only.

```python
from shellrent_sdk import create_client, unwrap
from shellrent_sdk.client.api.purchases import get_purchase, list_purchases

with create_client() as client:
    purchases = unwrap(list_purchases.sync_detailed(client=client, page=1, per_page=50))
    for purchase in purchases.data:
        print(purchase.purchase_id, purchase.purchase_name)
    print(f"Page {purchases.meta.page} of {purchases.meta.pages}")

    purchase = unwrap(get_purchase.sync_detailed(123, client=client)).data
```

Every JSON response has the envelope `{error, message, data, meta}`: `data` is the payload, `meta`
the pagination, if any. The client can be used for many calls; `with` closes its connections at the
end. The same client works with `asyncio`:

```python
import asyncio

from shellrent_sdk import create_client, unwrap
from shellrent_sdk.client.api.purchases import get_purchase


async def main() -> None:
    async with create_client() as client:
        calls = [get_purchase.asyncio_detailed(n, client=client) for n in (1, 2, 3)]
        for response in await asyncio.gather(*calls):
            print(unwrap(response).data.purchase_name)


asyncio.run(main())
```

Operations that download a file, such as `download_invoice_pdf`, return a `File` with the bytes in
`payload`; the file name is in the `Content-Disposition` header. `download_invoice_xml` and
`download_credit_note_xml` return the XML or, for signed documents, the p7m file: see `Content-Type`.

```python
from pathlib import Path

from shellrent_sdk.client.api.billing import download_invoice_pdf

response = download_invoice_pdf.sync_detailed(456, client=client)
Path("invoice.pdf").write_bytes(unwrap(response).payload.read())
```

`create_client()` also takes these options:

```python
client = create_client(
    credentials,
    token_store=FileTokenStore(),  # see "Token cache"
    retry=False,  # do not retry the requests rejected with 429
    timeout=60.0,  # seconds, default 30
)
```

As with httpx, the requests follow the proxy and certificate settings of the environment:
`HTTP_PROXY`, `HTTPS_PROXY`, `ALL_PROXY`, `NO_PROXY`, `SSL_CERT_FILE` and `SSL_CERT_DIR`.

## Error handling

`sync()` and `asyncio()` return the error responses documented in the specification as `ApiError`,
the error envelope, so you would check the type of every result. `unwrap()` does that for you: it
takes the result of `sync_detailed()` or `asyncio_detailed()`, returns the parsed body of a 2xx
response and raises `ApiException` for the documented errors.

```python
import httpx

from shellrent_sdk import ApiException, TokenError, UnexpectedStatus, unwrap

try:
    purchase = unwrap(get_purchase.sync_detailed(123, client=client))
except ApiException as e:
    # A documented error response, such as 404
    print(e.status_code, e.error.message)
except UnexpectedStatus as e:
    # A status code missing from the specification, such as 503
    print(e.status_code, e.content)
except TokenError as e:
    # The token endpoint refused the credentials, such as invalid_client
    print(e.error, e.error_description)
except httpx.TransportError as e:
    # Network errors and timeouts
    print(e)
```

- `ApiException` has `status_code`, `error` (the envelope, with `message`), `headers` and `content`.
- `UnexpectedStatus`, raised by the generated functions, has `status_code` and `content`.
- `TokenError` has the OAuth2 `error` and `error_description`, and the HTTP `status_code` of the
  token endpoint.

The API accepts 60 requests a minute per client. Requests rejected with 429 Too Many Requests, the
token requests included, are retried up to twice after the time given by `Retry-After`, if it is no
more than 60 seconds. If they are rejected again, `unwrap()` raises `ApiException` with
`status_code` 429 and `Retry-After` in `headers`; for the token endpoint, `TokenError` with `error`
`rate_limited`. `create_client(retry=False)` turns the retries off.

## Command line

The package installs the `shellrent` command, modelled on `gh api`: it sends a request to any path
of the API and prints the body of the response on stdout. It reads the credentials only from the
environment variables above: there is no option for the secret, which would show in `ps` and in the
shell history.

```bash
export SHELLRENT_CLIENT_ID=your-client-id
export SHELLRENT_CLIENT_SECRET=your-client-secret

shellrent api GET /api/v3/purchases | jq '.data[] | {purchase_id, name: .purchase_name.full_name}'
shellrent api GET '/api/v3/purchases?page=2&per_page=50' | jq -r '.data[].purchase_id'

# JSON body: as text, from a file with @, from stdin with -
shellrent api POST /api/v3/orders/pay --data '{"order_ids": [123], "use_prepaid_credit": true}'
shellrent api POST /api/v3/orders/pay --data @order.json
jq -n '{order_ids: [123], use_prepaid_credit: true}' | shellrent api POST /api/v3/orders/pay --data -

# Files are written as they are
shellrent api GET /api/v3/invoices/456/download/pdf > invoice.pdf

# An access token for other tools
curl -H "Authorization: Bearer $(shellrent token)" https://api.shellrent.com/api/v3/purchases
```

| Exit status | Meaning |
| --- | --- |
| 0 | 2xx response |
| 1 | HTTP error (the body is still on stdout, the status on stderr) or failed request |
| 2 | usage error, missing credentials, or credentials refused by the token endpoint |

```bash
if ! body=$(shellrent api GET /api/v3/purchases/123); then
    echo "Failed: $(jq -r .message <<<"$body")" >&2
fi
```

Each run is a new process, so the command keeps the token in a file, in `$XDG_CACHE_HOME/shellrent-sdk`
or `~/.cache/shellrent-sdk`, and reuses it until it expires: scripts run by cron do not request a
token every time. `SHELLRENT_TOKEN_CACHE` sets another directory, or `off` to keep the token only
for the current run. `python -m shellrent_sdk` is the same as `shellrent`, and
`uvx --from shellrent-sdk shellrent` runs it without installing it.

## Using httpx directly

`shellrent_sdk.auth` and `shellrent_sdk.http` do not depend on the generated code.
`shellrent_sdk.http.client_args()` returns the arguments of an `httpx.Client` or `httpx.AsyncClient`
with the authentication, the retries, the `User-Agent` and the timeout of the SDK:

```python
import httpx

from shellrent_sdk import ClientCredentials
from shellrent_sdk.http import client_args

with httpx.Client(**client_args(ClientCredentials.from_env())) as http:
    print(http.get("/api/v3/purchases").json())
```

## Regenerating the code

The code in `src/shellrent_sdk/client/` is generated from `spec/openapi.yaml`: do not edit it by
hand. To regenerate it, with [uv](https://docs.astral.sh/uv/) installed:

```bash
bin/generate
```

The script runs openapi-python-client (version pinned in the script) with
`openapi-python-client.yaml`, replacing the whole directory. CI fails if the committed code differs
from the generated one.

## Versioning

The SDK follows [Semantic Versioning](https://semver.org):

- new operations or models: minor version;
- renamed or removed operations (`operationId`) or models: major version, since modules and classes
  change name;
- fixes: patch version.

Changes are listed in [CHANGELOG.md](CHANGELOG.md).

## License

MIT, see [LICENSE](LICENSE).
