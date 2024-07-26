from typing import Optional, List
import time
import pathlib
import dataclasses

_FIELDS = [
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
    "cid",
]


@dataclasses.dataclass(frozen=True)
class Passport:
    byr: str
    iyr: str
    eyr: str
    hgt: str
    hcl: str
    ecl: str
    pid: str
    cid: Optional[str]


def count_valid_passports(file_path: str) -> int:
    passports = _get_passports(file=file_path)
    return len(passports)


def _get_passports(file: str) -> List[Passport]:
    with open(pathlib.Path(__file__).parent / file, "r") as puzzle_input:
        lines = puzzle_input.read().split("\n\n")
        passports: List[Passport] = list()
        for line in lines:
            try:
                passports.append(_make_passport(fields_string=line))
            except Exception:
                continue
        return passports


def _make_passport(fields_string: str) -> Passport:
    print("new passport:")
    fields = fields_string.split(" ")
    for field in fields:
        print(field)
    print("===========")


start = time.perf_counter()
print(count_valid_passports("eg.txt"))
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")

# start = time.perf_counter()
# print(count_valid_passports("input.txt"))
# print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
