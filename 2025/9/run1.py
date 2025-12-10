import logging
from pathlib import Path
from math import fabs

logger = logging.getLogger()
logging.basicConfig(level = logging.WARNING)


with open(f"{Path(__file__).resolve().parent}/inputs.txt", "r") as f:
    lines = f.readlines()


def get_area(a: tuple[int, int], b: tuple[int, int]) -> int:

    return int(fabs(b[0] - a[0])+1) * int(fabs(b[1] - a[1])+1)


def main():

    pts = {}

    for i, line in enumerate(lines):
        pts_str = line.split(",")
        pts[i] = tuple([int(x) for x in pts_str])
    
    areas: dict[int, dict[int, int]] = {}

    # calculating distances
    for a, v in pts.items():
        areas.setdefault(a, {})
        for b, x in pts.items():
            if b <= a:
                continue
    
            areas[a][b] = get_area(v, x)

    # print(areas[0])
    # flattening the distances
    # the smaller ID always comes first
    flat_areas: list[int] = []
    for a, v in areas.items():
        flat_areas.extend([w for w in v.values()])

    print("Largest Area: ", max(flat_areas))


if __name__ == "__main__":
    main()