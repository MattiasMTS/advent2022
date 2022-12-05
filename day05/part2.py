from __future__ import annotations

import argparse
import os.path
from typing import Dict, List

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")


def compute(s: str) -> str:
    stacks, instructions = s.split("\n\n")
    bottom_number_line = stacks.splitlines()[-1].strip()
    groups: Dict[int, List[str]]
    groups = {int(k): [] for k in bottom_number_line if k.strip() != ""}
    for substack in stacks.splitlines()[:-1]:
        for i, c in enumerate(substack[1::4], 1):
            if c != " ":
                groups[i].append(c)
    groups = {k: v[::-1] for k, v in groups.items()}

    for line in instructions.splitlines():
        _, nbr_to_iterate, _, nbr_from, _, nbr_to = line.split(" ")
        nbr_to_iterate, nbr_from, nbr_to = (
            int(nbr_to_iterate),
            int(nbr_from),
            int(nbr_to),
        )
        mv = groups[nbr_from][-nbr_to_iterate:]
        del groups[nbr_from][-nbr_to_iterate:]
        groups[nbr_to].extend(mv)

    return "".join(i[-1] for i in groups.values()).strip()


INPUT_S = r"""\
    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""
EXPECTED = "MCD"


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
