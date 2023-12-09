# Day       Time  Rank  Score       Time  Rank  Score
#   9   00:01:28     3     98   00:01:48     1    100

from itertools import pairwise


def seq(ints):
    if all(ints == 0 for ints in ints):
        return 0
    diffs = [b - a for a, b in pairwise(ints)]
    return ints[-1] + seq(diffs)


def p1(f):
    return sum(seq([int(x) for x in line.split()]) for line in f)


def p2(f):
    return sum(seq([int(x) for x in line.split()[::-1]]) for line in f)
