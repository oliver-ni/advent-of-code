# Day       Time  Rank  Score       Time  Rank  Score
#  21   00:08:16   521      0   08:28:05  3697      0


def do(get, start, t):
    bfs = set([start])

    for _ in range(t):
        new_bfs = set()
        for i, j in bfs:
            new_bfs.add((i, j - 1))
            new_bfs.add((i, j + 1))
            new_bfs.add((i - 1, j))
            new_bfs.add((i + 1, j))
        new_bfs = {(i, j) for i, j in new_bfs if get(i, j) == "."}
        bfs = new_bfs

    return len(bfs)


def p1(f):
    grid = {(i, j): x for i, line in enumerate(f) for j, x in enumerate(line.strip())}
    start = next(p for p, x in grid.items() if x == "S")
    grid[start] = "."
    return do(lambda i, j: grid.get((i, j)), start, 64)


def p2(f):
    lines = f.read().splitlines()
    n, m = len(lines), len(lines[0])
    grid = {(i, j): x for i, line in enumerate(lines) for j, x in enumerate(line)}
    start = next(p for p, x in grid.items() if x == "S")
    grid[start] = "."

    print(n, m)
    print(divmod(26501365, n))

    get = lambda i, j: grid[i % n, j % m]

    print(26501365 % n, do(get, start, 26501365 % n))
    print(26501365 % n + n, do(get, start, 26501365 % n + n))
    print(26501365 % n + 2 * n, do(get, start, 26501365 % n + 2 * n))
    print(26501365 % n + 3 * n, do(get, start, 26501365 % n + 3 * n))
    return 3916 + 15544 * 202300 + 15410 * 202300**2
