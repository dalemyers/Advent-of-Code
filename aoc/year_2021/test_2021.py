"""Test 2021."""

from aoc.year_2021 import *


def test_day_01():
    """Test day 01."""

    assert day_01.part1() == 1466
    assert day_01.part2() == 1491


def test_day_02():
    """Test day 02."""

    assert day_02.part1() == 2039912
    assert day_02.part2() == 1942068080


def test_day_03():
    """Test day 03."""

    assert day_03.part1() == 1025636
    assert day_03.part2() == 793873


def test_day_04():
    """Test day 04."""

    assert day_04.part1() == 22680
    assert day_04.part2() == 16168


def test_day_05():
    """Test day 05."""

    assert day_05.part1() == 5169
    assert day_05.part2() == 22083


def test_day_06():
    """Test day 06."""

    assert day_06.part1() == 352872
    assert day_06.part2() == 1604361182149


def test_day_07():
    """Test day 07."""

    assert day_07.part1() == 336120
    assert day_07.part2() == 96864235


def test_day_08():
    """Test day 08."""

    assert day_08.part1() == 473
    assert day_08.part2() == 1097568


def test_day_09():
    """Test day 09."""

    assert day_09.part1() == 475
    assert day_09.part2() == 1092012


def test_day_10():
    """Test day 10."""

    assert day_10.part1() == 290691
    assert day_10.part2() == 2768166558


def test_day_11():
    """Test day 11."""

    assert day_11.part1() == 1571
    assert day_11.part2() == 387


def test_day_12():
    """Test day 12."""

    assert day_12.part1() == 4167
    assert day_12.part2() == 98441


def test_day_13():
    """Test day 13."""

    assert day_13.part1() == 689
    assert ["".join(row) for row in day_13.part2()] == [
        "###..#....###...##....##..##..#....#..#.",
        "#..#.#....#..#.#..#....#.#..#.#....#..#.",
        "#..#.#....###..#.......#.#....#....#..#.",
        "###..#....#..#.#.......#.#.##.#....#..#.",
        "#.#..#....#..#.#..#.#..#.#..#.#....#..#.",
        "#..#.####.###...##...##...###.####..##..",
    ]


def test_day_14():
    """Test day 14."""

    assert day_14.part1() == 2874
    assert day_14.part2() == 5208377027195


def test_day_15():
    """Test day 15."""

    assert day_15.part1() == 523
    assert day_15.part2() == 2876


def test_day_16():
    """Test day 16."""

    assert day_16.part1() == 847
    assert day_16.part2() == 333794664059
