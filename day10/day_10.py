data = [n.strip() for n in open('day_10').readlines()]


CLOSER_MAP = {
    ')': ('(', 3),
    ']': ('[', 57),
    '}': ('{', 1197),
    '>': ('<', 25137),
}
OPENER_MAP = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4,
}


def calculate_incomplete_score(stack):
    inverted_stack_points = [OPENER_MAP[symbol] for symbol in reversed(stack)]
    score = 0
    for point in inverted_stack_points:
        score = score * 5 + point 
    return score


def check_syntax():
    error_count = 0
    incomplete_scores = []
    for line in data:
        stack = []
        for symbol in line:
            if closer := CLOSER_MAP.get(symbol):
                if len(stack) and stack[-1] != closer[0]:
                    error_count += closer[1]
                    stack = []
                    break
                elif not stack:
                    break
                else:
                    stack.pop()
            else:
                stack.append(symbol)
        if stack:
            incomplete_scores.append(calculate_incomplete_score(stack))
    middle_score = sorted(incomplete_scores)[round(len(incomplete_scores)/2)]
    return error_count, middle_score


def part2():
    pass


if __name__ == '__main__':
    part1, part2 = check_syntax()
    print(part1)
    print(part2)