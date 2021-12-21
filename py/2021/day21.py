import functools
import itertools


def p1(f):
    a, b = [int(x.split()[-1]) for x in f]
    sa, sb = 0, 0

    die = itertools.cycle(range(1, 101))
    rolls = 0

    while sb < 1000:
        roll = next(die) + next(die) + next(die)
        rolls += 3
        a = (a + roll - 1) % 10 + 1
        sa += a

        a, b = b, a
        sa, sb = sb, sa

    return rolls * sa


@functools.cache
def solve(a, b, sa=0, sb=0):
    wa, wb = 0, 0
    for r in itertools.product(range(1, 4), repeat=3):
        na = (a + sum(r) - 1) % 10 + 1
        if sa + na >= 21:
            wa += 1
            continue
        nwb, nwa = solve(b, na, sb, sa + na)
        wa += nwa
        wb += nwb
    return wa, wb


def p2(f):
    a, b = [int(x.split()[-1]) for x in f]
    return max(solve(a, b))
