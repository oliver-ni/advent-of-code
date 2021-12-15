import math
from collections import defaultdict
from heapq import heappop, heappush


def adj(i, j):
    return (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)


def p1(f):
    lines = list(f)
    size = len(lines)
    nums = {(i, j): int(x) for i, row in enumerate(lines) for j, x in enumerate(row.strip())}

    dist = defaultdict(lambda: math.inf, {(0, 0): 0})
    pq = [(0, (0, 0))]

    while len(pq) > 0:
        _, p = heappop(pq)
        if p == (size - 1, size - 1):
            return dist[p]
        for q in adj(*p):
            alt = dist[p] + nums.get(q, math.inf)
            if alt < dist[q]:
                dist[q] = alt
                heappush(pq, (dist[q], q))


def p2(f):
    lines = list(f)
    size = len(lines)
    nums = {
        (a * size + i, b * size + j): (int(x) + a + b - 1) % 9 + 1
        for i, row in enumerate(lines)
        for j, x in enumerate(row.strip())
        for a in range(5)
        for b in range(5)
    }

    dist = defaultdict(lambda: math.inf, {(0, 0): 0})
    pq = [(0, (0, 0))]

    while len(pq) > 0:
        _, p = heappop(pq)
        if p == (size * 5 - 1, size * 5 - 1):
            return dist[p]
        for q in adj(*p):
            alt = dist[p] + nums.get(q, math.inf)
            if alt < dist[q]:
                dist[q] = alt
                heappush(pq, (dist[q], q))
