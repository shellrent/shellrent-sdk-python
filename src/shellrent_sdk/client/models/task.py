from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.task_status import TaskStatus


T = TypeVar("T", bound="Task")


@_attrs_define
class Task:
    task_id: int
    purchase_id: int
    task_status: TaskStatus
    executed_instructions: int | None
    total_instructions: int | None
    is_started: bool
    date_started: datetime.datetime
    ask_user_error: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        task_id = self.task_id

        purchase_id = self.purchase_id

        task_status = self.task_status.to_dict()

        executed_instructions: int | None
        executed_instructions = self.executed_instructions

        total_instructions: int | None
        total_instructions = self.total_instructions

        is_started = self.is_started

        date_started = self.date_started.isoformat()

        ask_user_error: None | str | Unset
        if isinstance(self.ask_user_error, Unset):
            ask_user_error = UNSET
        else:
            ask_user_error = self.ask_user_error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "task_id": task_id,
                "purchase_id": purchase_id,
                "task_status": task_status,
                "executed_instructions": executed_instructions,
                "total_instructions": total_instructions,
                "is_started": is_started,
                "date_started": date_started,
            }
        )
        if ask_user_error is not UNSET:
            field_dict["ask_user_error"] = ask_user_error

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.task_status import TaskStatus

        d = dict(src_dict)
        task_id = d.pop("task_id")

        purchase_id = d.pop("purchase_id")

        task_status = TaskStatus.from_dict(d.pop("task_status"))

        def _parse_executed_instructions(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        executed_instructions = _parse_executed_instructions(d.pop("executed_instructions"))

        def _parse_total_instructions(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        total_instructions = _parse_total_instructions(d.pop("total_instructions"))

        is_started = d.pop("is_started")

        date_started = datetime.datetime.fromisoformat(d.pop("date_started"))

        def _parse_ask_user_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ask_user_error = _parse_ask_user_error(d.pop("ask_user_error", UNSET))

        task = cls(
            task_id=task_id,
            purchase_id=purchase_id,
            task_status=task_status,
            executed_instructions=executed_instructions,
            total_instructions=total_instructions,
            is_started=is_started,
            date_started=date_started,
            ask_user_error=ask_user_error,
        )

        task.additional_properties = d
        return task

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
