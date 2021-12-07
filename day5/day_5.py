from collections import defaultdict

data = [
    line.strip().split(' -> ')
    for line in open('day_5').readlines() if line != '\n'
]
data = [
    [
        [int(el) for el in entry[0].split(',')],
        [int(el) for el in entry[1].split(',')],
    ]
    for entry in data
]


result_map = defaultdict(int)


def calculate_line(start: list[int], end: list[int]) -> None:

    # vertical logic
    if start[0] == end[0]:
        range_from = min(start[1], end[1])
        range_to = max(start[1], end[1])
        for i in range(range_from, range_to + 1):
            result_map[(start[0], i)] += 1

    # horizontal logic
    elif start[1] == end[1]:
        range_from = min(start[0], end[0])
        range_to = max(start[0], end[0])
        for i in range(range_from, range_to + 1):
            result_map[(i, start[1])] += 1

    # diagonal logic
    else:
        if start[0] > end[0]:
            start, end = end, start

        range_from = start[0]
        range_to = end[0]

        sign = -1 if (start[1] - end[1]) > 0 else 1 

        for i, x in enumerate(range(range_from, range_to + 1)):
            result_map[(x, start[1] + (sign * i))] += 1


def calculate_map():
    total = 0
    for value in result_map.values():
        if value >= 2:
             total += 1
    return total


if __name__ == '__main__':
    for entry in data:
        calculate_line(entry[0], entry[1])
    total = calculate_map()
    print(total)
