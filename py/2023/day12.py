# Day       Time  Rank  Score       Time  Rank  Score
#  12   00:05:36    27     74   00:59:17  1070      0

from functools import cache
from itertools import combinations


def p1(f):
    ans = 0

    for line in f:
        chars, nums = line.split()
        nums = [int(x) for x in nums.split(",")]
        questions = [i for i, c in enumerate(chars) if c == "?"]

        for comb in combinations(questions, sum(nums) - chars.count("#")):
            a = "".join("#" if i in comb else c for i, c in enumerate(chars))
            lst = [len(t) for t in a.replace("?", ".").split(".") if t]
            if nums == lst:
                ans += 1

    return ans


@cache
def dp(chars, nums, *, curr=None):
    if len(nums) == 0 and curr is None:
        return "#" not in chars

    match chars[:1], curr:
        case "", None | 0:
            return len(nums) == 0
        case "", _:
            return 0

        case "?", None:
            return dp(chars[1:], nums) + dp(chars, nums[1:], curr=nums[0])
        case "?", 0:
            return dp(chars[1:], nums)
        case "?", _:
            return dp(chars[1:], nums, curr=curr - 1)

        case "#", None:
            return dp(chars, nums[1:], curr=nums[0])
        case "#", 0:
            return 0
        case "#", _:
            return dp(chars[1:], nums, curr=curr - 1)

        case ".", None | 0:
            return dp(chars[1:], nums)
        case ".", _:
            return 0


def p2(f):
    ans = 0

    for line in f:
        chars, nums = line.split()
        chars = "?".join([chars] * 5)
        nums = tuple(int(x) for x in nums.split(",")) * 5
        ans += dp(chars, nums)

    return ans
