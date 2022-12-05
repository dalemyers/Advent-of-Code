import os
from typing import List


def read_file_lines(path, strip: bool = True):
    base_path = os.path.dirname(__file__)
    aoc_path = os.path.abspath(os.path.join(base_path, ".."))
    with open(os.path.join(aoc_path, path), encoding="utf-8") as input_file:
        contents = input_file.readlines()

    if strip:
        return [c.strip() for c in contents]
    else:
        return contents


def read_ints_from_file(path: str) -> List[int]:
    base_path = os.path.dirname(__file__)
    aoc_path = os.path.abspath(os.path.join(base_path, ".."))
    with open(os.path.join(aoc_path, path), encoding="utf-8") as f:
        input_data = f.readlines()
    return list(map(int, input_data))


def read_int_comma_separated_from_file(path: str) -> List[int]:
    base_path = os.path.dirname(__file__)
    aoc_path = os.path.abspath(os.path.join(base_path, ".."))
    with open(os.path.join(aoc_path, path), encoding="utf-8") as f:
        input_data = f.read().strip()
    return list(map(int, input_data.split(",")))


def read_int_grid_file(path: str) -> List[List[int]]:
    base_path = os.path.dirname(__file__)
    aoc_path = os.path.abspath(os.path.join(base_path, ".."))
    with open(os.path.join(aoc_path, path), encoding="utf-8") as f:
        input_data = f.readlines()

    output = []

    for line in input_data:
        output_line = []
        for value in line.strip():
            output_line.append(int(value))
        output.append(output_line)

    return output


def read_chunked_ints(path: str) -> List[List[int]]:
    base_path = os.path.dirname(__file__)
    aoc_path = os.path.abspath(os.path.join(base_path, ".."))
    with open(os.path.join(aoc_path, path), encoding="utf-8") as input_file:
        contents = input_file.readlines()

    chunks = []
    chunk = []
    for line in contents:
        if len(line.strip()) == 0:
            chunks.append(chunk)
            chunk = []
            continue

        chunk.append(int(line))

    return chunks
