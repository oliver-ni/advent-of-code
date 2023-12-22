# Day       Time  Rank  Score       Time  Rank  Score
#  22   00:27:13   206      0   00:29:22    95      6


from itertools import zip_longest


def irange(start, stop):
    if start <= stop:
        return range(start, stop + 1)
    else:
        return range(start, stop - 1, -1)


def draw(a, b):
    i1, j1, k1 = a
    i2, j2, k2 = b
    result = zip_longest(irange(i1, i2), irange(j1, j2), irange(k1, k2))
    return set((a or i1, b or j1, c or k1) for a, b, c in result)


def fall(tiles, brick):
    while True:
        down = {(x, y, z - 1) for x, y, z in brick}
        if any(z == 0 for _, _, z in down) or down & tiles:
            return brick
        brick = down


def p1(f):
    tiles = set()
    bricks = []

    for line in f:
        a, b = [[int(x) for x in r.split(",")] for r in line.split("~")]
        brick = draw(a, b)
        bricks.append(brick)
        tiles |= brick

    bricks.sort(key=lambda p: min(z for _, _, z in p))

    for i, brick in enumerate(bricks):
        tiles -= brick
        bricks[i] = fall(tiles, brick)
        tiles |= bricks[i]

    ans = 0

    for brick in bricks:
        without = tiles - brick
        for other in bricks:
            if other == brick:
                continue
            without -= other
            if fall(without, other) != other:
                break
            without |= other
        else:
            ans += 1

    return ans


def p2(f):
    tiles = set()
    bricks = []

    for line in f:
        a, b = [[int(x) for x in r.split(",")] for r in line.split("~")]
        brick = draw(a, b)
        bricks.append(brick)
        tiles |= brick

    bricks.sort(key=lambda p: min(z for _, _, z in p))

    for i, brick in enumerate(bricks):
        tiles -= brick
        bricks[i] = fall(tiles, brick)
        tiles |= bricks[i]

    ans = 0

    for brick in bricks:
        without = tiles - brick
        for other in bricks:
            if other == brick:
                continue
            without -= other
            if fall(without, other) != other:
                ans += 1
            else:
                without |= other

    return ans
