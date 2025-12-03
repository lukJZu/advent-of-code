from pathlib import Path

SIZE = 12


def process_line(line: str) -> int:
    n_len = len(line)
    
    maxes = []

    start_idx = 0
    for i in range(SIZE):
        # the index of the character in the line where the max value needs to be found
        max_idx = n_len - (SIZE - i) + 1

        substr = line[start_idx:max_idx]
        
        max_val = max(list(substr))

        maxes.append(max_val)

        start_idx = substr.index(max_val) + 1 + start_idx


    return int("".join(maxes))




with open(f"{Path(__file__).resolve().parent}/inputs.txt", "r") as f:
    lines = f.readlines()

total = 0
for r in lines:
    total += process_line(r.replace("\n", ""))
    # break

print("SUM", total)