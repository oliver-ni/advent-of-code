# Day       Time  Rank  Score       Time  Rank  Score
#   2   00:03:09    34     67   00:04:02    14     87


def p1(f):
    ans = 0
    for line in f:
        id, game = line.split(": ")
        for set in game.split("; "):
            colors = [x.split() for x in set.split(", ")]
            counts = {b: int(a) for a, b in colors}
            if not (counts.get("red", 0) <= 12 and counts.get("green", 0) <= 13 and counts.get("blue", 0) <= 14):
                break
        else:
            ans += int(id.split()[-1])
    return ans


def p2(f):
    ans = 0
    for line in f:
        id, game = line.split(": ")
        needed = {"red": 0, "green": 0, "blue": 0}
        for set in game.split("; "):
            colors = [x.split() for x in set.split(", ")]
            counts = {b: int(a) for a, b in colors}
            needed["red"] = max(needed["red"], counts.get("red", 0))
            needed["green"] = max(needed["green"], counts.get("green", 0))
            needed["blue"] = max(needed["blue"], counts.get("blue", 0))
        ans += needed["red"] * needed["green"] * needed["blue"]
    return ans
