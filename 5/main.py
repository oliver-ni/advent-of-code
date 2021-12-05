import re
from collections import defaultdict


def nrange(s, e):
    if e >= s:
        return range(s, e + 1)
    else:
        return range(s, e - 1, -1)


def p1(f):
    pts = defaultdict(int)
    for line in f:
        ax, ay, bx, by = map(int, re.findall(r"\d+", line))
        if ax == bx:
            for y in range(min(ay, by), max(ay, by) + 1):
                pts[ax, y] += 1
        elif ay == by:
            for x in range(min(ax, bx), max(ax, bx) + 1):
                pts[x, ay] += 1
    return sum(1 for x in pts.values() if x >= 2)


def p2(f):
    pts = defaultdict(int)
    for line in f:
        ax, ay, bx, by = map(int, re.findall(r"\d+", line))
        if ax == bx:
            for y in range(min(ay, by), max(ay, by) + 1):
                pts[ax, y] += 1
        elif ay == by:
            for x in range(min(ax, bx), max(ax, bx) + 1):
                pts[x, ay] += 1
        else:
            for x, y in zip(nrange(ax, bx), nrange(ay, by)):
                pts[x, y] += 1
    return sum(1 for x in pts.values() if x >= 2)
