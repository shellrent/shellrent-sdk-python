from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="PurchaseCommentChangeRequest")


@_attrs_define
class PurchaseCommentChangeRequest:
    comment: str
    """ Comment of the user on the purchase, also shown in the description of its invoices """

    def to_dict(self) -> dict[str, Any]:
        comment = self.comment

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "comment": comment,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        comment = d.pop("comment")

        purchase_comment_change_request = cls(
            comment=comment,
        )

        return purchase_comment_change_request
