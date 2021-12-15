def adj(i, j):
    return (
        (i - 1, j),
        (i + 1, j),
        (i, j - 1),
        (i, j + 1),
        (i - 1, j - 1),
        (i - 1, j + 1),
        (i + 1, j - 1),
        (i + 1, j + 1),
    )


def p1(f):
    nums = {(i, j): int(x) for i, line in enumerate(f) for j, x in enumerate(line.strip())}

    def dfs(p, t, visited):
        if p in visited or nums[p] + t <= 9:
            return
        visited.add(p)
        for q in adj(*p):
            if q in nums:
                nums[q] += 1
                dfs(q, t, visited)

    def process(t):
        visited = set()
        for p in nums:
            dfs(p, t, visited)
        for p in visited:
            nums[p] = -t
        return len(visited)

    return sum(process(t) for t in range(1, 101))


def p2(f):
    nums = {(i, j): int(x) for i, line in enumerate(f) for j, x in enumerate(line.strip())}

    def dfs(p, t, visited):
        if p in visited or nums[p] + t <= 9:
            return
        visited.add(p)
        for q in adj(*p):
            if q in nums:
                nums[q] += 1
                dfs(q, t, visited)

    def process(t):
        visited = set()
        for p in nums:
            dfs(p, t, visited)
        for p in visited:
            nums[p] = -t
        return len(visited)

    return next(t for t in range(1, 10 ** 10) if process(t) == len(nums))
