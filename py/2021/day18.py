import itertools
from functools import cache


@cache
def addl(x, v):
    match x:
        case a, b:
            return addl(a, v), b
    return x + v


@cache
def addr(x, v):
    match x:
        case a, b:
            return a, addr(b, v)
    return x + v


@cache
def explode(x, lvl=0):
    if lvl == 4:
        return 0, x
    match x:
        case a, b:
            match explode(a, lvl + 1):
                case n, (l, r):
                    return (n, addl(b, r)), (l, 0)
            match explode(b, lvl + 1):
                case n, (l, r):
                    return (addr(a, l), n), (0, r)
    return x, None


@cache
def split(x):
    match x:
        case a, b:
            match split(a):
                case n, True:
                    return (n, b), True
            n, e = split(b)
            return (a, n), e
        case x if x >= 10:
            return (x // 2, (x + 1) // 2), True
    return x, False


@cache
def reduce(x):
    e = True
    while e:
        x, e = explode(x)
        if not e:
            x, e = split(x)
    return x


@cache
def magnitude(x):
    match x:
        case a, b:
            return 3 * magnitude(a) + 2 * magnitude(b)
    return x


def p1(f):
    pairs = [eval(x.replace("[", "(").replace("]", ")")) for x in f]
    while len(pairs) > 1:
        a, b, *rest = pairs
        pairs = reduce((a, b)), *rest
    return magnitude(pairs[0])


def p2(f):
    pairs = [eval(x.replace("[", "(").replace("]", ")")) for x in f]
    return max(magnitude(reduce((a, b))) for a, b in itertools.permutations(pairs, 2))
