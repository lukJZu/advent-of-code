from pathlib import Path


with open(f"{Path(__file__).resolve().parent}/inputs.txt", "r") as f:
    lines = f.readlines()







def main():
    
    accessible = 0
    for i in range(0, len(lines)):
        
        line = lines[i]
        for j in range(0, len(lines[i])):
            if line[j] != "@" or line[j] == "\n":
                continue

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
                if idx[0] < 0 or idx[0] >= len(lines):
                    continue
                if idx[1] < 0 or idx[1] >= len(line):
                    continue
                
                try:
                    val = lines[idx[0]][idx[1]]
                except IndexError:
                    continue
                if val == "@":
                    adj_count += 1

            if adj_count < 4:
                accessible += 1


    print("SUM", accessible)


if __name__ == "__main__":
    main()