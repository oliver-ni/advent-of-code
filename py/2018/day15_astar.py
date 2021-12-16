import itertools
import math
from collections import defaultdict
from heapq import heappop, heappush

from .day15 import Board, ElfDeath, Unit


class AStarBoard(Board):
    def find_nearest(self, source: Unit):
        targets = {x for x in self.units if x.team != source.team}
        if len(targets) == 0:
            return None

        dist = defaultdict(lambda: math.inf, {source.pos: 0})
        pq = [(0, self.units[source])]
        reached_dist = math.inf
        prev = {}

        while len(pq) > 0:
            _, p = heappop(pq)
            if p in self.walls:
                continue

            if p in self.units.reverse and p != source.pos:
                if self.units.reverse[p] in targets:
                    reached_dist = dist[p]
                continue

            if reached_dist < dist[p]:
                break

            for q in self.adj(*p):
                if dist[p] + 1 < dist[q]:
                    dist[q] = dist[p] + 1
                    prev[q] = p
                    heappush(pq, (dist[q], q))

        reached_targets = {x for x in targets if dist[x.pos] < math.inf}
        if len(reached_targets) == 0:
            return [], None

        target = min(reached_targets, key=lambda u: (dist[prev[u.pos]], prev[u.pos], u.hp, u.pos))
        pos = target.pos
        path = []
        while pos is not None:
            path.append(pos)
            pos = prev.get(pos)

        return path[::-1], target


def p1(f):
    board = AStarBoard.from_str(f.read())
    return board.run_game()


def p2(f):
    raw = f.read()
    for ap in itertools.count(4):
        board = AStarBoard.from_str(raw, elf_ap=ap)
        try:
            return board.run_game(raise_on_elf_death=True)
        except ElfDeath:
            pass
