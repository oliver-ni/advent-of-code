# Day       Time  Rank  Score       Time  Rank  Score
#   1   00:00:48     8     93   00:04:56    31     70

from math import inf


def p1(f):
    ans = 0
    for line in f:
        first = next(x for x in line if x.isdigit())
        last = next(x for x in line[::-1] if x.isdigit())
        ans += int(first) * 10 + int(last)
    return ans


nums = "0 zero 1 one 2 two 3 three 4 four 5 five 6 six 7 seven 8 eight 9 nine".split()


def p2(f):
    ans = 0
    for line in f:
        first = min(nums, key=lambda x: line.index(x) if x in line else inf)
        last = min(nums, key=lambda x: line[::-1].index(x[::-1]) if x in line else inf)
        ans += nums.index(first) // 2 * 10 + nums.index(last) // 2
    return ans
