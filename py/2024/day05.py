# Day       Time   Rank  Score       Time   Rank  Score
#   5   00:02:14    122      0   00:04:12    122      0

from functools import cmp_to_key


def p1(f):
    os, ls = [x.splitlines() for x in f.read().split("\n\n")]
    os = [[int(x) for x in o.split("|")] for o in os]
    ls = [[int(x) for x in o.split(",")] for o in ls]
    ans = 0
    for nums in ls:
        for x, y in os:
            try:
                if nums.index(x) >= nums.index(y):
                    break
            except ValueError:
                pass
        else:
            ans += nums[len(nums) // 2]
    return ans


def p2(f):
    os, ls = [x.splitlines() for x in f.read().split("\n\n")]
    os = [[int(x) for x in o.split("|")] for o in os]
    ls = [[int(x) for x in o.split(",")] for o in ls]
    ans = 0
    for nums in ls:
        for x, y in os:
            try:
                if nums.index(x) >= nums.index(y):
                    break
            except ValueError:
                pass
        else:
            continue
        nums.sort(key=cmp_to_key(lambda x, y: -([x, y] in os) + ([y, x] in os)))
        ans += nums[len(nums) // 2]
    return ans
