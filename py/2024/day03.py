# Day       Time  Rank  Score       Time  Rank  Score
# 3   00:01:03    55     46   00:03:37   120      0

import re


def p1(f):
    matches = re.findall(r"mul\((\d+),(\d+)\)", f.read())
    return sum(int(x) * int(y) for x, y in matches)


def p2(f):
    matches = re.findall(r"mul\((\d+),(\d+)\)|(don't\(\))|(do\(\))", f.read())
    on = True
    ans = 0
    for a, b, c, d in matches:
        if c == "don't()":
            on = False
        elif d == "do()":
            on = True
        elif on:
            ans += int(a) * int(b)
    return ans
