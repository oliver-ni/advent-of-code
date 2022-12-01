def p1(f):
    return max(sum(int(i) for i in x.split()) for x in f.read().split("\n\n"))


def p2(f):
    a = [sum(int(i) for i in x.split()) for x in f.read().split("\n\n")]
    ans = max(a)
    a.remove(max(a))
    ans += max(a)
    a.remove(max(a))
    ans += max(a)
    return ans
