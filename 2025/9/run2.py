import logging
from pathlib import Path
from math import fabs
from shapely.geometry import Point, Polygon
from shapely import prepare

logger = logging.getLogger()
logging.basicConfig(level = logging.INFO)


with open(f"{Path(__file__).resolve().parent}/inputs.txt", "r") as f:
    lines = f.readlines()


def get_area(a: tuple[int, int], b: tuple[int, int]) -> int:

    return int(fabs(b[0] - a[0])+1) * int(fabs(b[1] - a[1])+1)


def main():

    pts = {}

    for i, line in enumerate(lines):
        pts_str = line.split(",")
        pts[i] = tuple([int(x) for x in pts_str])
    

    polygon = Polygon(list(pts.values()))
    prepare(polygon)

    # print(polygon.contains(Point((pts[0][0],pts[0][1]))) or polygon.touches(Point((pts[0][0],pts[0][1]))))
    areas: dict[int, dict[int, int]] = {}

    # calculating areas
    for a, v in pts.items():
        areas.setdefault(a, {})
        for b, x in pts.items():
            if b <= a:
                continue
            
            logger.debug(f"Checking Points {v} and {x}")
            # check whether the other 2 corners are within the polygon
            corner_1 = Point((v[0], x[1]))
            corner_2 = Point((x[0], v[1]))
            small_polygon = Polygon([Point(v), Point(corner_1), Point(x), Point(corner_2)])

            logger.debug(f"{corner_1}, {corner_2}")

            if not small_polygon.within(polygon):
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