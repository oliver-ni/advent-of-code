from math import prod


def p1(f):
    grid = f.read().splitlines()
    ans = 0
    for ti, row in enumerate(grid):
        for tj, tree in enumerate(row):
            ans += (
                all(grid[ti][j] < tree for j in range(0, tj))
                or all(grid[ti][j] < tree for j in range(tj + 1, len(row)))
                or all(grid[i][tj] < tree for i in range(0, ti))
                or all(grid[i][tj] < tree for i in range(ti + 1, len(grid)))
            )
    return ans


def p2(f):
    grid = f.read().splitlines()
    ans = []

    for ti, row in enumerate(grid):
        for tj, tree in enumerate(row):
            ans.append([0, 0, 0, 0])

            for j in range(tj - 1, -1, -1):
                ans[-1][0] += 1
                if grid[ti][j] >= tree:
                    break

            for i in range(ti - 1, -1, -1):
                ans[-1][1] += 1
                if grid[i][tj] >= tree:
                    break

            for j in range(tj + 1, len(row)):
                ans[-1][2] += 1
                if grid[ti][j] >= tree:
                    break

            for i in range(ti + 1, len(grid)):
                ans[-1][3] += 1
                if grid[i][tj] >= tree:
                    break

    return max(prod(x) for x in ans)
