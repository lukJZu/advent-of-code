import logging
import re
from pathlib import Path

logger = logging.getLogger()
logging.basicConfig(level = logging.WARNING)


with open(f"{Path(__file__).resolve().parent}/inputs.txt", "r") as f:
    lines = f.readlines()


def process_target_str(target: str) -> list[bool]:

    return [False if c == "." else True for c in target]

def main():

    for line in lines:

        target_regex = r"^\[([\.#]+)\] .*$"
        buttons_regex = r"\(([^)]*)\)"
        target_search = re.match(target_regex, line)
        buttons_str = re.findall(buttons_regex, line)

        assert target_search
        assert buttons_str

        target_str = target_search.group(1)
        target = [False if c == "." else True for c in target_str]
        initial = [False for i in range(len(target_str))]
        
        buttons: list[tuple] = [
            tuple([int(y) for y in x.split(",")]) 
            for x in buttons_str
        ]

        
        break


if __name__ == "__main__":
    main()