python -m black -l 100 aoc
python -m pylint --rcfile=pylintrc aoc
python -m mypy --ignore-missing-imports aoc
