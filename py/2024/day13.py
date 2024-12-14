# Day       Time   Rank  Score       Time   Rank  Score
#  13       >24h  34742      0       >24h  29891      0

import re


def solve(adx, ady, bdx, bdy, tx, ty):
    thing = adx * bdy - bdx * ady
    a = (bdy * tx - bdx * ty) / thing
    b = (-ady * tx + adx * ty) / thing
    if a == int(a) and b == int(b):
        return int(a) * 3 + int(b)
    return 0


def p1(f):
    machines = [[int(x) for x in re.findall(r"\d+", s)] for s in f.read().split("\n\n")]
    return sum(solve(*m) for m in machines)


def p2(f):
    machines = [[int(x) for x in re.findall(r"\d+", s)] for s in f.read().split("\n\n")]
    return sum(
        solve(adx, ady, bdx, bdy, tx + 10000000000000, ty + 10000000000000)
        for adx, ady, bdx, bdy, tx, ty in machines
    )
