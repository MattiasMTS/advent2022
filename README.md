# 🎄 advent2022 🎄

https://adventofcode.com/2022

AoC 2022, prepare to get pythonized

# 🛠️ To get started 🛠️

Poetic justice - `poetry`. Run:

```shell
poetry shell && poetry install
```

or if you want a lot of damage:

```shell
pip install -r requirements.txt
```

The template is inspired by anthonywritescode's template! Check it out!

Day 00 is the template structure for remaining succeeding days.
Run `cp -r day00 dayNN`, where NN=day, to easily get started with a new day.

We are also utilizing a session cookie for the AoC website to easily fetch
inputs and submit code using the `aoc-` commands from the `./support/` package.

Useful commands (when you are in a dayNN folder):

- `pytest <path-to-file>` - to test the given input/expected.
- `aoc-download-input` - fetch the input for that day into your input.txt file.
- `aoc-submit --part <N>` - combine this with the pipe to echo the answer and submit it!
- `python3 part1 input.txt` - to get the output from your implementation and see how fast it was!
- `python3 part1 input.txt | aoc-submit --part 1` - example submit command.
