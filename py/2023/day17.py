# Day       Time  Rank  Score       Time  Rank  Score
#  17   00:14:54   115      0   00:16:17    56     45

from collections import defaultdict
from heapq import heappop, heappush


def dijkstra(grid, s, e, neighbors, max_run):
    start = s, (0, 0)
    dist = defaultdict(lambda: float("inf"), {start: 0})
    pq = [(0, start)]
    while pq:
        _, u = heappop(pq)
        if not all(-max_run <= n <= max_run for n in u[1]):
            continue
        if u[0] == e:
            return dist[u]
        for v in neighbors(*u):
            if v[0] not in grid:
                continue
            alt = dist[u] + grid[v[0]]
            if alt < dist[v]:
                dist[v] = alt
                heappush(pq, (alt, v))


def neighbors1(p, run):
    r, c = p
    nr, nc = run
    if nr == 0:
        yield (r - 1, c), (-1, 0)
        yield (r + 1, c), (1, 0)
    if nc == 0:
        yield (r, c - 1), (0, -1)
        yield (r, c + 1), (0, 1)
    if nr > 0:
        yield (r + 1, c), (nr + 1, 0)
    if nr < 0:
        yield (r - 1, c), (nr - 1, 0)
    if nc > 0:
        yield (r, c + 1), (0, nc + 1)
    if nc < 0:
        yield (r, c - 1), (0, nc - 1)


def p1(f):
    lines = f.read().splitlines()
    grid = {(i, j): int(x) for i, line in enumerate(lines) for j, x in enumerate(line)}
    n, m = len(lines), len(lines[0])
    return dijkstra(grid, (0, 0), (n - 1, m - 1), neighbors1, 3)


def neighbors2(p, run):
    r, c = p
    nr, nc = run
    if 0 < nr < 4:
        yield (r + 1, c), (nr + 1, 0)
    elif -4 < nr < 0:
        yield (r - 1, c), (nr - 1, 0)
    elif 0 < nc < 4:
        yield (r, c + 1), (0, nc + 1)
    elif -4 < nc < 0:
        yield (r, c - 1), (0, nc - 1)
    else:
        yield from neighbors1(p, run)


def p2(f):
    lines = f.read().splitlines()
    grid = {(i, j): int(x) for i, line in enumerate(lines) for j, x in enumerate(line)}
    n, m = len(lines), len(lines[0])
    return dijkstra(grid, (0, 0), (n - 1, m - 1), neighbors2, 10)
