import time
import pathlib

_SHINY_GOLD = "shiny gold bag"


def get_number_of_shiny_gold_bag_holders(file_path: str) -> int:
    rules = _get_bag_holding_rules(file=file_path)
    print(f"{rules=}")
    count = 0
    bags_containing_gold = list()
    for color, contains in rules.items():
        if any(_SHINY_GOLD in contents for contents in contains):
            bags_containing_gold.append(color)
            count += 1
    print(f"{bags_containing_gold=}")
    visited = list()
    for bag in bags_containing_gold:
        for color, contains in rules.items():
            if any(bag in contents for contents in contains) and color not in visited:
                count += 1
                visited.append(color)
    return count


def _get_bag_holding_rules(file: str):
    with open(pathlib.Path(__file__).parent / file, "r") as puzzle_input:
        lines = puzzle_input.read().splitlines()
        rules_by_bag = dict()
        for line in lines:
            line = (
                line.replace(" contain", ",")
                .replace(".", "")
                .replace("bags", "bag")
                .replace(", ", ",")
            )
            split_line = line.split(",")
            rules_by_bag[split_line[0]] = split_line[1:]
        return rules_by_bag


start = time.perf_counter()
print(get_number_of_shiny_gold_bag_holders("eg.txt"))
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")

start = time.perf_counter()
print(get_number_of_shiny_gold_bag_holders("input.txt"))
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
