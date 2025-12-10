import re
from typing import Literal
from pathlib import Path


with open(f"{Path(__file__).resolve().parent}/inputs.txt", "r") as f:
    lines = f.readlines()


def get_max_width(line: str, start_idx: int) -> int:
    for j in range(start_idx, len(line)):
        if line[j] in [" ", "\n"]:
            return j - start_idx

    return -1

def get_ints(str_list: list[str]) -> list[int]:
    width = len(str_list[0])
    
    ints = []
    for j in range(width - 1, -1, -1):
        ints.append(int("".join([str_list[i][j] for i in range(4)])))

    return ints

def process_col(ints: list[int], operation: Literal["+", "*"]) -> int:

    total = ints[0]
    if operation == "*":
        for i in ints[1:]:
            total *= i
    elif operation == "+":
        for i in ints[1:]:
            total += i

    return total

def main():

    total = 0

    max_line_width = max([len(x) for x in lines])

    j = 0
    while j < max_line_width - 1:
        max_col_width = max([get_max_width(lines[i], j) for i in range(4)])

        ints = get_ints([lines[i][j:j+max_col_width] for i in range(4)])

        total += process_col(ints, lines[4][j])
        # print(j, max_col_width, ints)
        j += max_col_width + 1
        # break



    print("SUM: ", total)


if __name__ == "__main__":
    main()