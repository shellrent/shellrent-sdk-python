# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.3.0] - 2026-10-01

### Added

- `unwrap(response, unexpected_status_type=...)`: another generated client passes its own
  `UnexpectedStatus`, so that `unwrap()` raises the same exception as its generated functions
  instead of the `UnexpectedStatus` of `shellrent_sdk.client`, which its callers would not catch.
  Without it, `unwrap()` raises the `UnexpectedStatus` of `shellrent_sdk.client` as before.
- `ServiceServerPaginatedListResponse`, from the updated specification.

### Changed

- `FileTokenStore()` without a directory follows `SHELLRENT_TOKEN_CACHE`, like the `shellrent`
  command: a directory, or `off` to keep the tokens in memory without writing any file. A directory
  passed to `FileTokenStore` still wins. The command now uses `FileTokenStore()` itself, with the
  same behaviour as before.
- Functions and models regenerated from the updated specification of the Shellrent API:
  - the default of `per_page` in the list operations is 15 instead of 20, as in the API;
  - `list_active_monitoring_products` and `list_private_cloud_sv_products` return
    `ServicePaginatedListResponse`, `list_cloud_vps_products` and `list_dedicated_server_products`
    return `ServiceServerPaginatedListResponse`: their `meta` is a `PaginationMeta`.

### Removed

- `ServiceListResponse`, `ServiceListResponseMetaType0`, `ServiceServerListResponse` and
  `ServiceServerListResponseMetaType0`, no longer in the specification: use
  `ServicePaginatedListResponse` and `ServiceServerPaginatedListResponse`.

## [0.2.0] - 2026-10-01

### Added

- `unwrap(response, error_type=...)`: another generated client passes its own `ApiError` model, so
  that its documented error responses raise `ApiException` instead of `UnexpectedStatus`. Without
  `error_type`, `unwrap()` works and is typed as before.
- `ApiErrorLike`, the protocol of the error envelopes of the generated clients (`error` and
  `message`).

### Changed

- `ApiException.error` is typed as `ApiErrorLike` instead of `ApiError`, so that it accepts the
  `ApiError` of any generated client. At runtime it is still the `ApiError` of the response; for its
  other fields, narrow it with `isinstance(e.error, ApiError)`.
- The message of `ApiException` is `HTTP <status>` when the envelope has no `message`.

## [0.1.0] - 2026-09-30

### Added

- Functions and models for the Shellrent API 3.0.0 (OpenAPI 3.1 specification), generated with
  openapi-python-client 0.29.1: nullable references typed as `Model | None`, required fields without
  `Unset`, `OrderPayRequest` as the body of `pay_orders` and `Payment | None` as its data, and the 429
  responses documented.
- `create_client()`, returning the generated client configured for the API.
- OAuth2 client credentials authentication (`shellrent_sdk.auth.OAuth2Auth`), with the token cached in
  memory, in files (`FileTokenStore`) or in any store implementing `TokenStore`.
- Retries of the requests rejected with 429 Too Many Requests, following `Retry-After`
  (`shellrent_sdk.http.RetryTransport`). Like the default transports of httpx, it follows `HTTP_PROXY`,
  `HTTPS_PROXY`, `ALL_PROXY`, `NO_PROXY`, `SSL_CERT_FILE` and `SSL_CERT_DIR` (`trust_env=False` ignores
  them).
- `unwrap()` and `ApiException`, to turn the documented error responses into exceptions, including the
  429 left after the retries.
- `TokenError`, with the OAuth2 `error` and `error_description` of the token endpoint, such as
  `invalid_client` or, for its rate limit, `rate_limited`.
- The `shellrent` command, with `shellrent api` and `shellrent token`.

[Unreleased]: https://github.com/shellrent/shellrent-sdk-python/compare/v0.3.0...HEAD
[0.3.0]: https://github.com/shellrent/shellrent-sdk-python/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/shellrent/shellrent-sdk-python/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/shellrent/shellrent-sdk-python/releases/tag/v0.1.0
