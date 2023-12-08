# Day       Time  Rank  Score       Time  Rank  Score
#   8   00:02:30    15     86   00:16:24   408      0

import math
from itertools import cycle


def p1(f):
    path, maps = f.read().split("\n\n")
    maps = [x.split(" = ") for x in maps.splitlines()]
    maps = {a: b[1:-1].split(", ") for a, b in maps}

    curr = "AAA"
    for count, d in enumerate(cycle(path), start=1):
        curr = maps[curr][d == "R"]
        if curr == "ZZZ":
            return count


def p2(f):
    path, maps = f.read().split("\n\n")
    maps = [x.split(" = ") for x in maps.splitlines()]
    maps = {a: b[1:-1].split(", ") for a, b in maps}

    ans = []

    for curr in maps:
        if not curr.endswith("A"):
            continue
        visited = set()
        for count, (idx, d) in enumerate(cycle(enumerate(path)), start=1):
            prev, curr = curr, maps[curr][d == "R"]
            visited.add((curr, idx))
            if prev.endswith("Z") and (curr, idx) in visited:
                ans.append(count - 1)
                break

    return math.lcm(*ans)
