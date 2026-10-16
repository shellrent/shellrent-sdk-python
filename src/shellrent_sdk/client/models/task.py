from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.task_status import TaskStatus


T = TypeVar("T", bound="Task")


@_attrs_define
class Task:
    """Operation on a purchase that goes on in the background, with its status and progress (`GET /api/v3/tasks/{task_id}`)"""

    task_id: int
    purchase_id: int
    """ Id of the purchase the task works on (`GET /api/v3/purchases/{purchase_id}`) """
    task_status: TaskStatus
    executed_instructions: int | None
    """ Number of the step reached by the task, out of `total_instructions`: equal to it when the task is done or
    failed """
    total_instructions: int | None
    """ Total number of steps of the task """
    is_started: bool
    """ Whether the execution of the task has started """
    ask_user_error: None | str
    """ Error found in the data provided for the task, null when there is none: the corrected data are sent with
    `POST /api/v3/tasks/{task_id}/data` """
    date_started: datetime.datetime
    """ Date and time the task was created """
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

        ask_user_error: None | str
        ask_user_error = self.ask_user_error

        date_started = self.date_started.isoformat()

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
                "ask_user_error": ask_user_error,
                "date_started": date_started,
            }
        )

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

        def _parse_ask_user_error(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        ask_user_error = _parse_ask_user_error(d.pop("ask_user_error"))

        date_started = datetime.datetime.fromisoformat(d.pop("date_started"))

        task = cls(
            task_id=task_id,
            purchase_id=purchase_id,
            task_status=task_status,
            executed_instructions=executed_instructions,
            total_instructions=total_instructions,
            is_started=is_started,
            ask_user_error=ask_user_error,
            date_started=date_started,
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
