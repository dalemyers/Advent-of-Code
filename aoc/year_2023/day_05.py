"""Day 5"""

from aoc.shared import read_chunked

chunks = [chunk.split("\n") for chunk in read_chunked("year_2023/input_05.txt")]

REQUIREMENTS = ["seed", "soil", "fertilizer", "water", "light", "temperature", "humidity", "location"]

Seeds = list[int]
MapRange = list[int]
DataMap = dict[str, list[MapRange]]


def get_data() -> tuple[DataMap, Seeds]:
    maps = {}
    seeds = [int(n) for n in chunks[0][0].split(": ")[-1].split(" ")]
    for chunk in chunks[1:]:
        identifier = chunk[0].replace(" map:", "")
        maps[identifier] = []
        for values in chunk[1:]:
            maps[identifier].append([int(n) for n in values.split(" ")])

    return maps, seeds


def translate(n: int, key: str, maps: dict[str, list[list[int]]]):
    mappings = maps[key]
    for dest_start, source_start, length in mappings:
        if n < source_start or n > source_start + length:
            continue
        delta = dest_start - source_start
        return n + delta

    return n


class Range:
    def __init__(self, start: int, end: int) -> None:
        assert start < end
        assert start >= 0
        self.start = start
        self.end = end

    def has_overlap(self, other: "Range") -> bool:
        if self.end < other.start:
            return False

        # Entirely right
        if self.start > other.end:
            return False

        return True

    def copy(self) -> "Range":
        return Range(self.start, self.end)

    def __repr__(self) -> str:
        return f"Range({format(self.start, '_')}, {format(self.end, '_')}, [{format(self.end - self.start, '_')}])"


def get_overlaps(r1: Range, r2: Range) -> tuple[Range | None, list[Range]]:
    # Entirely left
    if r1.end < r2.start:
        return None, [r1.copy()]

    # Entirely right
    if r1.start > r2.end:
        return None, [r1.copy()]

    # Entirely contained
    if r1.start >= r2.start and r1.end <= r2.end:
        return r1.copy(), []

    # Overlap left
    if r1.start < r2.start and r1.end <= r2.end:
        overlapped = Range(r2.start, r1.end)
        non_overlapped = [Range(r1.start, r2.start - 1)]
        return overlapped, non_overlapped

    # Overlap right
    if r1.start >= r2.start and r1.end > r2.end:
        overlapped = Range(r1.start, r2.end)
        non_overlapped = [Range(r2.end + 1, r1.end)]
        return overlapped, non_overlapped

    # Overlap entirely
    if r1.start < r2.start and r1.end > r2.end:
        overlapped = r1.copy()
        non_overlapped = [Range(r1.start, r2.start - 1), Range(r2.end + 1, r1.end)]
        return overlapped, non_overlapped

    raise ValueError("Unexpected boundaries")


def part1() -> int:
    """Part 1."""
    maps, seeds = get_data()
    destinations = []
    for seed in seeds:
        value = seed
        for m1, m2 in zip(REQUIREMENTS, REQUIREMENTS[1:]):
            value = translate(value, f"{m1}-to-{m2}", maps)
        destinations.append(value)

    return min(destinations)


def part2() -> int:
    """Part 2."""

    maps, ranges = get_data()

    minimums = []
    for seed_start, seed_length in zip(ranges[::2], ranges[1::2]):
        seed_end = seed_start + seed_length
        ranges = [Range(seed_start, seed_end)]

        for translation_map in maps.values():  # In order thanks to Python 3.8
            remaining_ranges = ranges
            translated_ranges = []

            while len(remaining_ranges) > 0:
                seed = remaining_ranges.pop(0)
                any_translations = False

                for trans_dest, trans_source, trans_length in translation_map:
                    pmap_range = Range(trans_source, trans_source + trans_length)

                    if not seed.has_overlap(pmap_range):
                        continue

                    overlapped, non_overlapped = get_overlaps(seed, pmap_range)

                    if not overlapped:
                        continue

                    delta = trans_dest - trans_source
                    translated_ranges.append(Range(max(0, overlapped.start + delta), max(0, overlapped.end + delta)))

                    for n in non_overlapped:
                        remaining_ranges.append(n)

                    any_translations = True

                if not any_translations:
                    translated_ranges.append(seed)

            ranges = translated_ranges

        minimum = min(r.start for r in ranges)

        if minimum == 0:  # No idea why we can skip this
            continue

        minimums.append(minimum)

    return min(minimums)


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
