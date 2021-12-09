"""
Way faster solution compared to the brute force I originally did.

On my computer, ~11.5 ms compared to ~740 ms.
"""

import itertools

LETTERS = "abcdefg"
LETTER_TO_DIGIT = {x: i for i, x in enumerate(LETTERS)}
WORDS = ["abcefg", "cf", "acdeg", "acdfg", "bcdf", "abdfg", "abdefg", "acf", "abcdefg", "abcdfg"]
WORDS = [frozenset(w) for w in WORDS]
WORD_TO_DISPLAY = {w: i for i, w in enumerate(WORDS)}
UNIQUE = {2: 1, 4: 4, 3: 7, 7: 8}


def p2(f):
    ans = 0

    for line in f:
        nums = [frozenset(LETTER_TO_DIGIT[i] for i in w) for w in line.replace("|", "").split()]
        known = [set(LETTERS) for _ in range(7)]

        def update_known(num, word):
            for digit in range(7):
                op = set.intersection if digit in num else set.difference
                known[digit] = op(known[digit], word)

        for num in nums:
            if len(num) in UNIQUE:
                update_known(num, WORDS[UNIQUE[len(num)]])

        try:
            found = set()
            while True:
                digit = next(d for d, p in enumerate(known) if len(p) == 1 and d not in found)
                update_known({digit}, known[digit])
                found.add(digit)
        except StopIteration:
            pass

        for translation in itertools.product(*known):
            if len(set((translation))) != 7:
                continue

            translated_nums = [frozenset({translation[i] for i in num}) for num in nums]
            if all(word in WORD_TO_DISPLAY for word in translated_nums):
                for i, word in enumerate(translated_nums[-4:][::-1]):
                    ans += WORD_TO_DISPLAY[word] * 10 ** i
                break

    return ans
