# Day       Time  Rank  Score       Time  Rank  Score
#  14   00:11:27   131      0   00:13:23    81     20


from itertools import count, product

ORIGIN = 500, 0


def draw(x1, y1, x2, y2):
    if x1 > x2:
        return draw(x2, y1, x1, y2)
    if y1 > y2:
        return draw(x1, y2, x2, y1)
    return product(range(x1, x2 + 1), range(y1, y2 + 1))


def adj(x, y):
    return (x, y + 1), (x - 1, y + 1), (x + 1, y + 1)


def p1(f):
    rocks = set()

    for line in f:
        pts = line.split(" -> ")
        for a, b in zip(pts, pts[1:]):
            rocks.update(draw(*eval(a), *eval(b)))

    max_y = max(y for _, y in rocks)

    for i in count():
        curr = ORIGIN

        while curr[1] < max_y:
            try:
                curr = next(x for x in adj(*curr) if x not in rocks)
            except StopIteration:
                break
        else:
            return i

        rocks.add(curr)


def p2(f):
    rocks = set()

    for line in f:
        pts = line.split(" -> ")
        for a, b in zip(pts, pts[1:]):
            rocks.update(draw(*eval(a), *eval(b)))

    max_y = max(y for _, y in rocks)

    for i in count():
        curr = ORIGIN

        while True:
            try:
                curr = next(p for p in adj(*curr) if p not in rocks and p[1] < max_y + 2)
            except StopIteration:
                break

        if curr == ORIGIN:
            return i + 1

        rocks.add(curr)
