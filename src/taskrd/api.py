import logging

import flask

from .storage import complete_task
from .storage import create_task
from .storage import get_tasks
from .storage import remove_task
from .storage import Task
from .storage import TaskNotFoundException


app = flask.Flask(__file__)

logging.basicConfig(filename="taskrd.log", filemode="a", level=logging.INFO)


@app.post("/tasks/list")
def handle_list_tasks() -> str:
    logging.info(f"requested: /tasks/list")
    tasks = filter_removed_tasks(get_tasks())
    return flask.jsonify(tasks)


@app.post("/tasks/create")
def handle_create_task() -> str:
    data = flask.request.get_json()
    logging.info(f"requested: /tasks/create: payload: {data}")

    title = data.get("title")
    if title is None:
        return flask.make_response("", 400)

    id = create_task(title)

    return flask.make_response(id, 201)


@app.post("/tasks/<id>/remove")
def handle_remove_task(id: str) -> str:
    logging.info(f"requested: /tasks/{id}/remove")
    try:
        remove_task(id)
    except TaskNotFoundException:
        logging.error(f"requested: /tasks/{id}/remove: task with ID={id} not found")
        return flask.make_response("", 404)
    return flask.make_response("", 204)


@app.post("/tasks/<id>/complete")
def handle_complete_task(id: str) -> None:
    logging.info(f"requested: /tasks/{id}/complete")
    try:
        complete_task(id)
    except TaskNotFoundException:
        logging.error(f"requested: /tasks/{id}/complete: task with ID={id} not found")
        return flask.make_response("", 404)
    return flask.make_response("", 200)


def filter_removed_tasks(tasks: dict[str, Task]) -> dict[str, Task]:
    return {
        id: task
        for id, task in tasks.items()
        if task["removed_at"] is None
    }
