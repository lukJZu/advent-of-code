from pathlib import Path


def move(start: int, instruction: str) -> tuple[int, int]:

    steps = int(instruction[1:])
    zero_count = 0

    zero_count += steps // 100

    steps_abbr = steps % 100

    if instruction[0] == "L":
        end = start - steps_abbr
        if end < 0 and start == 0:
            end = 100 + end
        elif end < 0 and start != 0:
            zero_count += 1
            end = 100 + end
        elif end == 0:
            zero_count += 1
    else:
        end = start + steps_abbr
        if end > 99:
            zero_count += 1
            end -= 100

    return end, zero_count



with open(f"{Path(__file__).resolve().parent}/inputs.txt", "r") as f:
    lines = f.readlines()
    
pos = 50
zero_counter = 0

for line in lines:
    new, zero = move(pos, line)
    zero_counter += zero

    pos = new
    
print("PWD", zero_counter)
