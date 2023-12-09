"""Test 2023."""

from aoc.year_2023 import *


def test_day_01():
    """Test day 01."""

    assert day_01.part1() == 56506
    assert day_01.part2() == 56017


def test_day_02():
    """Test day 02."""

    assert day_02.part1() == 2727
    assert day_02.part2() == 56580


def test_day_03():
    """Test day 03."""

    assert day_03.part1() == 557705
    assert day_03.part2() == 84266818


def test_day_04():
    """Test day 04."""

    assert day_04.part1() == 26914
    assert day_04.part2() == 13080971


def test_day_05():
    """Test day 05."""

    assert day_05.part1() == 278755257
    assert day_05.part2() == 26829166


def test_day_06():
    """Test day 06."""

    assert day_06.part1() == 1155175
    assert day_06.part2() == 35961505


def test_day_07():
    """Test day 07."""

    assert day_07.part1() == 19199
    assert day_07.part2() == 13_663_968_099_527


def test_day_08():
    """Test day 08."""

    assert day_08.part1() == 0
    assert day_08.part2() == 0
