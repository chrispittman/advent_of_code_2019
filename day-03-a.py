import sys

data = [line.rstrip() for line in sys.stdin.readlines()]
#data = ["R8,U5,L5,D3", "U7,R6,D4,L4"]
#data = ["R75,D30,R83,U83,L12,D49,R71,U7,L72", "U62,R66,U55,R34,D71,R55,D58,R83"]
#data = ["R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51", "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"]


def parse_path(paths):
    cur_x, cur_y = 0, 0
    locns = set()
    for path in paths:
        direction = path[0]
        distance = int(path[1:])
        for i in range(distance):
            if direction == 'R':
                cur_x += 1
            if direction == 'L':
                cur_x -= 1
            if direction == 'U':
                cur_y += 1
            if direction == 'D':
                cur_y -= 1
            locns.add((cur_x, cur_y))
    return locns


path1 = parse_path(data[0].split(','))
path2 = parse_path(data[1].split(','))
shared = path1 & path2
distances = list(map(lambda d: abs(d[0])+abs(d[1]), shared))
print(min(distances))