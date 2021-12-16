from __future__ import annotations

import math
from typing import NamedTuple


class BitView:
    def __init__(self, data: int):
        self.data = data
        self.size = (self.data.bit_length() + 3) // 4 * 4
        self.cursor = 0

    def __rshift__(self, n):
        self.cursor += n
        return (self.data >> (self.size - self.cursor)) & ((1 << n) - 1)


class Packet(NamedTuple):
    version: int
    value: int
    subpackets: list[Packet]


def parse(view: BitView):
    version = view >> 3
    type_id = view >> 3
    subpackets: list[Packet] = []

    if type_id == 4:
        value = 0
        while True:
            prefix = view >> 1
            value <<= 4
            value += view >> 4
            if prefix == 0:
                break

    else:
        length_type_id = view >> 1

        if length_type_id == 0:
            total_len = view >> 15
            end = view.cursor + total_len
            while view.cursor < end:
                subpackets.append(parse(view))
        elif length_type_id == 1:
            num_subpackets = view >> 11
            for _ in range(num_subpackets):
                subpackets.append(parse(view))

        if type_id == 0:
            value = sum(x.value for x in subpackets)
        if type_id == 1:
            value = math.prod(x.value for x in subpackets)
        if type_id == 2:
            value = min(x.value for x in subpackets)
        if type_id == 3:
            value = max(x.value for x in subpackets)
        if type_id == 5:
            value = 1 if subpackets[0].value > subpackets[1].value else 0
        if type_id == 6:
            value = 1 if subpackets[0].value < subpackets[1].value else 0
        if type_id == 7:
            value = 1 if subpackets[0].value == subpackets[1].value else 0

    return Packet(version, value, subpackets)


def p1(f):
    packet = int(f.read().strip(), 16)
    view = BitView(packet)

    def sum_versions(packet: Packet):
        version = packet.version
        for subpacket in packet.subpackets:
            version += sum_versions(subpacket)
        return version

    return sum_versions(parse(view))


def p2(f):
    packet = int(f.read().strip(), 16)
    view = BitView(packet)
    return parse(view).value
