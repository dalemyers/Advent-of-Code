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


def test_day_08():
    """Test day 08."""

    assert day_08.part1() == 1840
    assert day_08.part2() == 405769


def test_day_09():
    """Test day 09."""

    assert day_09.part1() == 5779
    assert day_09.part2() == 2331


def test_day_10():
    """Test day 10."""

    assert day_10.part1() == 13520
    assert (
        day_10.part2()
        == """
###...##..###..#..#.###..####..##..###..
#..#.#..#.#..#.#..#.#..#.#....#..#.#..#.
#..#.#....#..#.####.###..###..#..#.###..
###..#.##.###..#..#.#..#.#....####.#..#.
#....#..#.#....#..#.#..#.#....#..#.#..#.
#.....###.#....#..#.###..####.#..#.###..
"""
    )


def test_day_11():
    """Test day 11."""

    assert day_11.part1() == 102399
    assert day_11.part2() == 23641658401


def test_day_12():
    """Test day 12."""

    assert day_12.part1() == 484
    assert day_12.part2() == 478


def test_day_13():
    """Test day 13."""

    assert day_13.part1() == 5720
    assert day_13.part2() == 23504


def test_day_14():
    """Test day 14."""

    assert day_14.part1() == 672
    assert day_14.part2() == 26831


def test_day_15():
    """Test day 15."""

    assert day_15.part1() == 0
    assert day_15.part2() == 0
