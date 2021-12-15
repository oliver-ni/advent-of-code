def p1(f):
    dots, folds = f.read().strip().split("\n\n")
    dots = [eval(x) for x in dots.splitlines()]

    folds = [x.replace("fold along ", "").split("=") for x in folds.strip().splitlines()]
    n = int(folds[0][1])
    dots = {(a if a < n else n - (a - n), b) for a, b in dots}

    return len(dots)


def p2(f):
    dots, folds = f.read().strip().split("\n\n")
    dots = [eval(x) for x in dots.splitlines()]

    folds = [x.replace("fold along ", "").split("=") for x in folds.strip().splitlines()]

    for a, n in folds:
        n = int(n)
        if a == "x":
            dots = {(a if a < n else n - (a - n), b) for a, b in dots}
        else:
            dots = {(a, b if b < n else n - (b - n)) for a, b in dots}

    print()
    for j in range(0, 100):
        for i in range(0, 100):
            if (i, j) in dots:
                print("#", end="")
            else:
                print(" ", end="")
        print()
