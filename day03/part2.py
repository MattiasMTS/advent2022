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
    rucksacks = s.strip().split("\n")
    for group in zip(*[rucksacks[i::3] for i in range(3)]):
        common_item = list(
            {item for item in group[0] if item in group[1] and item in group[2]}
        )[0]
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
EXPECTED = 70


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
