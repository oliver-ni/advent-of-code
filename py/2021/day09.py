from collections import Counter
from math import prod


def adj(i, j):
    return (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)


def p1(f):
    nums = {(i, j): int(x) for i, line in enumerate(f) for j, x in enumerate(line.strip())}
    return sum(cell + 1 for p, cell in nums.items() if all(cell < nums.get(q, 9) for q in adj(*p)))


def p2(f):
    nums = {(i, j): int(x) for i, line in enumerate(f) for j, x in enumerate(line.strip())}
    basins = {}

    def dfs(p, idx):
        if p in basins or nums.get(p, 9) == 9:
            return
        basins[p] = idx
        for q in adj(*p):
            dfs(q, idx)

    for i, p in enumerate(nums.keys()):
        dfs(p, i)

    return prod(c for _, c in Counter(basins.values()).most_common(3))
