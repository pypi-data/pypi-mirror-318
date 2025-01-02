from pathlib import Path
from typing import Callable

import pytest

from sugarplum import (
    get_input,
    get_parametrized_test_data,
    get_test_answer,
    get_test_input,
)

YEAR: int = 2023
DAY: int = 24


@pytest.fixture(autouse=True)
def base_path(monkeypatch, tmp_path: Path) -> None:
    monkeypatch.setenv("SUGARPLUM_BASE_PATH", str(tmp_path))


@pytest.fixture(autouse=True)
def setup_dirs(tmp_path: Path) -> None:
    (tmp_path / str(YEAR)).mkdir()
    (tmp_path / f"{YEAR}/{DAY}").mkdir()


@pytest.fixture
def create_files(tmp_path: Path) -> Callable:
    def _create_files(data: list[tuple[str, str]]) -> None:
        for entry in data:
            with open(tmp_path / f"{YEAR}/{DAY}/{entry[0]}", "w") as f:
                f.write(entry[1])

    return _create_files


def test_reading_input_data(create_files: Callable) -> None:
    expected: str = "North Pole"
    create_files([("data.in", expected)])

    assert get_input(YEAR, DAY) == expected


def test_day_number_gets_zero_padded(tmp_path: Path) -> None:
    expected: str = "sleigh"
    day: int = 3
    (tmp_path / f"{YEAR}/{day:02}").mkdir()
    (tmp_path / f"{YEAR}/{day:02}/data.in").write_text(expected, encoding="utf-8")

    assert get_input(YEAR, day) == expected


def test_reading_test_input_data(create_files: Callable) -> None:
    expected: str = "Christmas"
    create_files([("test-1.in", expected)])

    assert get_test_input(YEAR, DAY, 1) == expected


def test_reading_test_answer(create_files: Callable) -> None:
    answer: int = 42
    create_files([("test-1.out", str(answer))])

    assert get_test_answer(YEAR, DAY, 1) == answer


def test_getting_parametrized_data(create_files: Callable) -> None:
    input_a: str = "Santa"
    input_b: str = "Claus"
    output_a: int = 4
    output_b: int = 16
    create_files(
        [
            ("test-1a.in", input_a),
            ("test-1a.out", str(output_a)),
            ("test-1b.in", input_b),
            ("test-1b.out", str(output_b)),
        ]
    )

    assert get_parametrized_test_data(YEAR, DAY, 1) == [
        (input_a, output_a),
        (input_b, output_b),
    ]
