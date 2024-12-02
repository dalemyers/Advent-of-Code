import os
import shutil

root_path = os.path.dirname(__file__)

module_path = os.path.join(root_path, "aoc")

years = []

for folder in os.listdir(module_path):
    if not folder.startswith("year_"):
        continue

    years.append(int(folder[len("year_") :]))

latest_year = sorted(years)[-1]

latest_year_path = os.path.join(module_path, f"year_{latest_year}")

days = []

for filename in os.listdir(latest_year_path):
    if not filename.startswith("day_"):
        continue

    filename = filename.replace(".py", "")

    days.append(int(filename[len("day_") :], 10))

days.append(0)

latest_day = sorted(days)[-1]
current_day = latest_day + 1

latest_day_path = os.path.join(latest_year_path, f"day_{latest_day:02}.py")
latest_input_path = os.path.join(latest_year_path, f"input_{latest_day:02}.txt")

next_day_path = os.path.join(latest_year_path, f"day_{current_day:02}.py")
next_input_path = os.path.join(latest_year_path, f"input_{current_day:02}.txt")

if not os.path.exists(next_day_path):
    with open(next_day_path, "w", encoding="utf-8") as f:
        f.write(
            f"""\"""Day {current_day}\"""

from aoc.shared import read_file_lines

lines = read_file_lines("year_{latest_year}/input_{current_day:02}.txt")


def part1() -> int:
    \"""Part 1.\"""

    return 0


def part2() -> int:
    \"""Part 2.\"""

    return 0


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
"""
        )

if not os.path.exists(next_input_path):
    with open(next_input_path, "w", encoding="utf-8") as f:
        f.write("")

init_path = os.path.join(latest_year_path, "__init__.py")

if not os.path.exists(init_path):
    with open(init_path, "w", encoding="utf-8") as init_file:
        init_file.write(f'"""{latest_year}"""\n\n')

with open(init_path, "a", encoding="utf-8") as init_file:
    init_file.write(f"from aoc.year_{latest_year} import day_{current_day:02}\n")

from aoc.year_2023 import *


test_path = os.path.join(latest_year_path, f"test_{latest_year}.py")

if not os.path.exists(test_path):
    with open(test_path, "w", encoding="utf-8") as test_file:
        test_file.write(f'"""Test {latest_year}."""\n')
        test_file.write("\n")
        test_file.write(f"from aoc.year_{latest_year} import *")

with open(test_path, "a", encoding="utf-8") as test_file:
    test_file.write("\n\n")
    test_file.write(f"def test_day_{current_day:02}():\n")
    test_file.write(f'    """Test day {current_day:02}."""\n')
    test_file.write("\n")
    test_file.write(f"    assert day_{current_day:02}.part1() == 0\n")
    test_file.write(f"    assert day_{current_day:02}.part2() == 0\n")
