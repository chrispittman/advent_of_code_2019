import sys

data = [line.rstrip() for line in sys.stdin.readlines()]
#data = ["R8,U5,L5,D3", "U7,R6,D4,L4"]
#data = ["R75,D30,R83,U83,L12,D49,R71,U7,L72", "U62,R66,U55,R34,D71,R55,D58,R83"]
#data = ["R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51", "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"]


def parse_path(paths):
    cur_x, cur_y, time = 0, 0, 0
    locns = []
    for path in paths:
        direction = path[0]
        distance = int(path[1:])
        for i in range(distance):
            time += 1
            if direction == 'R':
                cur_x += 1
            if direction == 'L':
                cur_x -= 1
            if direction == 'U':
                cur_y += 1
            if direction == 'D':
                cur_y -= 1
            locns.append((cur_x, cur_y, time))
    return locns


path1 = parse_path(data[0].split(','))
path2 = parse_path(data[1].split(','))
path1_set = set(list(map(lambda p: (p[0], p[1]), path1)))
path2_set = set(list(map(lambda p: (p[0], p[1]), path2)))
shared_path = path1_set & path2_set
dist_time_map = []
for path_el1 in path1:
    if (path_el1[0], path_el1[1]) not in shared_path:
        continue
    for path_el2 in path2:
        if path_el1[0] == path_el2[0] and path_el1[1] == path_el2[1]:
            dist = abs(path_el1[0]) + abs(path_el2[0])
            time = path_el1[2] + path_el2[2]
            dist_time_map.append((dist, time))
dist_time_map.sort(key=lambda e: e[1])
print(dist_time_map[0][1])
