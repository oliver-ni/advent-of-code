# Day       Time  Rank  Score       Time  Rank  Score
#   1   00:00:58    24     77   00:01:48    28     73


def p1(f):
    lines = [[int(x) for x in line.split()] for line in f.read().splitlines()]
    one, two = map(sorted, zip(*lines))
    return sum(abs(a - b) for a, b in zip(one, two))


def p2(f):
    lines = [[int(x) for x in line.split()] for line in f.read().splitlines()]
    one, two = map(sorted, zip(*lines))
    return sum(a * two.count(a) for a in one)
