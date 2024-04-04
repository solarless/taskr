import datetime
import sys

import click
import requests
import tabulate

from .models import Task


uri = "http://localhost:5000/tasks"


@click.group()
def cli() -> None:
    pass


@cli.command("list")
def get_tasks() -> None:
    tasks: dict[str, Task] = requests.post(uri + "/list").json()

    rows = []
    for task in tasks.values():
        date = datetime.datetime.fromisoformat(task["created_at"])
        rows.append((
            task["id"],
            task["title"],
            "yes" if task["done"] else "no",
            date.strftime("%B %-d"),
        ))

    print(tabulate.tabulate(rows, ("ID", "TITLE", "DONE", "CREATED AT"), tablefmt="plain"))


@cli.command("create")
@click.argument("title")
def create_task(title: str) -> None:
    response = requests.post(
        uri + "/create",
        json={"title": title},
        headers={"Content-Type": "application/json"},
    )
    if response.status_code != 201:
        click.secho("Error :(", fg="red", bold=True)
        sys.exit(1)

    click.secho("Success :)", fg="green", bold=True)


def main() -> None:
    cli()


if __name__ == "__main__":
    main()
