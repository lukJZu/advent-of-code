from pathlib import Path



def process_line(line: str) -> int:
    n_len = len(line)
    
    max_jolt = 0
    for i in range(0, n_len-1):
        i_char = line[i]
        if int(f"{i_char}0") < max_jolt:
            continue
        for j in range(i+1, n_len):
            j_char = line[j]
            jolt = int(f"{i_char}{j_char}")
            max_jolt = max(jolt, max_jolt)

    return max_jolt




with open(f"{Path(__file__).resolve().parent}/inputs.txt", "r") as f:
    lines = f.readlines()

total = 0
for r in lines:
    total += process_line(r)

print("SUM", total)