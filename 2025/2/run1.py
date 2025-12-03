from pathlib import Path




def is_int_repeated(n: int) -> bool:
    n_str = str(n)

    if len(n_str) % 2:
        return False
    
    mid_idx = int(len(n_str) / 2)
    
    if n_str[0:mid_idx] == n_str[mid_idx:]:
        return True




def find_invalids(line: str) -> int:
    nums = line.split("-")

    start, end = int(nums[0]), int(nums[1])

    total = 0
    for i in range(start, end+1):
        if is_int_repeated(i):
            total += i
        
    
    return total




with open(f"{Path(__file__).resolve().parent}/inputs.txt", "r") as f:
    line = f.read().strip()
    
ranges = line.split(",")

total = 0
for r in ranges:
    total += find_invalids(r)

print("SUM", total)