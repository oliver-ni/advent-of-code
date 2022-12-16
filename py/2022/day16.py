# Day       Time  Rank  Score       Time  Rank  Score
#  16   01:29:18  1219      0   01:39:21   336      0


import math
import re
from collections import defaultdict
from functools import cache

REGEX = r"^Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? ([\w ,]+)$"


def p1(f):
    valves = {}
    dist = defaultdict(lambda: defaultdict(lambda: math.inf))

    for i, flow_rate, tunnels in re.findall(REGEX, f.read(), re.MULTILINE):
        valves[i] = int(flow_rate)
        dist[i][i] = 0
        for j in tunnels.split(", "):
            dist[i][j] = 1

    for k in valves:
        for i in valves:
            for j in valves:
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    @cache
    def dp(i: str, t: int, remaining: frozenset):
        ans = 0
        for j in remaining:
            if (next_t := t - dist[i][j] - 1) >= 0:
                ans = max(ans, valves[j] * next_t + dp(j, next_t, remaining - {j}))
        return ans

    return dp("AA", 30, frozenset(x for x in valves if valves[x] > 0))


def p2(f):
    valves = {}
    dist = defaultdict(lambda: defaultdict(lambda: math.inf))

    for i, flow_rate, tunnels in re.findall(REGEX, f.read(), re.MULTILINE):
        valves[i] = int(flow_rate)
        dist[i][i] = 0
        for j in tunnels.split(", "):
            dist[i][j] = 1

    for k in valves:
        for i in valves:
            for j in valves:
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    @cache
    def dp(i: str, t: int, remaining: frozenset, elephant: bool):
        ans = dp("AA", 26, remaining, False) if elephant else 0
        for j in remaining:
            if (next_t := t - dist[i][j] - 1) >= 0:
                ans = max(ans, valves[j] * next_t + dp(j, next_t, remaining - {j}, elephant))
        return ans

    return dp("AA", 26, frozenset(x for x in valves if valves[x] > 0), True)
