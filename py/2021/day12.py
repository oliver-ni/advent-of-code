from collections import defaultdict


def p1(f):
    adj = defaultdict(set)

    for line in f:
        a, b = line.strip().split("-")
        adj[a].add(b)
        adj[b].add(a)

    visited = defaultdict(int)

    def dfs(p):
        if p == "end":
            return 1
        visited[p] += 1
        ans = 0
        for q in adj[p]:
            if visited[q] == 0 or q.upper() == q:
                ans += dfs(q)
        visited[p] -= 1
        return ans

    return dfs("start")


def p2(f):
    adj = defaultdict(set)

    for line in f:
        a, b = line.strip().split("-")
        adj[a].add(b)
        adj[b].add(a)

    visited = defaultdict(int)

    def dfs(p, allow):
        if p == "end":
            return 1
        visited[p] += 1
        ans = 0
        for q in adj[p]:
            if q.upper() == q or visited[q] == 0:
                ans += dfs(q, allow)
            elif allow and q != "start":
                ans += dfs(q, False)
        visited[p] -= 1
        return ans

    return dfs("start", True)
