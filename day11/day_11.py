from collections import defaultdict

data = [list(map(int, list(n.strip()))) for n in open('day_11').readlines()]

MAX_X, MAX_Y = len(data), len(data[0])


def try_increment_value(x, y, flashpoints):
    if x < 0 or y < 0 or x >= MAX_X or y >= MAX_Y:
        return -1
    if flashpoints.get((x, y)):
        return -1
    else:
        data[x][y] += 1
    return data[x][y]


def trigger_flashlight(x, y, flashpoints):
    data[x][y] = 0
    flashpoints[(x,y)] += 1
    # clockwise, starts from up
    directions = [
        (x - 1, y),
        (x - 1, y + 1),
        (x, y + 1),
        (x + 1, y + 1),
        (x + 1, y),
        (x + 1, y - 1),
        (x, y - 1),
        (x - 1, y - 1),
    ]
    for x, y in directions:
        if try_increment_value(x, y, flashpoints) > 9:
            trigger_flashlight(x, y, flashpoints)


def do_step():
    flashpoints = defaultdict(int)
    for x in range(MAX_X):
        for y in range(MAX_Y):
            if flashpoints.get((x, y)):
                continue
            data[x][y] += 1
            if data[x][y] > 9:
                trigger_flashlight(x, y, flashpoints)
    
    return sum(flashpoints.values())



def part1(steps):
    total_flashpoints = 0
    for _ in range(steps):
        total_flashpoints += do_step()

    return total_flashpoints


def part2():
    step = 0
    while True:
        step += 1
        flashpoints = do_step()
        if flashpoints == MAX_Y * MAX_Y:
            return step



if __name__ == '__main__':
    print(part1(steps=100))
    data = [list(map(int, list(n.strip()))) for n in open('day_11').readlines()]
    print(part2())
