import functools
import math


class Thing(tuple):
    def put(self, i, val):
        return Thing((*self[:i], val, *self[i + 1 :]))

    @classmethod
    def from_rooms(cls, a, b, c, d):
        return cls((None, None, a, None, b, None, c, None, d, None, None))


FINAL = Thing((None, None, (0, 0), None, (1, 1), None, (2, 2), None, (3, 3), None, None))
HALLS = 0, 1, 3, 5, 7, 9, 10
ROOMS = 2, 4, 6, 8
LETTERS = "ABCD"


def trange(a: int, b: int):
    if b >= a:
        return range(a + 1, b + 1)
    else:
        return range(a - 1, b - 1, -1)


@functools.cache
def final(room_size: int):
    return Thing.from_rooms(*[(i,) * room_size for i in range(4)])


@functools.cache
def search(spaces: Thing, room_size: int):
    if spaces == final(room_size):
        return 0

    ans = math.inf

    for hi in HALLS:
        if (bug := spaces[hi]) is not None:
            ri = ROOMS[bug]
            room = spaces[ri]
            if all(i in ROOMS or spaces[i] is None for i in trange(hi, ri)):
                if len(room) < room_size and all(x == bug for x in room):
                    new = spaces.put(hi, None).put(ri, (bug, *room))
                    dist = abs(ri - hi) + room_size - len(room)
                    ans = min(ans, search(new, room_size) + dist * 10 ** bug)

    for i, ri in enumerate(ROOMS):
        if not all(x == i for x in spaces[ri]):
            bug = spaces[ri][-1]
            room = spaces[ri][:-1]
            for hi in HALLS:
                if all(i in ROOMS or spaces[i] is None for i in trange(ri, hi)):
                    new = spaces.put(ri, room).put(hi, bug)
                    dist = abs(ri - hi) + room_size - len(room)
                    ans = min(ans, search(new, room_size) + dist * 10 ** bug)

    return ans


def p1(f):
    spaces = Thing.from_rooms((2, 2), (3, 1), (0, 0), (1, 3))
    return search(spaces, 2)


def p2(f):
    spaces = Thing.from_rooms((2, 3, 3, 2), (3, 1, 2, 1), (0, 0, 1, 0), (1, 2, 0, 3))
    return search(spaces, 4)
