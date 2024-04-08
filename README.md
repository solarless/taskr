# Dumb Task List Application

Just playing aroung concept of deamons, like dockerd (Docker Engine).
Because fucking cool is that it is just like `engine start` and it serves
in the background!

## How to run

```shell
# create and activate a virtual environment
python3 -m venv .venv
. .venv/bin/activate

# install this project and there you go!
pip install -e .
```

## Command-Line Interface

Package includes to executables: `taskrd` (engine) and `taskr` (client)

If you are too lazy to just type `taskr/taskrd --help`, next section is
for you!

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

## Some words

That's all for now :)
