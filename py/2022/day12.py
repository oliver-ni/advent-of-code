# Day       Time  Rank  Score       Time  Rank  Score
#  12   00:10:03   231      0   00:11:14   163      0


from collections import deque


def adj(i, j):
    return (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)


def p1(f):
    grid = {
        (i, j): x
        for i, row in enumerate(f.read().splitlines())
        for j, x in enumerate(row)
    }

    start = next(k for k, v in grid.items() if v == "S")
    end = next(k for k, v in grid.items() if v == "E")

    grid[start] = "a"
    grid[end] = "z"

    dist = {}
    bfs = deque([(0, start)])

    while len(bfs) > 0:
        t, p = bfs.popleft()
        if p in dist:
            continue
        dist[p] = t

        for q in adj(*p):
            if ord(grid.get(q, "~")) - ord(grid[p]) > 1:
                continue
            bfs.append((t + 1, q))

    return dist[end]


def p2(f):
    grid = {
        (i, j): "a" if x == "S" else x
        for i, row in enumerate(f.read().splitlines())
        for j, x in enumerate(row)
    }

    starts = {k for k, v in grid.items() if v == "a"}
    end = next(k for k, v in grid.items() if v == "E")
    grid[end] = "z"

    dist = {}
    bfs = deque([(0, x) for x in starts])

    while len(bfs) > 0:
        t, p = bfs.popleft()
        if p in dist:
            continue
        dist[p] = t

        for q in adj(*p):
            if ord(grid.get(q, "~")) - ord(grid[p]) > 1:
                continue
            bfs.append((t + 1, q))

    return dist[end]
