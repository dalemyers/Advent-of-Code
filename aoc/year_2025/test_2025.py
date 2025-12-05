"""Test 2025."""

from aoc.year_2025 import *


def test_day_01():
    """Test day 01."""

    assert day_01.part1() == 995
    assert day_01.part2() == 5847


def test_day_02():
    """Test day 02."""

    assert day_02.part1() == 53420042388
    assert day_02.part2() == 69553832684


def test_day_03():
    """Test day 03."""

    assert day_03.part1() == 16854
    assert day_03.part2() == 167526011932478


def test_day_04():
    """Test day 04."""

    assert day_04.part1() == 1372
    assert day_04.part2() == 7922


def test_day_05():
    """Test day 05."""

    assert day_05.part1() == 811
    assert day_05.part2() == 338189277144473
