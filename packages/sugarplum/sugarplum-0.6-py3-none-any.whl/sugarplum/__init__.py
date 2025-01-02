import os
from pathlib import Path


def _input_file_exists(year: int, day: int, part: int, sub_part: str) -> bool:
    return Path(
        os.environ["SUGARPLUM_BASE_PATH"] + f"/{year}/{day:02}/test-{part}{sub_part}.in"
    ).exists()


def _read_file(year: int, day: int, filename: str) -> str:
    with open(os.environ["SUGARPLUM_BASE_PATH"] + f"/{year}/{day:02}/{filename}") as f:
        return f.read()


def get_input(year: int, day: int) -> str:
    return _read_file(year, day, "data.in")


def get_test_input(year: int, day: int, part: int) -> str:
    return _read_file(year, day, f"test-{part}.in")


def get_test_answer(year: int, day: int, part: int) -> int:
    return int(_read_file(year, day, f"test-{part}.out"))


def get_parametrized_test_data(year: int, day: int, part: int) -> list[tuple[str, int]]:
    sub_part: str = "a"
    data: list[tuple[str, int]] = []
    while _input_file_exists(year, day, part, sub_part):
        data.append(
            (
                _read_file(year, day, f"test-{part}{sub_part}.in"),
                int(_read_file(year, day, f"test-{part}{sub_part}.out")),
            )
        )
        sub_part = chr(ord(sub_part) + 1)

    return data
