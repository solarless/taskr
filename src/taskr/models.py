import typing


class Task(typing.TypedDict):
    id: str
    title: str
    completed: bool
    created_at: str
