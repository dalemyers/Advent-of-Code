"""Test 2021."""

import aoc.year_2021.day_01
import aoc.year_2021.day_02
import aoc.year_2021.day_03


def test_day_01():
    """Test day 01."""

    assert aoc.year_2021.day_01.part1() == 1466
    assert aoc.year_2021.day_01.part2() == 1491


def test_day_02():
    """Test day 02."""

    assert aoc.year_2021.day_02.part1() == 2039912
    assert aoc.year_2021.day_02.part2() == 1942068080


def test_day_03():
    """Test day 03."""

    assert aoc.year_2021.day_03.part1() == 1025636
    assert aoc.year_2021.day_03.part2() == 793873
