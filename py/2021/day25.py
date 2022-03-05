import itertools


def p1(f):
    lines = list(f)
    size = len(lines)
    size2 = len(lines[0].strip())

    board = {
        (i, j): cell
        for i, row in enumerate(lines)
        for j, cell in enumerate(row.strip())
        if cell in ">v"
    }

    for t in itertools.count():
        nb = {}

        for (i, j), cell in board.items():
            if cell == ">" and (i, nj := (j + 1) % size2) not in board:
                nb[i, nj] = cell
            else:
                nb[i, j] = cell

        nb2 = {}

        for (i, j), cell in nb.items():
            if cell == "v" and (ni := (i + 1) % size, j) not in nb:
                nb2[ni, j] = cell
            else:
                nb2[i, j] = cell

        if nb2 == board:
            return t + 1

        board = nb2
