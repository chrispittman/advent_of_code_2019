import sys
import re

data = [line.rstrip() for line in sys.stdin.readlines()]
#data = ["<x=-1, y=0, z=2>","<x=2, y=-10, z=-7>","<x=4, y=-8, z=8>","<x=3, y=5, z=-1>"]

def parse_position(s):
    digits_re = re.compile('-?\d+')
    digits = digits_re.findall(s)
    digits = [int(d) for d in digits]
    return {'x':digits[0], 'y':digits[1], 'z':digits[2], 'v_x':0, 'v_y': 0, 'v_z':0}

moons = list(map(parse_position, data))

def apply_gravity(moons):
    for i in range(len(moons)):
        for j in range(i+1, len(moons)):
            moon1 = moons[i]
            moon2 = moons[j]
            if moon1['x'] > moon2['x']:
                moon1['v_x'] -= 1
                moon2['v_x'] += 1
            if moon1['x'] < moon2['x']:
                moon1['v_x'] += 1
                moon2['v_x'] -= 1
            if moon1['y'] > moon2['y']:
                moon1['v_y'] -= 1
                moon2['v_y'] += 1
            if moon1['y'] < moon2['y']:
                moon1['v_y'] += 1
                moon2['v_y'] -= 1
            if moon1['z'] > moon2['z']:
                moon1['v_z'] -= 1
                moon2['v_z'] += 1
            if moon1['z'] < moon2['z']:
                moon1['v_z'] += 1
                moon2['v_z'] -= 1

def apply_velocity(moons):
    for moon in moons:
        moon['x'] += moon['v_x']
        moon['y'] += moon['v_y']
        moon['z'] += moon['v_z']

def calc_energy(moons):
    total_energy = 0
    for moon in moons:
        e_k = abs(moon['x']) + abs(moon['y']) + abs(moon['z'])
        e_p = abs(moon['v_x']) + abs(moon['v_y']) + abs(moon['v_z'])
        total_energy += (e_k * e_p)
    return total_energy

num_steps = 1000

for i in range(num_steps):
    apply_gravity(moons)
    apply_velocity(moons)

print (calc_energy(moons))