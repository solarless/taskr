import typing


class Task(typing.TypedDict):
    id: str
    title: str
    done: bool
    created_at: str
