import sys

data = [line.rstrip() for line in sys.stdin.readlines()]
data = data[0]
data = [int(d) for d in data.split(',')]

def step(ptr, d):
    if d[ptr] == 99:
        return True, ptr, d
    if d[ptr] == 1:
        val1 = d[d[ptr+1]]
        val2 = d[d[ptr+2]]
        d[d[ptr+3]] = val1 + val2
        return False, ptr+4, d
    if d[ptr] == 2:
        val1 = d[d[ptr+1]]
        val2 = d[d[ptr+2]]
        d[d[ptr+3]] = val1 * val2
        return False, ptr+4, d
    raise RuntimeError('Unexpected opcode '+str(d[ptr])+' at posn '+str(ptr))


test_data = [1003,4,3,4,33]
data = test_data

ptr = 0
while True:
    should_halt, ptr, data = step(ptr, data)
    #    print(should_halt, ptr, data)
    if should_halt:
        break

print(data[0])
