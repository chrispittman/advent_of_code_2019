import sys

data = [line.rstrip() for line in sys.stdin.readlines()]
data = [int(line) for line in data]


def calc_fuel(mass):
    return int((mass / 3) - 2)


assert(calc_fuel(12) == 2)
assert(calc_fuel(14) == 2)
assert(calc_fuel(1969) == 654)
assert(calc_fuel(100756) == 33583)

print(sum([calc_fuel(mass) for mass in data]))
