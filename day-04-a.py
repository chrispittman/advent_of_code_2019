import sys

data = [line.rstrip() for line in sys.stdin.readlines()]
[lower, upper] = data[0].split('-')


def is_possible_password(s):
    if (s[0]>s[1] or s[1]>s[2] or s[2]>s[3] or s[3]>s[4] or s[4]>s[5]):
        return False
    if (s[0]==s[1] or s[1]==s[2] or s[2]==s[3] or s[3]==s[4] or s[4]==s[5]):
        return True
    return False


#print(is_possible_password('111111'))
#print(is_possible_password('223450'))
#print(is_possible_password('123789'))
num_possible = 0
for i in range(int(lower), int(upper)):
    if is_possible_password(str(i)):
        num_possible += 1
print(num_possible)