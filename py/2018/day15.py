from __future__ import annotations

import itertools
import math
from collections import defaultdict, deque

from common.bidict import Bidict


class ElfDeath(Exception):
    pass


class Unit:
    def __init__(self, team: str, board: Board, *, ap: int = 3, hp: int = 200):
        self.team = team
        self.board = board
        self.ap = ap
        self.hp = hp

    @property
    def pos(self):
        return self.board.units[self]


class Board:
    def __init__(
        self,
        num_rows: int,
        num_cols: int,
        walls: set[tuple[int, int]],
        units: Bidict[Unit, tuple[int, int]],
    ):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.walls = walls
        self.units = units

    @classmethod
    def from_str(cls, val: str, elf_ap: int = 3):
        lines = val.strip().splitlines()
        board = cls(len(lines), len(lines[0]), set(), Bidict())
        for r, row in enumerate(lines):
            for c, cell in enumerate(row):
                if cell == "#":
                    board.walls.add((r, c))
                elif cell == "E":
                    board.units[Unit("E", board, ap=elf_ap)] = (r, c)
                elif cell == "G":
                    board.units[Unit("G", board)] = (r, c)
        return board

    def adj(self, r: int, c: int):
        return (r - 1, c), (r, c - 1), (r, c + 1), (r + 1, c)

    def find_nearest(self, source: Unit):
        targets = {x for x in self.units if x.team != source.team}
        if len(targets) == 0:
            return None

        bfs = deque([source.pos])
        dist = defaultdict(lambda: math.inf, {source.pos: 0})
        prev = {}
        visited = set()
        reached = set()
        reached_dist = math.inf

        while len(bfs) > 0 and dist[bfs[0]] <= reached_dist:
            p = bfs.popleft()
            if p in visited or p in self.walls:
                continue
            visited.add(p)

            if p in self.units.reverse and p != source.pos:
                if self.units.reverse[p] in targets:
                    reached_dist = dist[p]
                    reached.add(self.units.reverse[p])
                continue

            for q in self.adj(*p):
                if dist[p] + 1 < dist[q]:
                    dist[q] = dist[p] + 1
                    prev[q] = p
                    bfs.append(q)

        if len(reached) == 0:
            return [], None

        target = min(reached, key=lambda u: (dist[prev[u.pos]], prev[u.pos], u.hp, u.pos))
        pos = target.pos
        path = []
        while pos is not None:
            path.append(pos)
            pos = prev.get(pos)

        return path[::-1], target

    def move(self, unit: Unit, raise_on_elf_death: bool = False):
        try:
            path, target = self.find_nearest(unit)
        except TypeError:
            return False

        if len(path) > 2:
            self.units[unit] = path[1]

        if len(path) <= 3 and target:
            target.hp -= unit.ap
            if target.hp <= 0:
                del self.units[target]
                if raise_on_elf_death and target.team == "E":
                    raise ElfDeath

        return True

    def run_round(self, raise_on_elf_death: bool = False):
        units = sorted(self.units, key=lambda u: self.units[u])
        for unit in units:
            if unit not in self.units:
                continue
            if not self.move(unit, raise_on_elf_death):
                return False
        return True

    def run_game(self, *, raise_on_elf_death: bool = False):
        for i in itertools.count():
            if not self.run_round(raise_on_elf_death):
                return i * sum(x.hp for x in self.units)


def p1(f):
    board = Board.from_str(f.read())
    return board.run_game()


def p2(f):
    raw = f.read()
    for ap in itertools.count(4):
        board = Board.from_str(raw, elf_ap=ap)
        try:
            return board.run_game(raise_on_elf_death=True)
        except ElfDeath:
            pass
