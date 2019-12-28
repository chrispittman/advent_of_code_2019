import sys
from math import atan2

data = [line.rstrip() for line in sys.stdin.readlines()]


def calc_dir(x, y):
    return "{0:.5f}".format(atan2(x, y))


# O(n^4) - ugh
ast_counts = {}
for x in range(len(data)):
    for y in range(len(data[0])):
        if not data[x][y] == '#':
            continue
        dirs = set()
        for i in range(len(data)):
            for j in range(len(data[0])):
                if i == x and j == y:
                    continue
                if not data[i][j] == '#':
                    continue
                dx = i - x
                dy = j - y
                dir = calc_dir(dx, dy)
                dirs.add(dir)
        ast_counts[(x,y)] = len(dirs)

best = max(ast_counts, key=ast_counts.get)
print(best, ast_counts[best])
