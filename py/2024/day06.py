# Day       Time   Rank  Score       Time   Rank  Score
#   6   00:04:42    277      0   00:41:35   2622      0


class T(tuple):
    def __add__(self, other):
        return T(x + y for x, y in zip(self, other))

    def rot(self):
        x, y = self
        return T((y, -x))


NORTH = T((-1, 0))


def sim(grid, pos, dir):
    visited = set()
    while pos in grid:
        if (pos, dir) in visited:
            return True, visited
        visited.add((pos, dir))
        while grid.get(pos + dir, ".") == "#":
            dir = dir.rot()
        pos += dir
    return False, visited


def p1(f):
    grid = {
        T((i, j)): c
        for i, r in enumerate(f.read().splitlines())
        for j, c in enumerate(r)
    }
    pos = next(p for p, c in grid.items() if c == "^")
    _, visited = sim(grid, pos, NORTH)
    visited = {p for p, d in visited}
    return len(visited)


def p2(f):
    grid = {
        T((i, j)): c
        for i, r in enumerate(f.read().splitlines())
        for j, c in enumerate(r)
    }
    pos = next(p for p, c in grid.items() if c == "^")
    _, visited = sim(grid, pos, NORTH)
    visited = {p for p, d in visited}

    ans = 0

    for vpos in visited:
        if grid[vpos] == "#":
            continue
        grid[vpos] = "#"
        works, _ = sim(grid, pos, NORTH)
        ans += works
        grid[vpos] = "."

    return ans
