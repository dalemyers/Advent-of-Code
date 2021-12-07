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

latest_day = sorted(days)[-1]

latest_day_path = os.path.join(latest_year_path, f"day_{latest_day:02}.py")
latest_input_path = os.path.join(latest_year_path, f"input_{latest_day:02}.txt")

next_day_path = os.path.join(latest_year_path, f"day_{latest_day+1:02}.py")
next_input_path = os.path.join(latest_year_path, f"input_{latest_day+1:02}.txt")

if not os.path.exists(next_day_path):
    shutil.copy(latest_day_path, next_day_path)

if not os.path.exists(next_input_path):
    shutil.copy(latest_input_path, next_input_path)

with open(
    os.path.join(latest_year_path, "__init__.py"), "a", encoding="utf-8"
) as init_file:
    init_file.write(f"from aoc.year_{latest_year} import day_{latest_day+1:02}\n")

with open(
    os.path.join(latest_year_path, f"test_{latest_year}.py"), "a", encoding="utf-8"
) as test_file:
    test_file.write("\n\n")
    test_file.write(f"def test_day_{latest_day+1:02}():\n")
    test_file.write(f'    """Test day {latest_day+1:02}."""\n')
    test_file.write("\n")
    test_file.write(f"    assert day_{latest_day+1:02}.part1() == 0\n")
    test_file.write(f"    assert day_{latest_day+1:02}.part2() == 0\n")
