PRIO = ".abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def p1(f):
    ans = 0

    for line in f:
        m = len(line) // 2
        a, b = line[:m], line[m:]
        c = set(a) & set(b)
        ans += PRIO.index(next(iter(c)))

    return ans


def p2(f):
    ans = 0
    ff = iter(f.read().split())

    while True:
        try:
            a, b, c = next(ff), next(ff), next(ff)
        except StopIteration:
            return ans

        d = set(a) & set(b) & set(c)
        ans += PRIO.index(next(iter(d)))
