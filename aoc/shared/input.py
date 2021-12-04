import os
from typing import List


def read_file_lines(path):
    base_path = os.path.dirname(__file__)
    aoc_path = os.path.abspath(os.path.join(base_path, ".."))
    with open(os.path.join(aoc_path, path), encoding="utf-8") as input_file:
        contents = input_file.readlines()
    return [c.strip() for c in contents]


def read_ints_from_file(path: str) -> List[int]:
    base_path = os.path.dirname(__file__)
    aoc_path = os.path.abspath(os.path.join(base_path, ".."))
    with open(os.path.join(aoc_path, path), encoding="utf-8") as f:
        input_data = f.readlines()
    return list(map(int, input_data))
