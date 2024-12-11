# Day       Time   Rank  Score       Time   Rank  Score
#  11   00:04:43    529      0   00:07:12    139      0

from functools import cache
from math import log10


@cache
def solve(n, k):
    if k == 0:
        return 1
    if n == 0:
        return solve(1, k - 1)
    quo, rem = divmod(int(log10(n)) + 1, 2)
    if rem == 0:
        fst, snd = divmod(n, 10**quo)
        return solve(fst, k - 1) + solve(snd, k - 1)
    else:
        return solve(n * 2024, k - 1)


def p1(f):
    return sum(solve(int(x), 25) for x in f.read().split())


def p2(f):
    return sum(solve(int(x), 75) for x in f.read().split())
