from __future__ import annotations

import argparse
import os.path

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")
MAPPERU = {
    "A": "rock",
    "B": "paper",
    "C": "scissor",
}
POINTS = {
    "rock": 1,
    "paper": 2,
    "scissor": 3,
}
WIN = {
    "rock": "scissor",
    "paper": "rock",
    "scissor": "paper",
}
LOSE = {v: k for k, v in WIN.items()}


def compute(s: str) -> int:
    rv = 0
    for row in (row.split(" ") for row in s.strip().split("\n")):
        opponent = MAPPERU[row[0]]
        mine = row[1]

        if mine == "Y":
            mine = opponent
            rv += 3
        elif mine == "X":
            mine = WIN[opponent]
        else:
            mine = LOSE[opponent]
            rv += 6
        rv += POINTS[mine]
    return rv


INPUT_S = """\
A Y
B X
C Z
"""
EXPECTED = 12


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
