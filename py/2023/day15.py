# Day       Time  Rank  Score       Time  Rank  Score
#  15   00:01:47    37     64   00:07:06    20     81

from collections import defaultdict


def hash(x):
    val = 0
    for c in x:
        val += ord(c)
        val *= 17
        val %= 256
    return val


def p1(f):
    return sum(map(hash, f.read().strip().split(",")))


def p2(f):
    hashmap = defaultdict(dict)

    for thing in f.read().strip().split(","):
        if "=" in thing:
            label, thing = thing.split("=")
            hashmap[hash(label)][label] = int(thing)
        elif "-" in thing:
            label = thing[:-1]
            hashmap[hash(label)].pop(label, None)

    return sum(
        (1 + i) * (1 + j) * val
        for i, box in hashmap.items()
        for j, val in enumerate(box.values())
    )
