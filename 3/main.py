def p1(f):
    lines = [[int(i) for i in x.strip()] for x in f]
    return int("".join(str(round(sum(l) / len(l))) for l in zip(*lines)), 2) * int(
        "".join(str(1 - round(sum(l) / len(l))) for l in zip(*lines)), 2
    )


def p2(f):
    lines = f.read().splitlines()
    lines2 = lines[:]

    i = 0
    while len(lines) > 1:
        c = round(0.0001 + sum(int(x[i]) for x in lines) / len(lines))
        lines = [x for x in lines if int(x[i]) == c]
        i += 1

    i = 0
    while len(lines2) > 1:
        c = 1 - round(0.0001 + sum(int(x[i]) for x in lines2) / len(lines2))
        lines2 = [x for x in lines2 if int(x[i]) == c]
        i += 1

    return int(lines[0], 2) * int(lines2[0], 2)
