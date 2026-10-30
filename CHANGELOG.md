# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.1.0] - 2026-10-30

Regenerated from the Shellrent API specification with the new SSL checks of the hosting and the discounted
renew price of the purchases. No breaking changes in names or signatures.

### Added

- `can_install_hosting_ssl_certificate` (`hosting`, `GET /api/v3/hostings/{hosting_id}/ssl-certificates/can-install`):
  whether an SSL certificate can be installed on the hosting now, with the same fields of the installation as
  keyword-only query parameters, and why not (`reason`). For a Let's Encrypt certificate, `dns_delegation` has the
  CNAME record that delegates its DNS validation, which must be created when the DNS are not on the Shellrent
  nameservers.
- `HostingSslCertificateCanInstall`, `HostingSslCertificateCanInstallResponse`, `HostingSslDnsDelegation`, the enum
  `HostingSslCertificateCanInstallReason` (`ALREADY_INSTALLED`, `CNAME_MISSING`, `LIMIT_REACHED`,
  `MAIL_NOT_SUPPORTED`, `OPERATION_RUNNING`) and the enums of the query parameters
  `CanInstallHostingSslCertificateDestinationType` and `CanInstallHostingSslCertificateCnType`.
- `Purchase.renew_price_discounted` (`Amount | None`): the renew price with the discount of the discount promotion
  applied to the purchase; `None` without a discount and for sub-accounts.

### Changed

- `HostingSslCertificateInstallRequest.destination_type` defaults to `UNSET` instead of `web`, and is not sent
  unless set: the API then installs on the website and the mail of a main hosting (`all`), or on the website of a
  subdomain (`web`). `cn_type` defaults to `WILDCARD` instead of `NORMAL`, and is ignored with
  `ssl_certificate_id`.
- `install_hosting_ssl_certificate` follows the rules of the control panel. A Let's Encrypt certificate with DNS
  that are not on the Shellrent nameservers requires the CNAME record of `dns_delegation` (409 without it).
  `ssl_certificate_id` accepts only the active certificates of the owner of the hosting (404 otherwise), and on the
  mail servers only wildcard certificates or certificates with SAN (400). A certificate already installed, the limit
  of Let's Encrypt installations or an operation running respond 409 instead of 400, and a mail server that does
  not accept certificates responds 403.
- Descriptions of the OAuth2 errors updated with `unauthorized_client` (owner of the client without two-factor
  authentication).

## [1.0.0] - 2026-10-16

Functions and models regenerated from the updated specification of the Shellrent API, which renames
paths, parameters and models: see the lists below to update the code written for 0.3.0.

### Added

- `create_prepaid_credit_payment` and `create_one_click_payment` (`payment`), which replace
  `pay_orders`, with `PrepaidCreditPaymentCreateRequest` and `OneClickPaymentCreateRequest`.
- `create_server_power_action` (`server`), with `ServerPowerActionRequest`: it replaces
  `start_server`, `stop_server`, `reboot_server`, `hard_stop_server` and `hard_reboot_server`.
- `can_reissue_ssl_certificate` and `reissue_ssl_certificate` (`ssl`), which replace
  `can_reemit_ssl_certificate` and `reemit_ssl_certificate`.
- `get_pec_mailbox_owner_change` (`pec`) and `list_private_cloud_available_ip_addresses` (`server`).
- `License`, `LicenseResponse` and `LicensePaginatedListResponse`, for both cPanel and Plesk.
- `DomainDetail` and `DomainDetailResponse`, returned by `get_domain`; `DomainNameserver` and
  `DomainPremiumPrices`.
- `Hosting.http_version`, `Hosting.file_protection_enabled` and `Hosting.php_settings`
  (`HostingPhpSetting`), `DomainAvailability.premium` and `DomainAvailability.premium_prices`,
  `ApiErrorMetaType0.errors` (the errors of each field in validation errors).
- Enums for request fields that were `str` or `int`: `DomainDnsRecordRequestType`,
  `DomainDnsZoneRequestZoneTtl`, `HostingCronjobCreateRequestRequestProtocol`,
  `HostingCronjobCreateRequestHttpRequestMethod`, `HostingHttpVersionUpdateRequestVersion`,
  `HostingPhpSettingsUpdateRequestSetting`, `HostingSslCertificateInstallRequestCnType`,
  `HostingSslCertificateInstallRequestDestinationType` and `SslCertificateExportRequestFormat`.

### Changed

- `unwrap()` returns `None` for a 204 No Content response instead of raising `UnexpectedStatus`:
  the specification now documents 204 for the deletions, `cancel_order`, `cancel_purchase`,
  `apply_domain_contact_changes`, `revoke_one_click_autorenew` and the payments with nothing to pay.
  The generated functions type these responses as `Any` instead of `EmptyResponse`.
