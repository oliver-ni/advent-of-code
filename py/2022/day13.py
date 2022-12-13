# Day       Time  Rank  Score       Time  Rank  Score
#  13   00:10:02   167      0   00:13:01   104      0


from functools import total_ordering
from math import prod


def cmp(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a - b

    if isinstance(a, list) and isinstance(b, list):
        for x, y in zip(a, b):
            if result := cmp(x, y):
                return result
        return len(a) - len(b)

    if isinstance(a, list):
        return cmp(a, [b])

    if isinstance(b, list):
        return cmp([a], b)

    assert False


@total_ordering
class _:
    def __init__(self, x):
        self.x = x

    def __lt__(self, other):
        return cmp(self.x, other.x) < 0

    def __eq__(self, other):
        return cmp(self.x, other.x) == 0


def p1(f):
    pairs = [[eval(x) for x in pair.splitlines()] for pair in f.read().split("\n\n")]
    return sum(i + 1 for i, (a, b) in enumerate(pairs) if cmp(a, b) < 0)


def p2(f):
    packets = [eval(x) for x in f.read().splitlines() if len(x) > 0]
    dividers = [[2]], [[6]]
    result = sorted([*packets, *dividers], key=_)
    return prod(result.index(x) + 1 for x in dividers)
