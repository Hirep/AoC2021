data = [
    [
        el.strip().split(' ')
        for el in n.strip().split('|')
    ] for n in open('day_8').readlines()
]


def part1():
    count = 0
    for line in data:
        for digit in line[1]:
            if len(digit) in (2,3,4,7):
                count += 1
    return count


LEN_TO_DIGIT_MAP = {
    2: 1,
    3: 7,
    4: 4,
    7: 8,
}


def six_digit(digit, digit_map):
    try:
        x = digit_map[8] - digit
        if x.issubset(digit_map[1]):
            digit_map[6] = digit
        elif x.issubset(digit_map[4]):
            digit_map[0] = digit
        else:
            digit_map[9] = digit
        return digit_map
    except:
        return digit_map


def five_digit(digit, digit_map):
    try:
        x = digit.union(digit_map[9])
        if x == digit_map[8]:
            digit_map[2] = digit
        else:
            x = digit.union(digit_map[7])
            if x == digit:
                digit_map[3] = digit
            else:
                digit_map[5] = digit
        return digit_map
    except:
        return digit_map


def extract_digits(line):
    digit_map = {}
    for digits in line:
        for digit in digits:
            if match := LEN_TO_DIGIT_MAP.get(len(digit)):
                digit_map[match] = set(digit)

    while len(digit_map.keys()) < 10:
        for digit in line[0]:
            digit = set(digit)
            if len(digit) in (2,3,4,7):
                continue
            if len(digit) == 5:
                digit_map = five_digit(digit, digit_map)
            if len(digit) == 6:
                digit_map = six_digit(digit, digit_map)
    line_total = ''
    for digit in line[1]:
        for key, val in digit_map.items():
            if set(digit) == val:
                line_total += str(key)
                break
    return int(line_total)


def part2():
    total = 0
    for line in data:
        total += extract_digits(line)
    return total


if __name__ == '__main__':
    print(part1())
    print(part2())