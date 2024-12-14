# Day       Time   Rank  Score       Time   Rank  Score
#  14   00:05:55    227      0   04:19:44   9363      0

from itertools import count
import re
from collections import Counter
from math import prod


WIDTH = 101
HEIGHT = 103

# WIDTH = 11
# HEIGHT = 7


def p1(f):
    things = [
        [int(x) for x in re.findall(r"-?\d+", line)] for line in f.read().splitlines()
    ]
    count = Counter()

    for x, y, dx, dy in things:
        x += dx * 100
        y += dy * 100
        x %= WIDTH
        y %= HEIGHT
        if x != WIDTH // 2 and y != HEIGHT // 2:
            count[x < WIDTH // 2, y < HEIGHT // 2] += 1

    return prod(count.values())


def p2(f):
    things = [
        [int(x) for x in re.findall(r"-?\d+", line)] for line in f.read().splitlines()
    ]

    for t in count(1):
        things = [
            ((x + dx) % WIDTH, (y + dy) % HEIGHT, dx, dy) for x, y, dx, dy in things
        ]
        things2 = {(x, y) for x, y, dx, dy in things}
        if len(things) == len(things2):
            for y in range(HEIGHT):
                for x in range(WIDTH):
                    if (x, y) in things2:
                        print("#", end="")
                    else:
                        print(".", end="")
                print()
            return t
