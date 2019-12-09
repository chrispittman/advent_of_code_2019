import sys

data = [line.rstrip() for line in sys.stdin.readlines()]

#data = ["COM)B","B)C","C)D","D)E","E)F","B)G","G)H","D)I","E)J","J)K","K)L"]

def calc_orbits(data, level, parent):
    children = [el for el in data if el.startswith(parent+')')]
    children = list(map(lambda el: el.split(')')[1], children))
    sum = level
    for child in children:
        sum += calc_orbits(data, level+1, child)
    return sum

print(calc_orbits(data, 0, 'COM'))