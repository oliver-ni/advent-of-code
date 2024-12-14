# Day       Time   Rank  Score       Time   Rank  Score
#  12   00:15:52   1487      0       >24h  30968      0

from collections import Counter


class T(tuple):
    def __add__(self, other):
        return T(x + y for x, y in zip(self, other))

    def rot(self):
        x, y = self
        return T((y, -x))


ZERO = T((0, 0))
NORTH = T((-1, 0))
EAST = NORTH.rot()
SOUTH = EAST.rot()
WEST = SOUTH.rot()

ORTHOGONAL = (NORTH, EAST, SOUTH, WEST)
DIAGONAL = (NORTH + EAST, NORTH + WEST, SOUTH + EAST, SOUTH + WEST)


def fill(grid, p, letter):
    if grid.get(p) != letter:
        return
    grid[p] = None
    yield p
    for dir in ORTHOGONAL:
        yield from fill(grid, p + dir, letter)


def p1(f):
    grid = {
        T((i, j)): c
        for i, r in enumerate(f.read().splitlines())
        for j, c in enumerate(r)
    }
    ans = 0
    for p, c in grid.items():
        if c is None:
            continue
        squares = list(fill(grid, p, c))
        perim = 0
        for p in squares:
            perim += 4
            if p + NORTH in squares:
                perim -= 2
            if p + WEST in squares:
                perim -= 2
        ans += perim * len(squares)
    return ans


def p2(f):
    grid = {
        T((i, j)): c
        for i, r in enumerate(f.read().splitlines())
        for j, c in enumerate(r)
    }

    ans = 0
    for p, c in grid.items():
        if c is None:
            continue
        squares = list(fill(grid, p, c))

        big_squares = {
            p + p + offset
            for p in squares
            for offset in (ZERO, SOUTH, EAST, SOUTH + EAST)
        }

        has_ne = Counter(p for p in big_squares if p + NORTH + EAST in big_squares)
        has_nw = Counter(p for p in big_squares if p + NORTH + WEST in big_squares)
        has_se = Counter(p for p in big_squares if p + SOUTH + EAST in big_squares)
        has_sw = Counter(p for p in big_squares if p + SOUTH + WEST in big_squares)
        has_opp1 = has_ne & has_sw - has_se - has_nw
        has_opp2 = has_se & has_nw - has_ne - has_sw

        counts = Counter((has_ne + has_nw + has_se + has_sw).values())
        sides = counts[3] // 3 + counts[1] + len(has_opp1) + len(has_opp2)

        ans += sides * len(squares)

    return ans
