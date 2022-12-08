"""Day 7"""

import itertools
from typing import List, Optional, Union
from aoc.shared import read_file_lines


class File:
    def __init__(self, name: str, size: int) -> None:
        self.name = name
        self._size = size

    def size(self) -> int:
        return self._size

    def __repr__(self) -> str:
        return f"{self.size} {self.name}"


class Folder:

    name: str
    contents: List[Union["Folder", File]]

    def __init__(self, name: str) -> None:
        self.name = name
        self.contents = []

    def size(self) -> int:
        return sum([c.size() for c in self.contents])

    def get(self, path: str) -> Optional[Union["Folder", File]]:
        if path == "":
            return self

        components = path.split("/")

        if components[0] == "":
            components = components[1:]

        for entry in self.contents:
            if entry.name == components[0]:
                return entry.get("/".join(components[1:]))

        return None

    def get_folders(self) -> List["Folder"]:
        folders = [
            [c] + c.get_folders() for c in self.contents if isinstance(c, Folder)
        ]
        return list(itertools.chain(*folders))

    def __repr__(self) -> str:
        return f"{self.name} - {self.size()}"


def load_fs() -> Folder:
    lines = read_file_lines("year_2022/input_07.txt")
    current_path = ""
    fs = Folder("/")
    current = fs

    while len(lines) > 0:
        line = lines.pop(0)
        if not line.startswith("$ "):
            raise Exception()

        line = line.replace("$ ", "")
        if line.startswith("cd "):
            line = line.replace("cd ", "")
            if line.startswith("/"):
                current_path = line
                current = fs
            else:
                if current_path == "/":
                    current_path = current_path + line
                else:
                    if line == "..":
                        current_path = "/".join(current_path.split("/")[:-1])
                    else:
                        current_path += "/" + line
                current = fs.get(current_path)
            continue

        # ls
        while len(lines) > 0 and not lines[0].startswith("$ "):
            entry = lines.pop(0)
            if entry.startswith("dir "):
                current.contents.append(Folder(entry.replace("dir ", "")))
            else:
                size_str, name = entry.split(" ")
                current.contents.append(File(name, int(size_str)))

    return fs


def part1() -> int:
    """Part 1."""
    return sum([f.size() for f in load_fs().get_folders() if f.size() <= 100_000])


def part2() -> int:
    """Part 2."""
    disk_space = 70_000_000
    required = 30_000_000

    fs = load_fs()
    folders = [fs] + fs.get_folders()

    folders.sort(key=lambda f: f.size())

    needed = required - (disk_space - fs.size())

    for f in folders:
        if f.size() > needed:
            return f.size()

    raise Exception()


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
