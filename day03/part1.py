from __future__ import annotations

import argparse
import os.path
import string

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")
PRIORITY = {
    **{lower: points for points, lower in enumerate(string.ascii_lowercase, 1)},
    **{upper: points for points, upper in enumerate(string.ascii_uppercase, 27)},
}


def compute(s: str) -> int:
    rv = 0
    for rucksack in s.strip().split("\n"):
        comp1 = rucksack[: int(len(rucksack) / 2)]
        comp2 = rucksack[int(len(rucksack) / 2) :]
        common_item = list({item for item in comp1 if item in comp2})[0]
        rv += PRIORITY[common_item]

    return rv


INPUT_S = """\
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""
EXPECTED = 157


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
