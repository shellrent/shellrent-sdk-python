from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PaymentProviderData")


@_attrs_define
class PaymentProviderData:
    """Data of an attempt of the payment, as given by the payment provider: which fields are set, and their format, depend
    on the provider

    """

    payed: bool | None
    """ Whether the attempt was paid """
    authorization_token: None | str
    """ Id of the authorization or of the order at the provider """
    authorization_code: None | str
    """ Authorization code of the transaction at the provider """
    status: None | str
    """ Status of the attempt at the provider, for example `OK` or `COMPLETED` """
    status_code: None | str
    """ Result code of the provider, for example `0` or `DECLINED`; `THRESHOLD_EXCEEDED` when the attempt was
    refused for the payment limits """
    message: None | str
    """ Message of the provider about the result """
    payer_name: None | str
    """ First name of the payer, as given by the provider """
    payer_surname: None | str
    """ Surname of the payer, as given by the provider """
    payer_email: None | str
    """ Email address of the payer, as given by the provider """
    bank_issuer: None | str
    """ Bank of the payer: the issuer of the card or the bank of the transfer """
    creditcard_pan: None | str
    """ Number of the card, masked or reduced to the last digits """
    creditcard_issuer: None | str
    """ Brand of the card, for example `VISA`, `MASTERCARD` or `AMEX` """
    creditcard_expiration: None | str
    """ Expiry of the card as `YYYY-MM-DD`, the last day of its month; for the methods without a card, the expiry
    set for the authorization """
    region: None | str
    """ Area of the card or of the payment, for example `EUROPE` or `SEPA` """
    transaction_type: None | str
    """ Type of the transaction at the provider, for example `NO_3DSECURE`, `DEBIT` or `TRF` (transfer) """
    payment_type: None | str
    """ Type of the payment at the provider, for example `PAYMENT_METHOD_TOKEN` or `CARD`; `Storno` for a payment
    created by the cancellation of another one """
    payment_date: datetime.datetime | None
    """ When the transaction took place at the provider """
    product_type: None | str
    """ Product of the card as given by the provider, for example `VISA` """
    nationality: None | str
    """ Country of the card or of the payer, as an ISO 3166-1 alpha-2 or alpha-3 code depending on the provider """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        payed: bool | None
        payed = self.payed

        authorization_token: None | str
        authorization_token = self.authorization_token

        authorization_code: None | str
        authorization_code = self.authorization_code

        status: None | str
        status = self.status

        status_code: None | str
        status_code = self.status_code

        message: None | str
        message = self.message

        payer_name: None | str
        payer_name = self.payer_name

        payer_surname: None | str
        payer_surname = self.payer_surname

        payer_email: None | str
        payer_email = self.payer_email

        bank_issuer: None | str
        bank_issuer = self.bank_issuer

        creditcard_pan: None | str
        creditcard_pan = self.creditcard_pan

        creditcard_issuer: None | str
        creditcard_issuer = self.creditcard_issuer

        creditcard_expiration: None | str
        creditcard_expiration = self.creditcard_expiration

        region: None | str
        region = self.region

        transaction_type: None | str
        transaction_type = self.transaction_type

        payment_type: None | str
        payment_type = self.payment_type

        payment_date: None | str
        if isinstance(self.payment_date, datetime.datetime):
            payment_date = self.payment_date.isoformat()
        else:
            payment_date = self.payment_date

        product_type: None | str
        product_type = self.product_type

        nationality: None | str
        nationality = self.nationality

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "payed": payed,
                "authorization_token": authorization_token,
                "authorization_code": authorization_code,
                "status": status,
                "status_code": status_code,
                "message": message,
                "payer_name": payer_name,
                "payer_surname": payer_surname,
                "payer_email": payer_email,
                "bank_issuer": bank_issuer,
                "creditcard_pan": creditcard_pan,
                "creditcard_issuer": creditcard_issuer,
                "creditcard_expiration": creditcard_expiration,
                "region": region,
                "transaction_type": transaction_type,
                "payment_type": payment_type,
                "payment_date": payment_date,
                "product_type": product_type,
                "nationality": nationality,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_payed(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        payed = _parse_payed(d.pop("payed"))

        def _parse_authorization_token(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        authorization_token = _parse_authorization_token(d.pop("authorization_token"))

        def _parse_authorization_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        authorization_code = _parse_authorization_code(d.pop("authorization_code"))

        def _parse_status(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        status = _parse_status(d.pop("status"))

        def _parse_status_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        status_code = _parse_status_code(d.pop("status_code"))

        def _parse_message(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        message = _parse_message(d.pop("message"))

        def _parse_payer_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        payer_name = _parse_payer_name(d.pop("payer_name"))

        def _parse_payer_surname(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        payer_surname = _parse_payer_surname(d.pop("payer_surname"))

        def _parse_payer_email(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        payer_email = _parse_payer_email(d.pop("payer_email"))

        def _parse_bank_issuer(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        bank_issuer = _parse_bank_issuer(d.pop("bank_issuer"))

        def _parse_creditcard_pan(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        creditcard_pan = _parse_creditcard_pan(d.pop("creditcard_pan"))

        def _parse_creditcard_issuer(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        creditcard_issuer = _parse_creditcard_issuer(d.pop("creditcard_issuer"))

        def _parse_creditcard_expiration(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        creditcard_expiration = _parse_creditcard_expiration(d.pop("creditcard_expiration"))

        def _parse_region(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        region = _parse_region(d.pop("region"))

        def _parse_transaction_type(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        transaction_type = _parse_transaction_type(d.pop("transaction_type"))

        def _parse_payment_type(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        payment_type = _parse_payment_type(d.pop("payment_type"))

        def _parse_payment_date(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                payment_date_type_0 = datetime.datetime.fromisoformat(data)

                return payment_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        payment_date = _parse_payment_date(d.pop("payment_date"))

        def _parse_product_type(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        product_type = _parse_product_type(d.pop("product_type"))

        def _parse_nationality(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        nationality = _parse_nationality(d.pop("nationality"))

        payment_provider_data = cls(
            payed=payed,
            authorization_token=authorization_token,
            authorization_code=authorization_code,
            status=status,
            status_code=status_code,
            message=message,
            payer_name=payer_name,
            payer_surname=payer_surname,
            payer_email=payer_email,
            bank_issuer=bank_issuer,
            creditcard_pan=creditcard_pan,
            creditcard_issuer=creditcard_issuer,
            creditcard_expiration=creditcard_expiration,
            region=region,
            transaction_type=transaction_type,
            payment_type=payment_type,
            payment_date=payment_date,
            product_type=product_type,
            nationality=nationality,
        )

        payment_provider_data.additional_properties = d
        return payment_provider_data

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
