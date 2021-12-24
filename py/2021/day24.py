from sympy import Add, Eq, Symbol, linsolve, solve, symbols


def solve(sections):
    w = symbols("w:14")
    z = []

    eqns = []

    for i, x in enumerate(sections):
        a, b, c = [int(x[i].split()[-1]) for i in (3, 4, 14)]
        if a == 26:
            eqns.append(Eq(z.pop(), w[i] - b))
        else:
            z.append(w[i] + c)

    return next(iter(linsolve(eqns, w[::-1])))[::-1]


def p1(f):
    sections = [x.strip().splitlines() for x in f.read().split("inp w")][1:]
    sol = solve(sections)
    subs = {}

    for var in sol:
        if not isinstance(var, Symbol):
            continue
        for val in range(9, 0, -1):
            result = [other.subs({**subs, var: val}) for other in sol]
            if all(isinstance(x, (Symbol, Add)) or 1 <= x <= 9 for x in result):
                subs[var] = val
                break

    print("".join(str(var.subs(subs)) for var in sol))


def p2(f):
    sections = [x.strip().splitlines() for x in f.read().split("inp w")][1:]
    sol = solve(sections)
    subs = {}

    for var in sol:
        if not isinstance(var, Symbol):
            continue
        for val in range(1, 10):
            result = [other.subs({**subs, var: val}) for other in sol]
            if all(isinstance(x, (Symbol, Add)) or 1 <= x <= 9 for x in result):
                subs[var] = val
                break

    print("".join(str(var.subs(subs)) for var in sol))
