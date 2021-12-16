import itertools
import math
from collections import *
from heapq import *


def p1(f):
    packet = str(bin(int(f.read().strip(), 16))[2:])
    total_version = 0

    def parse(start):
        nonlocal total_version
        version = int(packet[start : start + 3], 2)
        type_id = int(packet[start + 3 : start + 6], 2)
        total_version += version
        if type_id == 4:
            num = 0
            idx = start + 6
            while True:
                num <<= 4
                num += int(packet[idx + 1 : idx + 5], 2)
                if int(packet[idx : idx + 1], 2) != 1:
                    idx += 5
                    break
                idx += 5
            return idx
        else:
            length_type_id = int(packet[start + 6 : start + 7], 2)
            if length_type_id == 0:
                total_len = int(packet[start + 7 : start + 22], 2)
                idx = start + 22
                while idx < start + 22 + total_len:
                    idx = parse(idx)
            elif length_type_id == 1:
                num_subpackets = int(packet[start + 7 : start + 18], 2)
                idx = start + 18
                for i in range(num_subpackets):
                    idx = parse(idx)
            return idx

    parse(0)
    return total_version


def p2(f):
    packet = str(bin(int(f.read().strip(), 16))[2:])

    def parse(start):
        version = int(packet[start : start + 3], 2)
        type_id = int(packet[start + 3 : start + 6], 2)
        if type_id == 4:
            num = 0
            idx = start + 6
            while True:
                num <<= 4
                num += int(packet[idx + 1 : idx + 5], 2)
                if int(packet[idx : idx + 1], 2) != 1:
                    idx += 5
                    break
                idx += 5
            return idx, num
        else:
            length_type_id = int(packet[start + 6 : start + 7], 2)
            nums = []
            if length_type_id == 0:
                total_len = int(packet[start + 7 : start + 22], 2)
                idx = start + 22
                while idx < start + 22 + total_len:
                    idx, num = parse(idx)
                    nums.append(num)
            elif length_type_id == 1:
                num_subpackets = int(packet[start + 7 : start + 18], 2)
                idx = start + 18
                for i in range(num_subpackets):
                    idx, num = parse(idx)
                    nums.append(num)
            if type_id == 0:
                return idx, sum(nums)
            elif type_id == 1:
                return idx, math.prod(nums)
            elif type_id == 2:
                return idx, min(nums)
            elif type_id == 3:
                return idx, max(nums)
            elif type_id == 5:
                return idx, 1 if nums[0] > nums[1] else 0
            elif type_id == 6:
                return idx, 1 if nums[0] < nums[1] else 0
            elif type_id == 7:
                return idx, 1 if nums[0] == nums[1] else 0

    return parse(0)[1]
