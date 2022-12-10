# Day       Time  Rank  Score       Time  Rank  Score
#  10   00:03:53    24     77   00:07:51    13     88


def p1(f):
    X = 1
    t = 0
    signal = 0

    def tick():
        nonlocal signal, t
        t += 1
        if t in (20, 60, 100, 140, 180, 220):
            signal += t * X

    for line in f:
        match line.split():
            case ["addx", num]:
                tick()
                tick()
                X += int(num)
            case ["noop"]:
                tick()

    return signal


def p2(f):
    X = 1
    t = 0

    print()

    def tick():
        nonlocal t
        if t % 40 in (X - 1, X, X + 1):
            print("#", end="")
        else:
            print(".", end="")
        t += 1
        if t % 40 == 0:
            print()

    for line in f:
        match line.split():
            case ["addx", num]:
                tick()
                tick()
                X += int(num)
            case ["noop"]:
                tick()
