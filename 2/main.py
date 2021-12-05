def p1(f):
    h = d = 0
    for line in f:
        a, b = line.split()
        if a == "forward":
            h += int(b)
        elif a == "up":
            d -= int(b)
        elif a == "down":
            d += int(b)
    return h * d


def p2(f):
    h = d = m = 0
    for line in f:
        a, b = line.split()
        b = int(b)
        if a == "forward":
            h += b
            d += m * b
        elif a == "up":
            m -= b
        elif a == "down":
            m += b
    return h * d
