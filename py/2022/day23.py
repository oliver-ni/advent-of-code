from collections import Counter, deque
from itertools import count, product

DIRECTIONS = set(product(range(-1, 2), repeat=2)) - {(0, 0)}
ORTHOGONAL = [(-1, 0), (1, 0), (0, -1), (0, 1)]
CHECKS = {p: [d for d in DIRECTIONS if all(px in (0, dx) for px, dx in zip(p, d))] for p in ORTHOGONAL}


def add_tuple(a, b):
    return tuple(x + y for x, y in zip(a, b))


def ground_tiles(elves):
    xs, ys = zip(*elves)
    return sum((i, j) not in elves for i in range(min(xs), max(xs) + 1) for j in range(min(ys), max(ys) + 1))


def p1(f):
    elves = {(i, j) for i, row in enumerate(f) for j, cell in enumerate(row) if cell == "#"}
    props = deque(ORTHOGONAL)

    for _ in range(10):
        moves = {}

        for elf in elves:
            if not any(add_tuple(elf, d) in elves for d in DIRECTIONS):
                continue

            for p in props:
                if any(add_tuple(elf, c) in elves for c in CHECKS[p]):
                    continue
                moves[elf] = add_tuple(elf, p)
                break

        for old, new in moves.items():
            elves.remove(old)
            elves.add(new)

        props.rotate(-1)

    return ground_tiles(elves)


def p2(f):
    elves = {(i, j) for i, row in enumerate(f) for j, cell in enumerate(row) if cell == "#"}
    props = deque(ORTHOGONAL)

    for t in count():
        changed = False
        moves = {}

        for elf in elves:
            if not any(add_tuple(elf, d) in elves for d in DIRECTIONS):
                continue

            for p in props:
                if any(add_tuple(elf, c) in elves for c in CHECKS[p]):
                    continue
                moves[elf] = add_tuple(elf, p)
                break

        move_locs = Counter(moves.values())

        for old, new in moves.items():
            if move_locs[new] > 1:
                continue
            elves.remove(old)
            elves.add(new)
            changed = True

        if not changed:
            return t + 1

        props.rotate(-1)
