from __future__ import annotations

import argparse
import os.path
from typing import List

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")


def compute(s: str) -> int:
    try:
        for e, _ in enumerate(s):
            sliceru = s[e : e + 14]
            if len(set(sliceru)) == 14:
                return e + 14
        return 0
    except IndexError:
        return 0


INPUT_S = [
    "mjqjpqmgbljsphdztnvjfqwrcgsmlb",
    "bvwbjplbgvbhsrlpgdmjqwftvncz",
    "nppdvjthqldpwncqszvftbrmjlhg",
    "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",
    "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw",
]
EXPECTED = [
    19,
    23,
    23,
    29,
    26,
]


@pytest.mark.parametrize(
    ("input_s", "expected"),
    ((INPUT_S, EXPECTED),),
)
def test(input_s: List[str], expected: List[int]) -> None:
    for s, e in zip(input_s, expected):
        assert compute(s) == e


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("data_file", nargs="?", default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f, support.timing():  # type: ignore
        print(compute(f.read()))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
