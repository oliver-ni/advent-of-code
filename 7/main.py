def p1(f):
    a = [int(x) for x in f.read().split(",")]
    return min(sum(abs(x - i) for x in a) for i in a)


def p2(f):
    a = [int(x) for x in f.read().split(",")]
    return min(
        sum(abs(x - i) * (abs(x - i) + 1) // 2 for x in a)
        for i in range(min(a), max(a) + 1)
    )
