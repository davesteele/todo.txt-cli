#!/usr/bin/python3

import os
from pathlib import Path
from subprocess import run

cp = run(
    ["todo.txt-cli-helper", "todofile"],
    capture_output=True,
    encoding="utf-8"
)
assert cp.stdout.strip() == "~/.todo/todo.txt"
