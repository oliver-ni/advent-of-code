# Day       Time  Rank  Score       Time  Rank  Score
#  21   00:09:31   695      0   00:15:29    85     16


from operator import add, mul, sub, truediv

flip = lambda f: lambda *a: f(*reversed(a))

OPERATIONS = {
    "+": (add, sub, sub),
    "-": (sub, add, flip(sub)),
    "*": (mul, truediv, truediv),
    "/": (truediv, mul, flip(truediv)),
}


def parse(f):
    vals = {}
    for line in f:
        name, eq = line.split(": ")
        match eq.split():
            case [num]:
                vals[name] = int(num)
            case [a, op, b]:
                vals[name] = a, b, *OPERATIONS[op]
    return vals


def calc(vals, i):
    match vals[i]:
        case a, b, f, _, _:
            av, bv = calc(vals, a), calc(vals, b)
            if None in (av, bv):
                return None
            return f(av, bv)
        case _:
            return vals[i]


def p1(f):
    vals = parse(f)
    return int(calc(vals, "root"))


def p2(f):
    vals = parse(f)
    vals["humn"] = None
    vals["root"] = *vals["root"][:2], *OPERATIONS["-"]

    def solve(i, val):
        match vals[i]:
            case a, b, _, fa, fb:
                match calc(vals, a), calc(vals, b):
                    case av, None:
                        return solve(b, fb(val, av))
                    case None, bv:
                        return solve(a, fa(val, bv))
            case None:
                return val

    return int(solve("root", 0))
