# Day       Time  Rank  Score       Time  Rank  Score
#  23   00:04:37     8     93   01:53:00  1336      0

import sys

sys.setrecursionlimit(2**31 - 1)


def neighbors(i, j):
    yield i - 1, j
    yield i + 1, j
    yield i, j - 1
    yield i, j + 1


def p1(f):
    lines = f.read().splitlines()
    N, M = len(lines), len(lines[0])
    grid = {(i, j): x for i, l in enumerate(lines) for j, x in enumerate(l) if x != "#"}

    visited = set()

    def dfs(p):
        if p == (N - 1, M - 2):
            return 0
        visited.add(p)
        ans = float("-inf")
        ns = list(neighbors(*p))
        if grid[p] in "^v<>":
            ns = [ns["^v<>".index(grid[p])]]
        for n in ns:
            if n not in grid or n in visited:
                continue
            ans = max(ans, 1 + dfs(n))
        visited.remove(p)
        return ans

    return dfs((0, 1))


def p2(f):
    lines = f.read().splitlines()
    N, M = len(lines), len(lines[0])
    grid = {(i, j) for i, l in enumerate(lines) for j, x in enumerate(l) if x != "#"}
    adj = {p: {q: 1 for q in neighbors(*p) if q in grid} for p in grid}

    while True:
        for p, qs in adj.items():
            if len(qs) != 2:
                continue
            q1, q2 = adj[p]
            adj[q1][q2] = adj[q2][q1] = adj[q1][p] + adj[p][q2]
            del adj[p], adj[q1][p], adj[q2][p]
            break
        else:
            break

    visited = set()

    def dfs(p):
        if p == (N - 1, M - 2):
            return 0
        visited.add(p)
        ans = float("-inf")
        for n, dist in adj[p].items():
            if n in visited:
                continue
            ans = max(ans, dist + dfs(n))
        visited.remove(p)
        return ans

    return dfs((0, 1))
