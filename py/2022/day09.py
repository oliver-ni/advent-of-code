class lol(tuple):
    def __add__(self, other):
        return lol(a + b for a, b in zip(self, other))

    def __sub__(self, other):
        return lol(a - b for a, b in zip(self, other))


DIRS = {
    "R": lol((1, 0)),
    "L": lol((-1, 0)),
    "U": lol((0, 1)),
    "D": lol((0, -1)),
}


def move(h, t):
    diff = lol(min(1, max(-1, x)) for x in h - t)
    if h - t == diff:
        return t
    return t + diff


def p1(f):
    h = t = lol((0, 0))
    pos = set()

    for line in f.read().splitlines():
        dir, step = line.split()

        for i in range(int(step)):
            h += DIRS[dir]
            t = move(h, t)
            pos.add(t)

    return len(pos)


def p2(f):
    a = [lol((0, 0)) for i in range(10)]
    pos = set()

    for line in f.read().splitlines():
        dir, step = line.split()

        for i in range(int(step)):
            a[0] += DIRS[dir]

            for i in range(len(a) - 1):
                a[i + 1] = move(a[i], a[i + 1])

            pos.add(a[9])

    return len(pos)
