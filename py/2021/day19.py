import itertools
from collections import defaultdict


def rot(v):
    r = lambda a, b, c: (a, c, -b)
    t = lambda a, b, c: (-b, a, c)
    a = []
    for i in range(2):
        for j in range(3):
            v = r(*v)
            a.append(v)
            for i in range(3):
                v = t(*v)
                a.append(v)
        v = r(*t(*r(*v)))
    return a


def oo(aa, bb):
    ptsa = set(aa)
    for (a, b, c), (d, e, f) in itertools.product(aa, bb):
        if len(ptsa.intersection((x - d + a, y - e + b, z - f + c) for x, y, z in bb)) == 12:
            return d - a, e - b, f - c


def d(f):
    sc = [
        [*zip(*[rot([int(j) for j in i.split(",")]) for i in x.splitlines()[1:]])]
        for x in f.read().strip().split("\n\n")
    ]

    fr = {0: 0}
    fo = {0: (0, 0, 0)}
    nt = defaultdict(set)

    b = set(sc[0][0])

    while len(fr) < len(sc):
        for i, sci in enumerate(sc):
            if i in fr:
                continue
            for j, jrotidx in [*fr.items()]:
                if j in nt[i]:
                    continue
                scj = sc[j][jrotidx]
                axx, ayy, azz = fo[j]
                for rot_idx in range(24):
                    res = oo(scj, sci[rot_idx])
                    if res is None:
                        continue
                    ox, oy, oz = res
                    b |= {(x - ox - axx, y - oy - ayy, z - oz - azz) for x, y, z in sci[rot_idx]}
                    fr[i] = rot_idx
                    fo[i] = ox + axx, oy + ayy, oz + azz
                    break
                else:
                    continue
                break
            else:
                nt[i].add(j)
                continue
            break

    return fr, fo, b


def p1(f):
    return len(d(f)[2])


def p2(f):
    _, fo, _ = d(f)
    return max(
        sum(abs(i - j) for i, j in zip(fo[a], fo[b]))
        for a, b in itertools.product(range(len(fo)), repeat=2)
    )
