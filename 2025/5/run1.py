import re
from pathlib import Path


with open(f"{Path(__file__).resolve().parent}/inputs.txt", "r") as f:
    lines = f.readlines()


def main():
    newline_idx = lines.index("\n")

    ranges_str, ids_str = lines[:newline_idx], lines[newline_idx+1:]

    ranges = []

    for range in ranges_str:
        s = re.match(r"^(\d+)-(\d+)\n$", range)

        ranges.append((int(s.group(1)), int(s.group(2))))

    count = 0
    for i in ids_str:
        il = int(i.replace("\n", ""))
        for range in ranges:
            if il >= range[0] and il <= range[1]:
                count += 1
                break

    print("SUM", count)


if __name__ == "__main__":
    main()