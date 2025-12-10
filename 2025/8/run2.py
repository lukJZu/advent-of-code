import logging
from pathlib import Path
from math import sqrt

logger = logging.getLogger()
logging.basicConfig(level = logging.WARNING)


with open(f"{Path(__file__).resolve().parent}/inputs.txt", "r") as f:
    lines = f.readlines()


def get_distance(a: tuple[int, int, int], b: tuple[int, int, int]) -> float:

    return sqrt(
        (b[0] - a[0])**2 + (b[1] - a[1])**2 +(b[2] - a[2])**2
    )

def join_two_groups(groups: dict[int, int], old_id: int, new_id: int) -> dict[int, int]:

    for k, v in groups.items():
        if v == old_id:
            logger.debug(f"Junction {k} had group {old_id} now has group {new_id}")
            groups[k] = new_id

    return groups

def is_single_circuit(junction_groups: dict[int, int]) -> bool:
    
    groups = set()
    for _, g in junction_groups.items():
        groups.add(g)

        if len(groups) > 1:
            return False

    return True


def main():

    pts = {}

    for i, line in enumerate(lines):
        pts_str = line.split(",")
        pts[i] = tuple([int(x) for x in pts_str])
    
    distances: dict[int, dict[int, float]] = {}

    # calculating distances
    for a, v in pts.items():
        distances.setdefault(a, {})
        for b, x in pts.items():
            if b <= a:
                continue
    
            distances[a][b] = get_distance(v, x)

    # flattening the distances
    # the smaller ID always comes first
    flat_distances: list[tuple[int, int, float]] = []
    for a, v in distances.items():
        for b, x in v.items():
            flat_distances.append(
                (a, b, x)
            )
    # sorting the distances
    flat_distances = sorted(flat_distances, key=lambda x: x[2])

    # joining junction boxes
    joined_count = 0
    # k: v, where k is junction ID and v is junction groups
    # start with each junction in unique group
    junction_groups = {x: x for x in range(len(lines))}
    while True:
        distance = flat_distances[joined_count]
        a, b = distance[0], distance[1]

        logger.info(f"JOINING junctions {a} & {b}")
        logger.debug(f"Junction {a} had group {junction_groups[a]}. Junction {b} had group {junction_groups[b]}")
        # if junction_groups
        # assign the larger junction ID to the smaller group ID
        if junction_groups[a] == junction_groups[b]:
            logger.info(f"Junctions {a} and {b} already has the same group {junction_groups[a]}")
        elif junction_groups[a] == a and junction_groups[b] == b:
            join_two_groups(junction_groups, junction_groups[b], junction_groups[a])
        else:
            if junction_groups[a] < junction_groups[b]:
                join_two_groups(junction_groups, junction_groups[b], junction_groups[a])
            if junction_groups[a] > junction_groups[b]:
                join_two_groups(junction_groups, junction_groups[a], junction_groups[b])

        # logger.debug(f"Junction {a} now has group {junction_groups[a]}. Junction {b} now has group {junction_groups[b]}")
        
        joined_count += 1
        logger.debug("")

        if is_single_circuit(junction_groups):
            break
    

    print("SUM", pts[a][0]*pts[b][0])
    


if __name__ == "__main__":
    main()