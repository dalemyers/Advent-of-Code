"""Test 2022."""

from aoc.year_2022 import *


def test_day_01():
    """Test day 01."""

    assert day_01.part1() == 68467
    assert day_01.part2() == 203420


def test_day_02():
    """Test day 02."""

    assert day_02.part1() == 11449
    assert day_02.part2() == 13187


def test_day_03():
    """Test day 03."""

    assert day_03.part1() == 7980
    assert day_03.part2() == 2881


def test_day_04():
    """Test day 04."""

    assert day_04.part1() == 503
    assert day_04.part2() == 827


def test_day_05():
    """Test day 05."""

    assert day_05.part1() == "VWLCWGSDQ"
    assert day_05.part2() == "TCGLQSLPW"


def test_day_06():
    """Test day 06."""

    assert day_06.part1() == 1140
    assert day_06.part2() == 3495


def test_day_07():
    """Test day 07."""

    assert day_07.part1() == 1648397
    assert day_07.part2() == 1815525
