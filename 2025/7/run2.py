from pathlib import Path
from pprint import pprint


with open(f"{Path(__file__).resolve().parent}/inputs.txt", "r") as f:
    lines = f.readlines()


"""
(active_col, (path))
eg. (23, (2,1,2,3))
"""

def process_line(line: str, actives: dict[int, int]) -> dict[int, int]:
    
    new_actives: dict[int, int] = {}
    for i, c in enumerate(line):
        if c == "\n":
            break

        if c == "S":
            new_actives[i] = 1
    
        if i not in actives.keys():
            continue
        
        current_col_counts = actives[i]
        if c == "^":
            if i - 1 >= 0:
                new_actives.setdefault(i-1, 0)
                new_actives[i-1] += current_col_counts
                print(f"SPLITTING FROM {i} TO {i-1}, adding {current_col_counts}. Col {i-1} is now {new_actives[i-1]}")
            if i + 1 < len(line):
                new_actives.setdefault(i+1, 0)
                new_actives[i+1] += current_col_counts
                print(f"SPLITTING FROM {i} TO {i+1}, adding {current_col_counts}. Col {i+1} is now {new_actives[i+1]}")

        elif c == ".":
            new_actives.setdefault(i, 0)
            new_actives[i] += current_col_counts
            print(f"PASSING {i}, adding {current_col_counts}. Col {i} is now {new_actives[i]}")

    # pprint(new_actives)
    return new_actives

def main():

    actives = {}
    for i, line in enumerate(lines):
        print(f"PROCESSING line {i} out of {len(lines)}...")
        actives = process_line(line, actives)
        # if i > 8:
        #     break

    total = 0
    for v in actives.values():
        total += v

    print("SUM: ", total)


if __name__ == "__main__":
    main()