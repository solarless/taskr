import logging

import flask

from .storage import create_task
from .storage import get_tasks
from .storage import remove_task
from .storage import TaskNotFoundException


app = flask.Flask(__file__)

logging.basicConfig(filename="taskrd.log", filemode="a", level=logging.INFO)


@app.post("/tasks/list")
def handle_list_tasks() -> str:
    logging.info(f"requested: /tasks/list")
    return flask.jsonify(get_tasks())


@app.post("/tasks/create")
def handle_create_task() -> str:
    data = flask.request.get_json()
    logging.info(f"requested: /tasks/create: payload: {data}")

    title = data.get("title")
    if title is None:
        return flask.make_response("", 400)

    id = create_task(title)

    return flask.make_response(id, 201)


@app.post("/tasks/remove/<id>")
def handle_remove_task(id: str) -> str:
    logging.info(f"requested: /tasks/remove/{id}")
    try:
        remove_task(id)
    except TaskNotFoundException:
        logging.error(f"requested: /tasks/remove/{id}: task with ID={id} not found")
        return flask.make_response("", 404)
    return flask.make_response("", 204)