import datetime
import json
import pathlib
import random
import typing


tasks_file = pathlib.Path("tasks.json")


class Task(typing.TypedDict):
    id: str
    title: str
    done: bool
    created_at: str


def get_tasks() -> dict[str, Task]:
    with tasks_file.open() as file:
        tasks: dict[str, Task] = json.load(file)

    return tasks


def save_tasks(tasks: dict[str, Task]) -> None:
    with tasks_file.open("w") as file:
        json.dump(tasks, file)


def create_task(title: str) -> str:
    tasks = get_tasks()

    time = datetime.datetime.now().astimezone().isoformat(timespec="seconds")
    id = random.randbytes(6).hex()
    tasks[id] = {
        "id": id,
        "title": title,
        "done": False,
        "created_at": time,
    }

    save_tasks(tasks)
    return id


class TaskNotFoundException(Exception):
    pass


def remove_task(id: str) -> None:
    tasks = get_tasks()

    if tasks.pop(id, None) is None:
        raise TaskNotFoundException()

    save_tasks(tasks)
