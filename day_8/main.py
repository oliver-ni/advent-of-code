import itertools


def p1(f):
    return sum(len(word) in {2, 3, 4, 7} for line in f for word in line.split()[-4:])


def p2(f):
    LETTERS = "abcdefg"
    NUMS = ["abcefg", "cf", "acdeg", "acdfg", "bcdf", "abdfg", "abdefg", "acf", "abcdefg", "abcdfg"]
    NUMS = {frozenset(x): i for i, x in enumerate(NUMS)}

    ans = 0
    for line in f:
        a, b = [x.split() for x in line.split(" | ")]
        for perm in itertools.permutations(LETTERS):
            translation = {x: LETTERS[i] for i, x in enumerate(perm)}
            if all(frozenset(translation[i] for i in w) in NUMS for w in a + b):
                for idx, w in enumerate(b[::-1]):
                    ans += NUMS[frozenset(translation[i] for i in w)] * 10 ** idx
                break

    return ans
