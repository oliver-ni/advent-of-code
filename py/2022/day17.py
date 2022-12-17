from itertools import cycle

ROCKS = [
    {0 + 0j, 1 + 0j, 2 + 0j, 3 + 0j},
    {1 + 2j, 0 + 1j, 1 + 1j, 2 + 1j, 1 + 0j},
    {2 + 2j, 2 + 1j, 0 + 0j, 1 + 0j, 2 + 0j},
    {0 + 3j, 0 + 2j, 0 + 1j, 0 + 0j},
    {0 + 1j, 1 + 1j, 0 + 0j, 1 + 0j},
]

ROCKS_1 = cycle(ROCKS)
ROCKS_2 = cycle(enumerate(ROCKS))
DIRECTIONS = {">": 1, "<": -1}


def get_max_y(grid):
    return max(int(p.imag) for p in grid)


def p1(f):
    wind = cycle(DIRECTIONS[x] for x in f.read().strip())
    rest = set(x - 1j for x in range(7))

    for i in range(2022):
        start = 2 + (4 + get_max_y(rest)) * 1j
        rock = {start + p for p in next(ROCKS_1)}

        while True:
            w = next(wind)
            new_rock = {p + w for p in rock}
            if not new_rock & rest and all(0 <= p.real <= 6 for p in new_rock):
                rock = new_rock

            new_rock = {p - 1j for p in rock}
            if rest & new_rock:
                rest.update(rock)
                break

            rock = new_rock

    return get_max_y(rest) + 1


def p2(f):
    wind = cycle(enumerate(DIRECTIONS[x] for x in f.read().strip()))
    rest = set(x - 1j for x in range(7))
    last = {}
    t = 1000000000000

    while t > 0:
        max_y = get_max_y(rest)
        start = 2 + (4 + max_y) * 1j
        r_idx, rock = next(ROCKS_2)
        rock = {start + p for p in rock}

        while True:
            w_idx, w = next(wind)
            new_rock = {p + w for p in rock}
            if not new_rock & rest and all(0 <= p.real <= 6 for p in new_rock):
                rock = new_rock

            new_rock = {p - 1j for p in rock}
            if rest & new_rock:
                rest.update(rock)
                break

            rock = new_rock

        max_y = get_max_y(rest)
        heights = tuple(max_y - get_max_y(p for p in rest if p.real == i) for i in range(7))
        t -= 1

        try:
            old_t, old_max_y = last[r_idx, w_idx, heights]
            rest = {p + t // (old_t - t) * (max_y - old_max_y) * 1j for p in rest}
            t %= old_t - t
        except KeyError:
            last[r_idx, w_idx, heights] = t, max_y

    return get_max_y(rest) + 1
