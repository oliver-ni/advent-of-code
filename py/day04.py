def p1(f):
    nums = [int(x) for x in f.readline().strip().split(",")]
    boards = [
        [[int(i) for i in l.split()] for l in x.splitlines()]
        for x in f.read().strip().split("\n\n")
    ]

    for num in nums:
        for b in boards:
            for i, row in enumerate(b):
                for j, cell in enumerate(row):
                    if cell == num:
                        b[i][j] = None
            for row in b:
                if all(x is None for x in row):
                    score = sum(i for r in b for i in r if i is not None)
                    return score * num
            for col in zip(*b):
                if all(x is None for x in col):
                    score = sum(i for r in b for i in r if i is not None)
                    return score * num


def p2(f):
    nums = [int(x) for x in f.readline().strip().split(",")]
    boards = [
        [[int(i) for i in l.split()] for l in x.splitlines()]
        for x in f.read().strip().split("\n\n")
    ]

    wins = []
    win = None

    for num in nums:
        if sum(x not in wins for x in boards) == 1:
            win = next(i for i, x in enumerate(boards) if x not in wins)
        for bb, b in enumerate(boards):
            for i, row in enumerate(b):
                for j, cell in enumerate(row):
                    if cell == num:
                        b[i][j] = None
            for row in b:
                if all(x is None for x in row):
                    if bb == win:
                        score = sum(i for r in b for i in r if i is not None)
                        return score * num
                    wins.append(b)
            for col in zip(*b):
                if all(x is None for x in col):
                    if bb == win:
                        score = sum(i for r in b for i in r if i is not None)
                        return score * num
                    wins.append(b)
