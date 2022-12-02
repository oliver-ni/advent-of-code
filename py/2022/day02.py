def p1(f):
    ans = 0

    for line in f:
        a, b = line.split()
        a = "ABC".index(a)
        b = "XYZ".index(b)

        ans += b + 1

        match (b - a) % 3:
            case 1:
                ans += 6
            case 0:
                ans += 3

    return ans


def p2(f):
    ans = 0

    for line in f:
        a, b = line.split()
        a = "ABC".index(a)

        match b:
            case "X":
                ans += (a - 1) % 3 + 1
            case "Y":
                ans += 3
                ans += a + 1
            case "Z":
                ans += 6
                ans += (a + 1) % 3 + 1

    return ans
