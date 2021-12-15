import math
from collections import defaultdict
from heapq import heappop, heappush

from PIL import Image, ImageColor, ImageDraw

GRID_SIZE = 1


def adj(i, j):
    return (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)


def get_color(val):
    if val == math.inf:
        return ImageColor.getrgb("white")
    h = val % 360
    return ImageColor.getrgb(f"hsv({h}, 100%, 100%)")


def p1(f):
    lines = list(f)
    size = len(lines)
    nums = {(i, j): int(x) for i, row in enumerate(lines) for j, x in enumerate(row.strip())}

    dist = defaultdict(lambda: math.inf, {(0, 0): 0})
    pq = [(0, (0, 0))]

    im = Image.new("RGB", (GRID_SIZE * size, GRID_SIZE * size), (255, 255, 255))
    pixels = im.load()
    pixels[0, 0] = get_color(0)

    t = 0
    while len(pq) > 0:
        print(t)
        im.save(f"images/output_{t:010}.png")
        _, p = heappop(pq)
        if p == (size - 1, size - 1):
            break
        for q in adj(*p):
            alt = dist[p] + nums.get(q, math.inf)
            if alt < dist[q]:
                dist[q] = alt
                heappush(pq, (dist[q], q))
                pixels[q] = get_color(dist[q])
        t += 1

    return dist[p]
