from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="HostingEmailWblistRequest")


@_attrs_define
class HostingEmailWblistRequest:
    """Sender to add to the allow list or the block list of the antispam: a whole domain or an address"""

    domain: None | str | Unset = UNSET
    """ Sender domain; send either `domain` or `mailbox` """
    mailbox: None | str | Unset = UNSET
    """ Sender address; send either `domain` or `mailbox` """

    def to_dict(self) -> dict[str, Any]:
        domain: None | str | Unset
        if isinstance(self.domain, Unset):
            domain = UNSET
        else:
            domain = self.domain

        mailbox: None | str | Unset
        if isinstance(self.mailbox, Unset):
            mailbox = UNSET
        else:
            mailbox = self.mailbox

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if domain is not UNSET:
            field_dict["domain"] = domain
        if mailbox is not UNSET:
            field_dict["mailbox"] = mailbox

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_domain(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        domain = _parse_domain(d.pop("domain", UNSET))

        def _parse_mailbox(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mailbox = _parse_mailbox(d.pop("mailbox", UNSET))

        hosting_email_wblist_request = cls(
            domain=domain,
            mailbox=mailbox,
        )

        return hosting_email_wblist_request
