# Day       Time  Rank  Score       Time  Rank  Score
#  18   00:12:35   298      0   00:14:45    31     70


class _(tuple):
    def __add__(self, other):
        return _(x + y for x, y in zip(self, other))

    def __mul__(self, other):
        return _(x * other for x in self)


NORTH = _((-1, 0))
SOUTH = _((1, 0))
EAST = _((0, 1))
WEST = _((0, -1))

DIRECTIONS = {
    "U": NORTH,
    "D": SOUTH,
    "R": EAST,
    "L": WEST,
}


def p1(f):
    pos = _((0, 0))
    vertices = [pos]
    boundary = 0
    for line in f:
        dir, num, hex = line.split()
        num = int(num)
        vertices.append(vertices[-1] + DIRECTIONS[dir] * num)
        boundary += num
    xs, ys = zip(*vertices)
    left = sum(a * b for a, b in zip(xs, ys[1:]))
    right = sum(a * b for a, b in zip(ys, xs[1:]))
    return abs(left - right) // 2 + boundary // 2 + 1


def p2(f):
    pos = _((0, 0))
    vertices = [pos]
    boundary = 0
    for line in f:
        dir, num, hex = line.split()
        dir = "RDLU"[int(hex[-2])]
        num = int(hex[2:-2], 16)
        vertices.append(vertices[-1] + DIRECTIONS[dir] * num)
        boundary += num
    xs, ys = zip(*vertices)
    left = sum(a * b for a, b in zip(xs, ys[1:]))
    right = sum(a * b for a, b in zip(ys, xs[1:]))
    return abs(left - right) // 2 + boundary // 2 + 1
