# Day       Time  Rank  Score       Time  Rank  Score
#  25   00:05:08    22     79   00:05:18    23     78


DIGITS = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}
DIGITS_R = {v: k for k, v in DIGITS.items()}


def p1(f):
    total = 0

    for num in f:
        for i, digit in enumerate(num.strip()[::-1]):
            total += DIGITS[digit] * 5**i

    ans = ""

    while total > 0:
        total, digit = divmod(total, 5)
        if digit > 2:
            digit -= 5
            total += 1
        ans += DIGITS_R[digit]

    return ans[::-1]
