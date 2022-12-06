def p1(f):
    line = f.read()
    for i, _ in enumerate(line):
        if len(set(line[i - 4 : i])) == 4:
            return i


def p2(f):
    line = f.read()
    for i, _ in enumerate(line):
        if len(set(line[i - 14 : i])) == 14:
            return i
