# Day       Time  Rank  Score       Time  Rank  Score
#  10   00:17:12   375      0   00:37:33   111      0

from collections import deque


class _(tuple):
    def __add__(self, other):
        return _(x + y for x, y in zip(self, other))

    def __neg__(self):
        return _(-x for x in self)


ADJ = {
    ".": [],
    "|": [(1, 0), (-1, 0)],
    "-": [(0, 1), (0, -1)],
    "L": [(0, 1), (-1, 0)],
    "J": [(0, -1), (-1, 0)],
    "7": [(0, -1), (1, 0)],
    "F": [(0, 1), (1, 0)],
}
ADJ = {k: [_(x) for x in v] for k, v in ADJ.items()}
ALL = ADJ["|"] + ADJ["-"]

EXPANDS = {
    ".": ["...", "...", "..."],
    "|": [".#.", ".#.", ".#."],
    "-": ["...", "###", "..."],
    "L": [".#.", ".##", "..."],
    "J": [".#.", "##.", "..."],
    "7": ["...", "##.", ".#."],
    "F": ["...", ".##", ".#."],
}


def p1(f):
    tiles = {_((i, j)): x for i, l in enumerate(f) for j, x in enumerate(l.strip())}

    s = next(p for p, x in tiles.items() if x == "S")
    s_adj = [dp for dp in ALL if -dp in ADJ[tiles.get(s + dp, ".")]]
    tiles[s] = next(x for x, adj in ADJ.items() if set(adj) == set(s_adj))
    print("S is", tiles[s], end=", ")

    bfs = deque([(s, 0)])
    dists = {}
    while bfs:
        p, d = bfs.popleft()
        if p not in tiles or p in dists:
            continue
        dists[p] = d
        for dp in ADJ[tiles[p]]:
            bfs.append((p + dp, d + 1))

    return max(dists.values())


def p2(f):
    tiles = {_((i, j)): x for i, l in enumerate(f) for j, x in enumerate(l.strip())}

    s = next(p for p, x in tiles.items() if x == "S")
    s_adj = [dp for dp in ALL if -dp in ADJ[tiles.get(s + dp, ".")]]
    tiles[s] = next(x for x, adj in ADJ.items() if set(adj) == set(s_adj))
    print("S is", tiles[s], end=", ")

    bfs = deque([(s, 0)])
    dists = {}
    while bfs:
        p, d = bfs.popleft()
        if p not in tiles or p in dists:
            continue
        dists[p] = d
        for dp in ADJ[tiles[p]]:
            bfs.append((p + dp, d + 1))

    big_tiles = {
        p + p + p + (ei, ej): EXPANDS[x][ei][ej] if p in dists else EXPANDS["."][ei][ej]
        for p, x in tiles.items()
        for ei in range(3)
        for ej in range(3)
    }

    bfs = deque([_((0, 0))])
    seen = set()
    while bfs:
        p = bfs.popleft()
        if p not in big_tiles or p in seen or big_tiles[p] == "#":
            continue
        seen.add(p)
        for dp in ALL:
            bfs.append(p + dp)

    return sum(
        all(p + p + p + (ei, ej) not in seen for ei in range(3) for ej in range(3))
        for p in tiles
    )
