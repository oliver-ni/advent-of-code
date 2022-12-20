from collections import deque, namedtuple

_ = namedtuple("_", ("id", "val"))


def p1(f):
    nums = deque(_(id, int(x)) for id, x in enumerate(f))
    order = list(nums)

    for x in order:
        idx = next(i for i, y in enumerate(nums) if x.id == y.id)
        nums.rotate(-idx)
        nums.popleft()
        nums.rotate(-x.val)
        nums.appendleft(x)

    nums.rotate(-next(i for i, x in enumerate(nums) if x.val == 0))
    return nums[1000 % len(nums)].val + nums[2000 % len(nums)].val + nums[3000 % len(nums)].val


def p1(f):
    nums = deque(_(id, int(x) * 811589153) for id, x in enumerate(f))
    order = list(nums)

    for t in range(10):
        for x in order:
            idx = next(i for i, y in enumerate(nums) if x.id == y.id)
            nums.rotate(-idx)
            nums.popleft()
            nums.rotate(-x.val)
            nums.appendleft(x)

    nums.rotate(-next(i for i, x in enumerate(nums) if x.val == 0))
    return nums[1000 % len(nums)].val + nums[2000 % len(nums)].val + nums[3000 % len(nums)].val
