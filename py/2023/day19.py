# Day       Time  Rank  Score       Time  Rank  Score
#  19   00:05:30     6     95   00:41:35   436      0

from collections import deque


def p1(f):
    workflows, instructions = f.read().split("\n\n")
    names = {"A": "A", "R": "R"}
    maps = {}
    for line in workflows.splitlines():
        name, conds = line[:-1].split("{")
        conds = conds.replace(":", " and ").replace(",", " or ")
        maps[name] = conds
        names[name] = name
    ans = 0
    for inst in instructions.splitlines():
        x, m, a, s = [int(x[2:]) for x in inst[1:-1].split(",")]
        at = "in"
        while at not in "AR":
            at = eval(maps[at], names, locals())
        if at == "A":
            ans += x + m + a + s
    return ans


class Thing:
    def __init__(self, name, range=None):
        self.name = name
        self.range = range

    def __lt__(self, other):
        return Thing(self.name, range(1, other))

    def __gt__(self, other):
        return Thing(self.name, range(other + 1, 4001))


def split_range(a, b):
    sect = range(max(a.start, b.start), min(a.stop, b.stop))
    left = range(a.start, sect.start)
    right = range(sect.stop, a.stop)
    return left, sect, right


def p2(f):
    global x, m, a, s
    workflows, _ = f.read().split("\n\n")
    names = {"A": "A", "R": "R"}
    for line in workflows.splitlines():
        name, conds = line.split("{")
        names[name] = name

    maps = {}
    for line in workflows.splitlines():
        name, conds = line.split("{")
        x, m, a, s = Thing("x"), Thing("m"), Thing("a"), Thing("s")
        conds = "{" + ",None:".join(conds.rsplit(",", 1))
        maps[name] = eval(conds, globals(), names)

    q = deque()
    q.append(("in", *[range(1, 4001) for _ in range(4)]))
    ans = 0

    while q:
        at, x, m, a, s = q.popleft()
        if at == "R":
            continue
        if at == "A":
            ans += len(x) * len(m) * len(a) * len(s)
            continue
        for k, v in maps[at].items():
            if k is None:
                q.append((v, x, m, a, s))
                continue
            left, sect, right = split_range(eval(k.name), k.range)
            assert not (left and right)
            exec(f"global {k.name}; {k.name} = sect")
            q.append((v, x, m, a, s))
            exec(f"global {k.name}; {k.name} = left or right")
    return ans
