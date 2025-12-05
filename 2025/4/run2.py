from pathlib import Path


with open(f"{Path(__file__).resolve().parent}/inputs.txt", "r") as f:
    lines = f.readlines()



def roll_accessible(test_lines: list[str], i: int, j: int) -> bool:

    line = test_lines[i]

    idxes = [
        (i-1, j-1), 
        (i-1, j), 
        (i-1, j+1), 
        (i, j-1), 
        (i, j+1), 
        (i+1, j-1), 
        (i+1, j), 
        (i+1, j+1)
    ]

    adj_count = 0
    for idx in idxes:
        if idx[0] < 0 or idx[0] >= len(test_lines):
            continue
        if idx[1] < 0 or idx[1] >= len(line):
            continue

        # print(idx, len(lines), len(line))
        try:
            val = test_lines[idx[0]][idx[1]]
        except IndexError:
            continue
        if val == "@":
            adj_count += 1

    if adj_count < 4:
        return True
    
    return False




def process_iteration(test_lines: list[str]) -> tuple[list[str], int]:
    
    accessible_count = 0
    new_lines = []
    for i in range(0, len(test_lines)):
        
        new_line = ""
        for j in range(0, len(test_lines[i])):
            if test_lines[i][j] != "@":
                new_line += "."
                continue

            if roll_accessible(test_lines, i, j):
                new_line += "."
                accessible_count += 1
            else:
                new_line += "@"

        new_lines.append(new_line)

        # print(new_line == test_lines[i])
    return new_lines, accessible_count


def main():

    old_lines = lines
    new_lines = []
    accessible_count = 0
    iteration = 0
    while True:
        # print("iteration", iteration)
        new_lines, count = process_iteration(old_lines)
        accessible_count += count

        if new_lines == old_lines:
            break

        iteration += 1
        old_lines = new_lines

    print("SUM", accessible_count)

if __name__ == "__main__":
    main()