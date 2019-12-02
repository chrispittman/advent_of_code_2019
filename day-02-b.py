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


#test_data = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
#data = test_data
original_data = data.copy()

# there's gotta be a more clever way to do this than to iterate over
# all possible noun/verb combinations...
# looks like this calculates 2560661 + (432000*noun) + verb,
# at least for my input
for noun in range(100):
    for verb in range(100):
        data = original_data.copy()
        data[1] = noun
        data[2] = verb
        ptr = 0
        while True:
            should_halt, ptr, data = step(ptr, data)
            if should_halt:
                break
        if data[0] == 19690720:
            print((100 * noun) + verb)
