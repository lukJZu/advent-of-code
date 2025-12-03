from pathlib import Path




def is_int_repeated(n: int) -> bool:
    n_str = str(n)

    n_len = len(n_str)
    for j in range(1, int(n_len/2)+1):
        if n_len % j:
            continue
    
        # spliting string into equal chunks
        split_idx = int(n_len / j)

        chunks = [n_str[(i*j):((i+1)*j)] for i in range(0, split_idx)]

        if len(set(chunks)) == 1:
            return True
    
    return False




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