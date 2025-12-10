from pathlib import Path


with open(f"{Path(__file__).resolve().parent}/inputs.txt", "r") as f:
    lines = f.readlines()


def process_line(line: str, active_cols: set[int]) -> tuple[set[int], int]:
    split_count = 0
    new_active: set[int] = set()
    for i, c in enumerate(line):
        if c == "\n":
            break

        if c == "S":
            new_active.add(i)
        
        if c == "^" and i in active_cols:
            if i + 1 < len(line) and i + 1 not in active_cols:
                new_active.add(i+1)
            if i - 1 >= 0  and i - 1 not in active_cols:
                new_active.add(i-1)

            split_count += 1
        if c == "." and i in active_cols:
            new_active.add(i)

    # print(new_active)
    return new_active, split_count

def main():

    total = 0

    active = set()
    for line in lines:
        active, count = process_line(line, active)
        total += count

    print("SUM: ", total)


if __name__ == "__main__":
    main()