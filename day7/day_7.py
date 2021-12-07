crab_positions = [int(n) for n in open('day_7').readline().split(',')]


def median(numbers):
    n = len(numbers)
    if n % 2 == 0:
        return int((numbers[int(n/2)-1] + numbers[int(n/2)]) / 2)
    else:
        return numbers[int((n-1)/2)]


def get_fuel_consumption(meeting_point):
    fuel_consumptions = [
        abs(position - meeting_point) for position in crab_positions
    ]
    total_fuel = sum(fuel_consumptions)
    return total_fuel


def part1():
    crab_positions.sort()
    meeting_point = median(crab_positions)
    return get_fuel_consumption(meeting_point)


def get_crab_engineering_fuel_consumption(meeting_point):
    fuel_consumptions = [
        sum(range(abs(position - meeting_point)+1))
        for position in crab_positions
    ]
    total_fuel = sum(fuel_consumptions)
    return total_fuel


def part2():
    meeting_point = round(sum(crab_positions)/len(crab_positions))
    # don't ask about -1, its crab engineering
    return get_crab_engineering_fuel_consumption(meeting_point - 1)


if __name__ == '__main__':
    print(part1())
    print(part2())