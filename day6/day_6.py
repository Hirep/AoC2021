from typing import Optional

data = [int(n) for n in open('day_6').readline().split(',')]


class School:
    """
    Used for suboptimal part 1 solution
    """
    def __init__(self, initial_habitants: list['Fish']):
        self.habitants = initial_habitants

    def live_day(self):
        new_population = []
        for fish in self.habitants:
            child = fish.live_day()
            if child:
                new_population.append(child)
        self.habitants.extend(new_population)


class Fish:
    def __init__(self, days_to_child=8):
        self.days_to_child = days_to_child

    def live_day(self) -> Optional['Fish']:
        self.days_to_child -= 1
        child = None
        if self.days_to_child < 0:
            self.days_to_child = 6
            child = Fish()
        return child

    def __repr__(self):
        return f'<Fish days_to_child={self.days_to_child}'


fish_map = {}


def live_days(fish: Fish, days) -> int:
    key = (fish.days_to_child, days)
    if result := fish_map.get(key):
        return result
    else:
        population = 0
        for i in range(days):
            child = fish.live_day()
            if child:
                population += 1
                population += live_days(child, days-(i+1))
        fish_map[key] = population
        return population


def part1():
    habitants = [Fish(days) for days in data]
    school = School(habitants)
    for day in range(80):
        school.live_day()
    return len(school.habitants)


def part2():
    habitants = [Fish(days) for days in data]
    new_fish = 0
    for fish in habitants:
        new_fish += live_days(fish, 256)

    population = new_fish + len(habitants)
    return population


if __name__ == '__main__':
    print(part1())
    print(part2())