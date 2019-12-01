import sys

data = [line.rstrip() for line in sys.stdin.readlines()]
data = [int(line) for line in data]


def calc_fuel(mass):
    fuel = 0
    while True:
        new_fuel = int((mass / 3) - 2)
        if new_fuel <= 0:
            break
        fuel += new_fuel
        mass = new_fuel
    return fuel


assert (calc_fuel(12) == 2)
assert (calc_fuel(14) == 2)
assert (calc_fuel(1969) == 966)
assert (calc_fuel(100756) == 50346)

print(sum([calc_fuel(mass) for mass in data]))
