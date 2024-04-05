import os
import os.path
import signal
import sys
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
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    if os.path.exists("taskrd.pid"):
        click.echo("taskr daemon is already started")
        sys.exit(1)

    with open("taskrd.pid", "w") as file:
        file.write(str(process.pid))


@cli.command("stop")
def stop():
    try:
        with open("taskrd.pid") as file:
            pid = int(file.read())
    except FileNotFoundError:
        click.echo("taskr daemon is not started", file=sys.stderr)
        sys.exit(1)

    os.kill(pid, signal.SIGTERM)
    os.remove("taskrd.pid")


def main() -> None:
    cli()


if __name__ == "__main__":
    main()
