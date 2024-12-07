# Day       Time   Rank  Score       Time   Rank  Score
#   7   00:04:43    380      0   00:08:46    573      0


def p1(f):
    lines = [
        [int(x) for x in line.replace(":", "").split(" ")]
        for line in f.read().splitlines()
    ]

    def solve(nums, i, ans):
        if i == 0:
            return nums[0] == ans
        return solve(nums, i - 1, ans / nums[i]) or solve(nums, i - 1, ans - nums[i])

    return sum(nums[0] for nums in lines if solve(nums[1:], len(nums) - 2, nums[0]))


def p2(f):
    lines = [
        [int(x) for x in line.replace(":", "").split(" ")]
        for line in f.read().splitlines()
    ]

    def solve(nums, i, ans):
        if i == 0:
            return nums[0] == ans
        quo, rem = divmod(ans, nums[i])
        s_ans, s_nums_i = str(ans), str(nums[i])
        return (
            (rem == 0 and solve(nums, i - 1, quo))
            or (ans >= nums[i] and solve(nums, i - 1, ans - nums[i]))
            or (
                s_ans.endswith(s_nums_i)
                and solve(nums, i - 1, int("0" + s_ans[: -len(s_nums_i)]))
            )
        )

    return sum(nums[0] for nums in lines if solve(nums[1:], len(nums) - 2, nums[0]))
