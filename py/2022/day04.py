irange = lambda a, b: range(a, b + 1)


def p1(f):
    ans = 0
    for l in f:
        a, b = l.strip().split(",")
        a = set(irange(*map(int, a.split("-"))))
        b = set(irange(*map(int, b.split("-"))))
        if len(a - b) == 0 or len(b - a) == 0:
            ans += 1
    return ans


def p2(f):
    ans = 0
    for l in f:
        a, b = l.strip().split(",")
        a = set(irange(*map(int, a.split("-"))))
        b = set(irange(*map(int, b.split("-"))))
        if len(a & b) > 0:
            ans += 1
    return ans
