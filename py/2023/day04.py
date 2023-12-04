# Day       Time  Rank  Score       Time  Rank  Score
#   4   00:02:44    83     18   00:10:55   469      0


from collections import defaultdict


def p1(f):
    ans = 0
    for line in f:
        _, line = line.split(": ")
        wins, nums = map(str.split, line.split(" | "))
        count = sum(nums.count(w) for w in wins)
        if count > 0:
            ans += 2 ** (count - 1)
    return ans


def p2(f):
    cards = defaultdict(int)
    for i, line in enumerate(f):
        _, line = line.split(": ")
        wins, nums = map(str.split, line.split(" | "))
        count = sum(nums.count(w) for w in wins)
        cards[i] += 1
        for j in range(i + 1, i + count + 1):
            cards[j] += cards[i]
    return sum(cards.values())
