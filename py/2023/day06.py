# Day       Time  Rank  Score       Time  Rank  Score
#   6   00:03:28   142      0   00:06:02   221      0


import math


def p1(f):
    races = [map(int, line.split()[1:]) for line in f]
    ans = 1
    for time, dist in zip(*races):
        ans *= sum((time - hold) * hold >= dist for hold in range(time))
    return ans


def p2(f):
    time, dist = [int(line.replace(" ", "").split(":")[1]) for line in f]
    a = (time - math.sqrt(time**2 - 4 * dist)) / 2
    b = (time + math.sqrt(time**2 - 4 * dist)) / 2
    return math.floor(b) - math.ceil(a) + 1
