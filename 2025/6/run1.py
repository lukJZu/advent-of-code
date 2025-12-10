import re
from typing import Literal
from pathlib import Path


with open(f"{Path(__file__).resolve().parent}/inputs.txt", "r") as f:
    lines = f.readlines()


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

    lines_split = []

    for line in lines:
        lines_split.append(line.split())

    total = 0
    for j in range(0, len(lines_split[0])):
        # print(j)
        # print([lines_split[i][j] for i in range(4)], lines_split[4][j])
        total += process_col(
            [int(lines_split[i][j]) for i in range(4)],
            lines_split[4][j]
        )


    print("SUM: ", total)


if __name__ == "__main__":
    main()