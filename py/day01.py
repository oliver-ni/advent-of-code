def p1(f):
    nums = [int(x) for x in f]
    return sum(b > a for a, b in zip(nums, nums[1:]))


def p2(f):
    nums = [int(x) for x in f]
    return sum(b > a for a, b in zip(nums, nums[3:]))
