# Dumb Task List Application

Just playing around concept of deamons, like `dockerd` (Docker Engine).
Because how fucking cool is that it's just like `engine start` and it serves
in the background!

## Core concepts

Imagine a simple task list project, but instead of traditional web
oriented architecture it relays on a bit lower level.
It's assumed that you run it only on your machine, like Docker Engine
(imagine someone could just connect to your local Docker Engine and remove
some volumes that are used for your application database, haha), as it was
built with self-hostness (does anyone speaks like this?) in mind.
But in theory you can run it everywhere and get access to it from everywhere
as well.

This project is splitted into two parts, the engine and the client.

### The engine

This is the core and it contains all the logic.
Yeah, just a simple CRUD but it is what it is.
It exposes a simple HTTP API (not even RESTful) in order to be able to send
requests like creating and removing tasks. Also it has a simple CLI so you
can run it :)

It stores all data in simple `tasks.json` file :)

It produces logs into `taskrd.log` file on each incoming request, just to
make debugging process easier.

### The client

This is the user interface that you can use to easily send requests to
engine.
Of course, you can send raw requests via `curl` or some other stuff, but are
you kidding me?

By the way you can implement your own client for the engine, like Web or
Terminal UI. I think it's always fun to do some stuff like that and I'd be
glad if someone build an alternative client!

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
  - `start` — obviously starts the engine itself
    (the coolest part of this fun project)
  - `stop` — like `start` but not the same
    (haha it stops the engine!)

`taskr`

  - `list` — prints a pretty table with information about each task
  - `create TITLE` — creates a task with title `TITLE`
  - `complete ID...` — marks all tasks with ids `ID` as completed
  - `remove ID...` — removes all tasks with ids `ID`. You may assume that it's
    gonna be completely removed, but (haha!) it just gets soft deleted (SCAM)

## Contributing

I'd be glad to see someone creating an issue and letting me know about some
problems/possible improvements!

Feel free to create an issue or maybe even a pull request! Let's play with
this project together!

## Some words

Don't take this project as a real world application, and more importantly, don't
expect this to be well written because I made it just for educational purposes
and didn't even think about performance/clean code at all :)

Think that's all, at least for now!
