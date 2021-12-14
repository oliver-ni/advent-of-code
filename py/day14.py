from collections import Counter


def p1(f):
    code, rules = f.read().strip().split("\n\n")
    rules = [x.split(" -> ") for x in rules.splitlines()]
    rules = {a: b for a, b in rules}

    for i in range(10):
        newcode = ""
        for a, b in zip(code, code[1:]):
            c = f"{a}{b}"
            newcode += a + rules[c]
        newcode += b
        code = newcode

    cc = Counter(code)
    aa = cc.most_common()
    return aa[0][1] - aa[-1][1]


def p2(f):
    code, rules = f.read().strip().split("\n\n")
    rules = [x.split(" -> ") for x in rules.splitlines()]
    rules = {a: b for a, b in rules}

    pairs = Counter(f"{a}{b}" for a, b in zip(code, code[1:]))

    for i in range(40):
        newpairs = Counter()
        for p, c in pairs.items():
            newpairs[p[0] + rules[p]] += c
            newpairs[rules[p] + p[1]] += c
        pairs = newpairs

    cc = Counter([code[0]])
    for (a, b), c in pairs.items():
        cc[b] += c

    aa = cc.most_common()
    return aa[0][1] - aa[-1][1]
