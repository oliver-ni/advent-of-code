# Day       Time  Rank  Score       Time  Rank  Score
#  11   00:23:23   848      0   00:26:46   394      0


from collections import defaultdict
from math import prod


def parse_monkey(lines):
    return {
        "items": [int(x) for x in lines[1][18:].split(",")],
        "op": lambda old: eval(lines[2][19:]),
        "test": lambda x: x % int(lines[3][21:]) == 0,
        "testnum": int(lines[3][21:]),
        "throw": {
            True: int(lines[4][29:]),
            False: int(lines[5][30:]),
        },
    }


def p1(f):
    monkeys = [parse_monkey(m.splitlines()) for m in f.read().split("\n\n")]
    active = defaultdict(int)

    for r in range(20):
        for i, m in enumerate(monkeys):
            for item in m["items"]:
                active[i] += 1
                new = m["op"](item) // 3
                test = m["test"](new)
                throw = m["throw"][test]
                monkeys[throw]["items"].append(new)
            m["items"] = []

    a = sorted(active.values(), reverse=True)
    return a[0] * a[1]


def p2(f):
    monkeys = [parse_monkey(m.splitlines()) for m in f.read().split("\n\n")]
    active = defaultdict(int)
    mod = prod(m["testnum"] for m in monkeys)

    for r in range(10000):
        for i, m in enumerate(monkeys):
            for item in m["items"]:
                active[i] += 1
                new = m["op"](item) % mod
                test = m["test"](new)
                throw = m["throw"][test]
                monkeys[throw]["items"].append(new)
            m["items"] = []

    a = sorted(active.values(), reverse=True)
    return a[0] * a[1]
