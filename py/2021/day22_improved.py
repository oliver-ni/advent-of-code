from __future__ import annotations

import re
from dataclasses import dataclass, field


@dataclass
class Thing:
    x1: int
    x2: int
    y1: int
    y2: int
    z1: int
    z2: int
    holes: list[Thing] = field(default_factory=list)

    def volume(self):
        vol = (self.x2 - self.x1) * (self.y2 - self.y1) * (self.z2 - self.z1)
        return vol - sum(x.volume() for x in self.holes)

    def __and__(self, cub):
        isect = Thing(
            max(self.x1, cub.x1),
            min(self.x2, cub.x2),
            max(self.y1, cub.y1),
            min(self.y2, cub.y2),
            max(self.z1, cub.z1),
            min(self.z2, cub.z2),
        )
        if isect.x2 > isect.x1 and isect.y2 > isect.y1 and isect.z2 > isect.z1:
            return isect

    def __sub__(self, cub):
        if isect := self & cub:
            for hole in self.holes:
                hole -= cub
            self.holes.append(isect)


def p2(f):
    things = []

    for line in f:
        x1, x2, y1, y2, z1, z2 = [int(x) for x in re.findall(r"-?\d+", line)]
        cub = Thing(x1, x2 + 1, y1, y2 + 1, z1, z2 + 1)

        for other in things:
            other -= cub

        if line.startswith("on"):
            things.append(cub)

    return sum(x.volume() for x in things)
