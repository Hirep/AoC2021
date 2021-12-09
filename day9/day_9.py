from collections import defaultdict

data = [n.strip() for n in open('day_9').readlines()]

MAX_X, MAX_Y = len(data), len(data[0])

PATH_MAP = {}
RISK_POINTS_MAP = {}


def try_get_height(x, y):
    if x < 0 or y < 0 or x >= MAX_X or y >= MAX_Y:
        return None
    return int(data[x][y])


def get_height_for_point(point):
    x, y = point
    if bottom := PATH_MAP.get((x, y)):
        return bottom
    current_height = try_get_height(x, y)
    moves = {
        try_get_height(x-1, y): (x-1, y),
        try_get_height(x, y+1): (x, y+1),
        try_get_height(x+1, y): (x+1, y),
        try_get_height(x, y-1): (x, y-1),
    }
    min_height_value = min([key for key in moves.keys() if key is not None])
    min_height_coordinates = moves[min_height_value]

    if (
        (min_height_value > current_height) or
        (min_height_value == current_height)
    ):
        risk_level = int(data[x][y])
        RISK_POINTS_MAP[(x, y)] = risk_level
        PATH_MAP[(x, y)] = (x, y)
        return (x, y)

    if is_bottom := get_height_for_point(min_height_coordinates):
        PATH_MAP[(x, y)] = is_bottom
        return is_bottom


def build_low_point_map():
    for x in range(MAX_X):
        for y in range(MAX_Y):
            if int(data[x][y]) == 9:
                continue
            get_height_for_point((x, y))


def part1():
    build_low_point_map()
    risk_level = sum([val + 1 for val in RISK_POINTS_MAP.values()])
    return risk_level


def part2():
    build_low_point_map()
    x = defaultdict(int)
    for v in PATH_MAP.values():
        x[v] += 1
    product = 1
    for p in sorted(x.values())[-3:]:
        product = p * product
    return product


if __name__ == '__main__':
    print(part1())
    print(part2())