from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.api_error_meta_type_0 import ApiErrorMetaType0


T = TypeVar("T", bound="ApiError")


@_attrs_define
class ApiError:
    """Error response: the code in `error`, the description in `message`, the errors for each field in `meta` for
    validation errors

    """

    error: int
    """ Error code: 1000 validation failed (details in `meta.errors`), 1001 bad request, 1100 access token missing,
    invalid, expired or revoked (HTTP 401: request a new token and retry once), 1101 insufficient scope (HTTP 403:
    the token lacks a scope listed in the `WWW-Authenticate` header), 1102 the access token audience is not valid
    for this API (HTTP 403), 1200 not found, 1201 not implemented, 1202 method not allowed, 1300 rate limited, 1400
    conflict with a business rule or with the state of the resource, 1500 server error, 1601 forbidden (for example
    a feature not included in the plan, an operation not available to sub-accounts, the internal API without
    administrator privileges, or a request from an IP address not allowed for the account), 1700 payment declined by
    the payment provider (HTTP 402: the orders are still to be paid), 1 other errors. Do not retry 403 responses
    with a new token: the result does not change. """
    message: str
    """ Description of the error, for the developers of the client """
    data: Any
    """ Always null in error responses """
    meta: ApiErrorMetaType0 | None
    """ Null, except in validation errors (HTTP 400 with error 1000), where it contains `errors` """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_error_meta_type_0 import ApiErrorMetaType0

        error = self.error

        message = self.message

        data = self.data

        meta: dict[str, Any] | None
        if isinstance(self.meta, ApiErrorMetaType0):
            meta = self.meta.to_dict()
        else:
            meta = self.meta

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "error": error,
                "message": message,
                "data": data,
                "meta": meta,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.api_error_meta_type_0 import ApiErrorMetaType0

        d = dict(src_dict)
        error = d.pop("error")

        message = d.pop("message")

        data = d.pop("data")

        def _parse_meta(data: object) -> ApiErrorMetaType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                meta_type_0 = ApiErrorMetaType0.from_dict(data)

                return meta_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ApiErrorMetaType0 | None, data)

        meta = _parse_meta(d.pop("meta"))

        api_error = cls(
            error=error,
            message=message,
            data=data,
            meta=meta,
        )

        api_error.additional_properties = d
        return api_error

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
