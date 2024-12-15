# Day       Time   Rank  Score       Time   Rank  Score
#  15   00:14:02    379      0   00:42:41    449      0


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

DIRS = {
    "<": WEST,
    "^": NORTH,
    "v": SOUTH,
    ">": EAST,
}


def p1(f):
    g, moves = f.read().split("\n\n")
    grid = {T((i, j)): c for i, r in enumerate(g.splitlines()) for j, c in enumerate(r)}
    pos = next(p for p, c in grid.items() if c == "@")
    grid[pos] = "."

    def push_box(p, dir):
        if grid[p + dir] == "#":
            return
        if grid[p + dir] == ".":
            return p + dir
        return push_box(p + dir, dir)

    for thing in moves.replace("\n", ""):
        dir = DIRS[thing]
        if grid[pos + dir] == "#":
            continue
        if grid[pos + dir] == "O":
            if push_to := push_box(pos + dir, dir):
                grid[push_to] = "O"
                grid[pos + dir] = "."
            else:
                continue
        pos += dir

    return sum(100 * i + j for (i, j), c in grid.items() if c == "O")


def p2(f):
    g, moves = f.read().split("\n\n")
    g = g.replace("#", "##").replace("O", "[]").replace(".", "..").replace("@", "@.")
    grid = {T((i, j)): c for i, r in enumerate(g.splitlines()) for j, c in enumerate(r)}
    pos = next(p for p, c in grid.items() if c == "@")
    grid[pos] = "."

    def push(p, dir):
        if grid[p + dir] == "#":
            raise ValueError("cannot push")
        if grid[p + dir] == "[" and dir != WEST:
            yield from push(p + dir + EAST, dir)
            yield from push(p + dir, dir)
        if grid[p + dir] == "]" and dir != EAST:
            yield from push(p + dir + WEST, dir)
            yield from push(p + dir, dir)
        yield p

    for thing in moves.replace("\n", ""):
        dir = DIRS[thing]
        if grid[pos + dir] == "#":
            continue
        try:
            things = dict.fromkeys(push(pos, dir))
        except ValueError:
            continue
        for thing in things.keys():
            grid[thing + dir] = grid[thing]
            grid[thing] = "."
        pos += dir

    return sum(100 * i + j for (i, j), c in grid.items() if c == "[")
