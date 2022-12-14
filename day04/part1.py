from __future__ import annotations

import argparse
import os.path

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")


def compute(s: str) -> int:
    rv = 0
    for pair in [line.split(",") for line in s.strip().split("\n")]:
        left, right = pair[0].split("-"), pair[1].split("-")
        left_range = range(int(left[0]), int(left[1]) + 1)
        right_range = range(int(right[0]), int(right[1]) + 1)
        if all(i in right_range for i in left_range) or all(
            i in left_range for i in right_range
        ):
            rv += 1
    return rv


INPUT_S = """\
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""
EXPECTED = 2


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
