# Day       Time  Rank  Score       Time  Rank  Score
#  20   00:19:58    47     54   03:12:30  2533      0

from collections import defaultdict, deque
from math import prod


def p1(f):
    things = {}
    conj_state = defaultdict(dict)
    flip_flop_state = defaultdict(bool)

    for line in f:
        name, dest = line.strip().split(" -> ")
        dest = dest.split(", ")
        things[name[1:]] = name[0], dest
        for y in dest:
            conj_state[y][name[1:]] = False

    counts = defaultdict(int)
    q = deque()

    def send(x, y, high):
        counts[high] += 1
        conj_state[y][x] = high
        q.append((y, high))

    for _ in range(1000):
        send("button", "roadcaster", False)
        while q:
            x, high = q.popleft()
            if x not in things:
                continue
            match things[x]:
                case "b", dest:
                    for y in dest:
                        send(x, y, high)
                case "%", dest if not high:
                    flip_flop_state[x] = not flip_flop_state[x]
                    for y in dest:
                        send(x, y, flip_flop_state[x])
                case "&", dest:
                    pulse = not all(conj_state[x].values())
                    for y in dest:
                        send(x, y, pulse)

    return prod(counts.values())


def p2(f):
    for line in f:
        name, dest = line.strip().split(" -> ")
        dest = dest.split(", ")
        print(name[1:], ":", name)
        for y in dest:
            print(name[1:], "->", y)
    print("rx.style.fill: Yellow")
    print("roadcaster.style.fill: Yellow")

    # got busy with something else, solved by hand after
