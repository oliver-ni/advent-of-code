import functools
import math
import re


@functools.cache
def xt(dx, x1, x2):
    x = 0
    result = None
    for t in range(1000):
        if x >= x1 and result is None:
            result = t, math.inf
        if x > x2:
            return result[0], t
        if dx == 0:
            break
        x += dx
        dx -= 1
    return result


def p1(f):
    x1, x2, y1, y2 = map(int, re.findall(r"-?\d+", f.read()))

    for dy in range(abs(y1), -abs(y1) - 1, -1):
        y = 0
        maxy = 0
        for t in range(1000):
            if y1 <= y <= y2:
                return maxy
            if y < y1 and dy < 0:
                break
            y += dy
            dy -= 1
            maxy = max(maxy, y)


def p2(f):
    x1, x2, y1, y2 = map(int, re.findall(r"-?\d+", f.read()))

    a = set()

    for dy in range(abs(y1), -abs(y1) - 1, -1):
        ody = dy
        y = 0
        maxy = 0
        for t in range(1000):
            if y1 <= y <= y2:
                for dx in range(x2 + 1):
                    match xt(dx, x1, x2):
                        case t0, t1:
                            if t0 <= t < t1:
                                a.add((dx, ody))
            if y < y1 and dy < 0:
                break
            y += dy
            dy -= 1
            maxy = max(maxy, y)

    return len(a)
