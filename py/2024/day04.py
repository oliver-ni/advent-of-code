# Day       Time   Rank  Score       Time   Rank  Score
#   4   16:05:19  69538      0   16:06:55  61477      0


def p1(f):
    grid = f.read().splitlines()
    N = len(grid)
    ans = 0
    for _ in range(4):
        grid = ["".join(x)[::-1] for x in zip(*grid)]
        diags = [
            "".join(grid[i][ofs + i] for i in range(N) if 0 <= ofs + i < N)
            for ofs in range(-N, N)
        ]
        ans += sum(x.count("XMAS") for x in [*grid, *diags])
    return ans


def p2(f):
    grid = f.read().splitlines()
    N = len(grid)
    ans = 0
    for _ in range(4):
        grid = ["".join(x)[::-1] for x in zip(*grid)]
        for i in range(1, N - 1):
            for j in range(1, N - 1):
                if (
                    grid[i - 1][j - 1] == grid[i - 1][j + 1] == "M"
                    and grid[i][j] == "A"
                    and grid[i + 1][j - 1] == grid[i + 1][j + 1] == "S"
                ):
                    ans += 1
    return ans


# X---
# -X--
# ..X.
# ...X
# ....
# ....
