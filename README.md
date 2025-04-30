# Dumb Task List Application

Just playing around concept of deamons, like `dockerd` (Docker Engine).
Because how fucking cool is that it's just like `engine start` and it serves
in the background!

## Core concepts

Imagine a simple task list project, but instead of traditional web
oriented architecture it relays on a bit lower level.
It's assumed that you run it only on your local machine rather than public
server, like Docker Engine (imagine someone could just connect to your local
Docker Engine). But in theory you can run it everywhere and get access to it
from everywhere as well.

This project is splitted into two parts, the engine and the client.

### The engine

This is the core and it contains all the CRUD logic. It exposes a simple HTTP
API (not even RESTful). Also it has a simple CLI so you can run it.

It stores all data in simple `tasks.json` file.

And it produces logs into `taskrd.log` file on each incoming request, just to
make debugging process easier.

### The client

This is the CLI frontend for the engine. You can send requests to the engine by
yourself via curl instead :)

## Installing

```shell
# create and activate a virtual environment
python3 -m venv .venv
. .venv/bin/activate

# install this project as a package and there you go!
pip install -e .
```

## Command-Line Interface

The package provides two executables, `taskrd` (engine) and `taskr` (client)

`taskrd`

  - `status` — show whether engine is running
  - `start` — starts the engine
  - `stop` — stops the engine

`taskr`

  - `list` — prints a pretty table with information about each task
  - `create TITLE` — creates a task with title `TITLE`
  - `complete ID...` — marks all tasks with ids `ID` as completed
  - `remove ID...` — removes all tasks with ids `ID`
