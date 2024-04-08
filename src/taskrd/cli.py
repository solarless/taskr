import os
import os.path
import signal
import sys
import subprocess

import click

from .storage import tasks_file


@click.group()
def cli() -> None:
    pass


@cli.command("start")
def start():
    if os.path.exists("taskrd.pid"):
        click.echo("taskr daemon is already started")
        sys.exit(1)

    process = subprocess.Popen(
        ["gunicorn", "--bind", "localhost:5000", "taskrd.api:app"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    if not tasks_file.exists():
        tasks_file.touch()
        tasks_file.write_text("{}")

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


@cli.command("status")
def show_status() -> None:
    started = os.path.exists("taskrd.pid")
    status = click.style("started", fg="green", bold=True) if started else click.style("stopped", fg="red", bold=True)

    click.echo(f"status: {status}")


def main() -> None:
    cli()


if __name__ == "__main__":
    main()
