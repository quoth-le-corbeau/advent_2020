from typing import Tuple, List
from functools import reduce
import time
import pathlib
import re

_TARGET_SUM = 2020


def product_of_target_triple(file_path: str) -> int:
    triple = _get_target_triple(file=file_path)
    return triple[0] * triple[1] * triple[2]


def _get_target_triple(file: str) -> Tuple[int, int, int]:
    with open(pathlib.Path(__file__).parent / file, "r") as puzzle_input:
        lines = puzzle_input.read()
        all_entries = list(map(int, re.findall(r"\d+", lines)))
        return _get_triple_with_target_sum(all_entries=sorted(all_entries))


def _get_triple_with_target_sum(
    all_entries: List[int]) -> Tuple[int, int, int]:
    print(all_entries)
    relevant_entries = list()
    i = 0
    while all_entries[i] + all_entries[-(i+1)] > 2020:
        i += 1
    return (0,0,0)


start = time.perf_counter()
print(product_of_target_triple("eg.txt"))
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")

# start = time.perf_counter()
# print(product_of_target_triple("input.txt"))
# print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
