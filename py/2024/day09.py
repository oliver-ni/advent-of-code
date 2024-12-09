# Day       Time   Rank  Score       Time   Rank  Score
#   9   00:13:56    930      0   00:27:33    501      0

from heapq import heappush, heappop
from itertools import batched
from operator import attrgetter

key = attrgetter("start")


def p1(f):
    line = map(int, f.read().strip() + "0")
    blocks = {}
    free_blocks = []
    next_idx = 0

    for i, (filled, free) in enumerate(batched(line, 2)):
        for j in range(next_idx, next_idx + filled):
            blocks[j] = i
        next_idx += filled
        for j in range(next_idx, next_idx + free):
            heappush(free_blocks, j)
        next_idx += free

    for i in list(blocks.keys())[::-1]:
        if free_blocks[0] >= i:
            break
        x = heappop(free_blocks)
        blocks[x] = blocks.pop(i)
        heappush(free_blocks, i)

    return sum(k * v for k, v in blocks.items())


def p2(f):
    line = map(int, f.read().strip() + "0")
    files = []
    free_blocks = set()
    next_idx = 0

    for i, (filled, free) in enumerate(batched(line, 2)):
        files.append((range(next_idx, next_idx + filled), i))
        next_idx += filled
        free_blocks.add(range(next_idx, next_idx + free))
        next_idx += free

    new_files = []

    for rng, fid in files[::-1]:
        new = min((x for x in free_blocks if len(x) >= len(rng)), key=key, default=rng)
        if new.start >= rng.start:
            new_files.append((rng, fid))
            continue
        free_blocks.remove(new)
        free_blocks.add(rng)
        free_blocks.add(range(new.start + len(rng), new.stop))
        new_files.append((range(new.start, new.start + len(rng)), fid))

    return sum(sum(rng) * fid for rng, fid in new_files)
