# Day       Time  Rank  Score       Time  Rank  Score
#  14   00:03:05    24     77   00:17:53   114      0


def west(grid):
    for row in grid:
        slot = 0
        for i, c in enumerate(row):
            if c == "#":
                slot = i + 1
            if c == "O":
                row[i] = "."
                row[slot] = "O"
                slot += 1


def transpose(grid):
    return [list(x) for x in zip(*grid)]


def p1(f):
    grid = [list(l.strip()) for l in f]
    grid = transpose(grid)
    west(grid)
    return sum(i + 1 for col in grid for i, c in enumerate(col[::-1]) if c == "O")


def p2(f):
    grid = [list(l.strip()) for l in f]
    states = {}
    i = 0

    while i < 1000000000:
        joined = "\n".join("".join(row) for row in grid)
        if joined in states:
            cycle = i - states[joined]
            i += (1000000000 - i) // cycle * cycle
            if i == 1000000000:
                break
        states[joined] = i

        grid = transpose(grid)
        west(grid)
        grid = transpose(grid)

        west(grid)

        grid = grid[::-1]
        grid = transpose(grid)
        west(grid)
        grid = transpose(grid)
        grid = grid[::-1]

        grid = [row[::-1] for row in grid]
        west(grid)
        grid = [row[::-1] for row in grid]

        i += 1

    grid = transpose(grid)
    return sum(i + 1 for col in grid for i, c in enumerate(col[::-1]) if c == "O")
