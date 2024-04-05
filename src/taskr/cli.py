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
    try:
        tasks: dict[str, Task] = requests.post(uri + "/list").json()
    except requests.ConnectionError:
        click.echo(f"could not connect to taskr daemon", file=sys.stderr)
        sys.exit(1)

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
    try:
        response = requests.post(
            uri + "/create",
            json={"title": title},
        )
    except requests.ConnectionError:
        click.echo(f"could not connect to taskr daemon", file=sys.stderr)
        sys.exit(1)

    if response.status_code != 201:
        click.secho("Error :(", fg="red", bold=True)
        sys.exit(1)

    click.echo(response.content)


@cli.command("remove")
@click.argument("ids", nargs=-1)
def remove_task(ids: list[str]) -> None:
    for id in ids:
        try:
            response = requests.post(uri + f"/remove/{id}")
        except requests.ConnectionError:
            click.echo(f"could not connect to taskr daemon", file=sys.stderr)
            sys.exit(1)

        if response.status_code == 404:
            click.echo(f"could not find task with ID={id}", file=sys.stderr)
            sys.exit(1)

        click.echo(f"Deleted: {id}")


def main() -> None:
    cli()


if __name__ == "__main__":
    main()
