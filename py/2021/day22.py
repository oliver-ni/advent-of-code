import re
from itertools import product


def crange(a, b):
    return range(max(a, -50), min(b, 51))


def p1(f):
    points = set()
    for line in f:
        x1, x2, y1, y2, z1, z2 = map(int, re.findall(r"-?\d+", line))
        region = product(crange(x1, x2 + 1), crange(y1, y2 + 1), crange(z1, z2 + 1))
        if line.startswith("on"):
            points |= set(region)
        else:
            points -= set(region)
    return len(points)


def p2(f):
    instructions = []
    xs = set()
    ys = set()
    zs = set()

    for line in f:
        x1, x2, y1, y2, z1, z2 = map(int, re.findall(r"-?\d+", line))
        instructions.append((line.startswith("on"), (x1, x2 + 1, y1, y2 + 1, z1, z2 + 1)))
        xs |= {x1, x2 + 1}
        ys |= {y1, y2 + 1}
        zs |= {z1, z2 + 1}

    xtr = list(sorted(xs))
    ytr = list(sorted(ys))
    ztr = list(sorted(zs))

    xfr = {x: i for i, x in enumerate(xtr)}
    yfr = {y: i for i, y in enumerate(ytr)}
    zfr = {z: i for i, z in enumerate(ztr)}

    points = set()
    for state, (x1, x2, y1, y2, z1, z2) in instructions:
        region = set(
            len(yfr) * len(zfr) * x + len(zfr) * y + z
            for x in range(xfr[x1], xfr[x2])
            for y in range(yfr[y1], yfr[y2])
            for z in range(zfr[z1], zfr[z2])
        )
        if state:
            points |= region
        else:
            points -= region

    ans = 0
    for p in points:
        y, z = divmod(p, len(zfr))
        x, y = divmod(y, len(yfr))
        ans += (xtr[x + 1] - xtr[x]) * (ytr[y + 1] - ytr[y]) * (ztr[z + 1] - ztr[z])

    return ans
