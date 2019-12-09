import sys

data = [line.rstrip() for line in sys.stdin.readlines()]

#data = ["COM)B","B)C","C)D","D)E","E)F","B)G","G)H","D)I","E)J","J)K","K)L","K)YOU","I)SAN"]


def calc_path(data, path, target):
    parents = [el for el in data if el.endswith(')'+target)]
    if len(parents) == 0:
        return path
    parent = parents[0].split(')')[0]
    path.insert(0, parent)
    return calc_path(data, path, parent)


path1 = calc_path(data, [], 'YOU')
path2 = calc_path(data, [], 'SAN')
while path1[0] == path2[0]:
    del(path1[0])
    del(path2[0])
print(len(path1) + len(path2))