- Path parameters renamed: `creditnote_id` → `credit_note_id` (`billing`), `cronjob_id` →
  `cron_job_id` (`hosting`), `microsoft365_id` → `microsoft_365_subscription_id` (`license_`),
  `topup_id` → `top_up_id` (`get_prepaid_credit_topup`).
- Parameters moved from the path to keyword-only query parameters: `recurrence_id` of
  `can_change_purchase_recurrence`, `status` of `can_change_purchase_renew_status`, `domain_name`
  of `list_ssl_approver_emails`. `export_ssl_certificate` takes the format in the body
  (`SslCertificateExportRequest`) instead of the positional `format_`.
- `create_hosting_database` has no body: the API chooses the name of the database.
- New keyword-only parameters: `one_click_id` and `prepaid_credit` of `can_pay_order`, `page` and
  `per_page` of `list_sms_messages` and `list_sms_prices`. The `body` of `upload_file` is required
  and `UploadFileBody` has the `file` field.
- Return types: `create_server_network_interface`, `delete_server_network_interface`,
  `create_object_storage_bucket_firewall_entry` and `delete_object_storage_bucket_firewall_entry`
  return `TaskResponse`; `update_private_cloud_virtual_machine` returns `EmptyResponse` when no
  resource changes; `get_hosting_antivirus` returns `HostingAntivirusNullableResponse`.
- The default of `per_page` in the list operations is 20, as in the specification.
- `error` of the success envelopes is `Literal[0]`. The fields that are always null are `Any`:
  `meta` of the envelopes that are not paginated lists, `data` of `EmptyResponse` and of `ApiError`.
- The package is classified as `Development Status :: 5 - Production/Stable`.
- Model fields: many fields are now nullable or required as in the API, some request fields are
  enums (see Added), `Domain.nameservers` is a list of `DomainNameserver`,
  `Payment.provider_data` is `PaymentProviderData | None`, `ObjectStorage.code`,
  `ObjectStorageBucket.code` and `ObjectStorageIamUser.code` are `int | None`,
  `ObjectStorageBucket.creation_date` is a date, `ApiUpload.upload_date` a datetime, the `tlsa_*`
  fields of `HostingDnsRecord` are `int | None`, `Creditnote.creditnote_year` is `int | None`.

### Removed

- `pay_orders` and `OrderPayRequest`: use `create_prepaid_credit_payment` or
  `create_one_click_payment`.
- `start_server`, `stop_server`, `reboot_server`, `hard_stop_server` and `hard_reboot_server`: use
  `create_server_power_action`. `start_server_first_backup` and `create_hosting_catch_all` (use
  `update_hosting_catch_all`, which creates or replaces it).
- Secure Mail: `buy_secure_mail`, `buy_secure_mail_for_google_workspace`,
  `buy_secure_mail_for_microsoft_365`, `list_secure_mails`, `get_secure_mail`,
  `get_secure_mail_statistics`, `list_secure_mail_mailboxes`, `upgrade_secure_mail_quantity`,
  `downgrade_secure_mail_quantity`, the `Securemail*` and `BuyServiceSecuremail*` models and
  `Purchase.securemail_id`.
- `can_reemit_ssl_certificate`, `reemit_ssl_certificate` and `SslCertificateCanReemit*`.
- Models renamed: `CpanelLicense*` and `PleskLicense*` → `License*`, `DomainResponse` →
  `DomainDetailResponse`, `HostingEmailBlocList*` → `HostingEmailBlockList*`,
  `PaymentProviderDataType0` → `PaymentProviderData`, `GetHostingAntivirusResponse200` →
  `HostingAntivirusNullableResponse`. Also removed: the `*ResponseMetaType0` models of the `meta`
  that is always null (such as `PaymentResponseMetaType0`), `EmptyResponseDataType0`,
  `ApiErrorDataType0`, `HostingDatabaseCreateRequest`, `PayOrdersResponse200`,
  `BuyServiceObjectStorageRequestConfigurationTbSize` (`tb_size` is an `int`).
- Fields no longer in the API: `Domain.dnssec_enabled`, the `ns_*_ip` of
  `DomainDnsNameserversChangeRequest`, `HostingSubdomainCreateRequest.subdomain`,
  `Microsoft365DomainAvailable.microsoft_uuid`, `ObjectStorageIamUser.firewall_policy`,
  `OneClick.one_click_preference`, `PecOwnerChange.person_id_accept` and `person_id_reject`,
  `ServerBackup.backup_path` and `backup_path_parent`.

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

[Unreleased]: https://github.com/shellrent/shellrent-sdk-python/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/shellrent/shellrent-sdk-python/compare/v0.3.0...v1.0.0
[0.3.0]: https://github.com/shellrent/shellrent-sdk-python/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/shellrent/shellrent-sdk-python/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/shellrent/shellrent-sdk-python/releases/tag/v0.1.0
