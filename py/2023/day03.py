# Day       Time  Rank  Score       Time  Rank  Score
#   3   00:04:58    16     85   00:07:55    15     86


import re
from collections import defaultdict


def p1(f):
    lines = f.read().splitlines()
    ans = 0
    for i, line in enumerate(lines):
        for m in re.finditer(r"\d+", line):
            idxs = [(i, m.start() - 1), (i, m.end())]
            idxs += [(i - 1, j) for j in range(m.start() - 1, m.end() + 1)]
            idxs += [(i + 1, j) for j in range(m.start() - 1, m.end() + 1)]
            count = sum(0 <= a < len(lines) and 0 <= b < len(lines[a]) and lines[a][b] != "." for a, b in idxs)
            if count > 0:
                ans += int(m.group())
    return ans


def p2(f):
    lines = f.read().splitlines()
    adj = defaultdict(list)
    for i, line in enumerate(lines):
        for m in re.finditer(r"\d+", line):
            idxs = [(i, m.start() - 1), (i, m.end())]
            idxs += [(i - 1, j) for j in range(m.start() - 1, m.end() + 1)]
            idxs += [(i + 1, j) for j in range(m.start() - 1, m.end() + 1)]
            for a, b in idxs:
                if 0 <= a < len(lines) and 0 <= b < len(lines[a]) and lines[a][b] != ".":
                    adj[a, b].append(m.group())
    return sum(int(x[0]) * int(x[1]) for x in adj.values() if len(x) == 2)
