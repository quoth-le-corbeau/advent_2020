from typing import List, Tuple
import time
import pathlib


def get_highest_seat_id(file_path: str) -> int:
    boarding_passes = _get_boarding_passes(file=file_path)
    print(f"{boarding_passes=}")
    seat_ids: List[int] = list()
    for boarding_pass in boarding_passes:
        row_number = _get_row_number(binary_code=boarding_pass[0])
        column_number = _get_column_number(binary_code=boarding_pass[1])
        seat_ids.append(row_number * 8 * column_number)
    return max(seat_ids)


def _get_row_number(binary_code: str) -> int:
    """
    binary search algo with 0 - 127
    0101100
    
    """
    return 1


def _get_column_number(binary_code: str) -> int:
    return 1


def _get_boarding_passes(file: str) -> List[Tuple[str, str]]:
    with open(pathlib.Path(__file__).parent / file, "r") as puzzle_input:
        lines = puzzle_input.read().splitlines()
        boarding_passes: List[Tuple[str, str]] = list()
        for line in lines:
            boarding_passes.append((line[:-3], line[-3:]))
        return boarding_passes


start = time.perf_counter()
print(get_highest_seat_id("eg.txt"))
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")

# start = time.perf_counter()
# print(get_highest_seat_id("input.txt"))
# print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
