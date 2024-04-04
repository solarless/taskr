import os
import signal
import subprocess

import click

from .api import app


@click.group()
def cli() -> None:
    pass


@cli.command("start")
def start():
    process = subprocess.Popen(
        ["gunicorn", "--bind", "localhost:5000", "taskrd.api:app"],
        start_new_session=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    with open("taskrd.pid", "w") as file:
        file.write(str(process.pid))


@cli.command("stop")
def stop():
    with open("taskrd.pid") as file:
        pid = int(file.read())

    os.kill(pid, signal.SIGTERM)
    os.remove("taskrd.pid")


def main() -> None:
    cli()


if __name__ == "__main__":
    main()
