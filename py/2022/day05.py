import re
from collections import deque


def p1(f):
    crates, instructions = f.read().split("\n\n")
    stacks = []

    for line in crates.splitlines():
        for i, idx in enumerate(range(1, len(line), 4)):
            while i >= len(stacks):
                stacks.append(deque())
            if line[idx] != " ":
                stacks[i].append(line[idx])

    for inst in instructions.splitlines():
        a, b, c = map(int, re.findall(r"\d+", inst))
        for i in range(a):
            stacks[c - 1].appendleft(stacks[b - 1].popleft())

    return "".join(x[0] for x in stacks)


def p2(f):
    crates, instructions = f.read().split("\n\n")
    stacks = []

    for line in crates.splitlines():
        for i, idx in enumerate(range(1, len(line), 4)):
            while i >= len(stacks):
                stacks.append(deque())
            if line[idx] != " ":
                stacks[i].append(line[idx])

    for inst in instructions.splitlines():
        a, b, c = map(int, re.findall(r"\d+", inst))
        temp = deque()
        for i in range(a):
            temp.appendleft(stacks[b - 1].popleft())
        stacks[c - 1].extendleft(temp)

    return "".join(x[0] for x in stacks)
