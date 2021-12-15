PAIRS = "()", "[]", "{}", "<>"
OTHER = {b: a for a, b in PAIRS}


def p1(f):
    scores = []

    for line in f:
        a = []
        for x in line.strip():
            if x in "[<({":
                a.append(x)
            elif a.pop() != OTHER[x]:
                scores.append({")": 3, "]": 57, "}": 1197, ">": 25137}[x])
                break

    return sum(scores)


def p2(f):
    scores = []

    for line in f:
        a = []
        for x in line.strip():
            if x in "[<({":
                a.append(x)
            elif a.pop() != OTHER[x]:
                break
        else:
            s = 0
            while len(a) > 0:
                s *= 5
                s += {"(": 1, "[": 2, "{": 3, "<": 4}[a.pop()]
            scores.append(s)

    return sorted(scores)[len(scores) // 2]
