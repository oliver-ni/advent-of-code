# Day       Time   Rank  Score       Time   Rank  Score
#  10   00:03:46    197      0   00:04:09     96      5


class T(tuple):
    def __add__(self, other):
        return T(x + y for x, y in zip(self, other))

    def rot(self):
        x, y = self
        return T((y, -x))


NORTH = T((-1, 0))
EAST = NORTH.rot()
SOUTH = EAST.rot()
WEST = SOUTH.rot()


def find(grid, p):
    if grid[p] == 9:
        yield [p]
    for dir in (NORTH, EAST, SOUTH, WEST):
        if grid.get(p + dir, -1) == grid[p] + 1:
            for thing in find(grid, p + dir):
                yield [p, *thing]


def p1(f):
    grid = {
        T((i, j)): int(c)
        for i, r in enumerate(f.read().splitlines())
        for j, c in enumerate(r)
    }
    starts = [p for p, c in grid.items() if c == 0]
    return sum(len({path[-1] for path in find(grid, p)}) for p in starts)


def p2(f):
    grid = {
        T((i, j)): int(c)
        for i, r in enumerate(f.read().splitlines())
        for j, c in enumerate(r)
    }
    starts = [p for p, c in grid.items() if c == 0]
    return sum(1 for p in starts for _ in find(grid, p))
