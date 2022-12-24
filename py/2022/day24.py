# Day       Time  Rank  Score       Time  Rank  Score
#  24   00:22:12   111      0   00:23:25    70     31


from collections import deque

DIRECTIONS = [(1, 0, 0), (1, -1, 0), (1, 1, 0), (1, 0, -1), (1, 0, 1)]


def add_tuple(a, b):
    return tuple(sum(p) for p in zip(a, b))


def has_blizzard(grid, N, M, t, i, j):
    if (i, j) in ((-1, 0), (N, M - 1)):
        return False
    try:
        return (
            grid[(i - t) % N, j] == "v"
            or grid[(i + t) % N, j] == "^"
            or grid[i, (j - t) % M] == ">"
            or grid[i, (j + t) % M] == "<"
        )
    except KeyError:
        return True


def shortest(grid, N, M, start, end, start_t=0):
    visited = set()
    bfs = deque([(start_t, *start)])

    while len(bfs) > 0:
        t, i, j = p = bfs.popleft()
        if p in visited:
            continue
        visited.add(p)

        if (i, j) == end:
            return t

        for d in DIRECTIONS:
            x = add_tuple(p, d)
            if not has_blizzard(grid, N, M, *x):
                bfs.append(x)


def p1(f):
    lines = [row[1:-1] for row in f.read().splitlines()[1:-1]]
    grid = {(i, j): cell for i, row in enumerate(lines) for j, cell in enumerate(row)}
    N, M = len(lines), len(lines[0])
    grid[-1, 0] = grid[N, M - 1] = "."
    return shortest(grid, N, M, (-1, 0), (N, M - 1))


def p2(f):
    lines = [row[1:-1] for row in f.read().splitlines()[1:-1]]
    grid = {(i, j): cell for i, row in enumerate(lines) for j, cell in enumerate(row)}
    N, M = len(lines), len(lines[0])
    grid[-1, 0] = grid[N, M - 1] = "."

    t1 = shortest(grid, N, M, (-1, 0), (N, M - 1))
    t2 = shortest(grid, N, M, (N, M - 1), (-1, 0), t1)
    return shortest(grid, N, M, (-1, 0), (N, M - 1), t2)
