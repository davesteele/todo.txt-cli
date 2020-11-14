#!/usr/bin/python3

import os
from pathlib import Path
from subprocess import run

todo_path = Path("~/.todo/todo.txt").expanduser()

if todo_path.exists():
    todo_path.unlink()

# Can I add a tasks using todo.txt-cli?
run(
    "TODO_FILE=%s todo.txt-cli add Foo" % str(todo_path),
    shell=True,
    capture_output=True,
    encoding="utf-8",
)
with open(str(todo_path), "r") as fp:
    todo_txt = fp.read()
assert "Foo" in todo_txt
