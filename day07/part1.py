from __future__ import annotations

import argparse
import os.path
from pathlib import Path
from typing import Dict

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")
LIMIT = 100_000


def get_size(files: Dict[Path, int], dir: str) -> int:
    rv = 0
    for key, value in files.items():
        if str(key).startswith(dir + "/"):
            rv += value
    return 0 if rv > LIMIT else rv


def compute(s: str) -> int:
    foo = {}
    pwd = Path("/")
    dirs = {pwd}

    for cmd in s.splitlines()[1:]:
        if cmd == "$ cd ..":
            pwd = pwd.parent

        elif cmd.startswith("$ cd"):
            pwd = pwd.joinpath(cmd.split(" ", 2)[-1])
            dirs.add(pwd)

        elif cmd.startswith(("dir", "$ ls")):
            continue

        else:
            content, filename = cmd.split(" ", 1)
            foo[pwd.joinpath(filename)] = int(content)
    size_root = sum(foo.values())
    if size_root > LIMIT:
        size_root = 0
    return size_root + sum(get_size(foo, str(dir)) for dir in dirs)


INPUT_S = """\
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""
EXPECTED = 95437


@pytest.mark.parametrize(
    ("input_s", "expected"),
    ((INPUT_S, EXPECTED),),
)
def test(input_s: str, expected: int) -> None:
    assert compute(input_s) == expected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("data_file", nargs="?", default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f, support.timing():  # type: ignore
        print(compute(f.read()))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
