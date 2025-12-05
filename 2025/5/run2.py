import re
from pathlib import Path


with open(f"{Path(__file__).resolve().parent}/inputs.txt", "r") as f:
    lines = f.readlines()


def combine_ranges(ranges: list[tuple[int, int]]) -> list[tuple[int,int]]:

    skip_idxes = []
    replace_with_ranges = []

    if len(ranges) == 1:
        return ranges

    for i, r in enumerate(ranges):
        if i in skip_idxes:
            continue

        new_lower, new_upper = r
        for j, s in enumerate(ranges):
            if j <= i:
                continue

            # skip non-overlapping 
            if new_upper < s[0] or new_lower > s[1]:
                continue
            
            if new_lower > s[0]:
                new_lower = s[0]

            if new_upper < s[1]:
                new_upper = s[1]

            skip_idxes.append(j)
    
        replace_with_ranges.append((new_lower, new_upper))
    
    return replace_with_ranges
        


def main():
    newline_idx = lines.index("\n")

    ranges_str = lines[:newline_idx]

    ranges: list[tuple[int, int]] = []

    for r in ranges_str:
        s = re.match(r"^(\d+)-(\d+)\n$", r)

        ranges.append((int(s.group(1)), int(s.group(2))))

    count = 0
    ranges.sort(key=lambda x: x[0])
    combined = sorted(combine_ranges(ranges), key=lambda x: x[0])
    count = sum([(x[1] - x[0] + 1) for x in combined])

    print("SUM", count)


if __name__ == "__main__":
    main()