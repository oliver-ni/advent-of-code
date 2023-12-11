# Day       Time  Rank  Score       Time  Rank  Score
#  11   00:03:31    11     90   00:04:14     3     98

from itertools import combinations


def p1(f):
    grid = [line.strip() for line in f]
    dbl_i = {i for i, line in enumerate(grid) if "#" not in line}
    dbl_j = {j for j in range(len(grid[0])) if "#" not in [line[j] for line in grid]}
    pts = {(i, j) for i, l in enumerate(grid) for j, c in enumerate(l) if c == "#"}

    return sum(
        abs(p[0] - q[0])
        + abs(p[1] - q[1])
        + len(dbl_i & set(range(min(p[0], q[0]), max(p[0], q[0]) + 1)))
        + len(dbl_j & set(range(min(p[1], q[1]), max(p[1], q[1]) + 1)))
        for p, q in combinations(pts, 2)
    )


def p2(f):
    grid = [line.strip() for line in f]
    dbl_i = {i for i, line in enumerate(grid) if "#" not in line}
    dbl_j = {j for j in range(len(grid[0])) if not any(line[j] == "#" for line in grid)}
    pts = {(i, j) for i, l in enumerate(grid) for j, c in enumerate(l) if c == "#"}

    return sum(
        abs(p[0] - q[0])
        + abs(p[1] - q[1])
        + 999999 * len(dbl_i & set(range(min(p[0], q[0]), max(p[0], q[0]) + 1)))
        + 999999 * len(dbl_j & set(range(min(p[1], q[1]), max(p[1], q[1]) + 1)))
        for p, q in combinations(pts, 2)
    )
