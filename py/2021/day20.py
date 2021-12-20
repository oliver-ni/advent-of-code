from collections import defaultdict
from itertools import product


def enhance(alg, img):
    new_img = {}
    min_i = min(i for i, _ in img)
    max_i = max(i for i, _ in img)
    min_j = min(j for _, j in img)
    max_j = max(j for _, j in img)
    for i in range(min_i - 1, max_i + 2):
        for j in range(min_j - 1, max_j + 2):
            s = tuple(img[i + a, j + b] for a, b in product(range(-1, 2), repeat=2))
            num = int("".join(s).replace(".", "0").replace("#", "1"), 2)
            new_img[i, j] = alg[num]
    return new_img


def p1(f):
    alg, img = f.read().split("\n\n")
    img = {(i, j): x for i, row in enumerate(img.splitlines()) for j, x in enumerate(row)}
    img = defaultdict(lambda: ".", img)
    img = defaultdict(lambda: alg[0], enhance(alg, img))
    img = defaultdict(lambda: ".", enhance(alg, img))
    return sum(x == "#" for x in img.values())


def p2(f):
    alg, img = f.read().split("\n\n")
    img = {(i, j): x for i, row in enumerate(img.splitlines()) for j, x in enumerate(row)}
    img = defaultdict(lambda: ".", img)
    for _ in range(25):
        img = defaultdict(lambda: alg[0], enhance(alg, img))
        img = defaultdict(lambda: ".", enhance(alg, img))
    return sum(x == "#" for x in img.values())
