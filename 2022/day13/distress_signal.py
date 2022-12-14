from functools import cmp_to_key
from math import prod


def cmp(packet_1, packet_2):
    try:
        return (packet_1 > packet_2) - (packet_1 < packet_2)
    except TypeError:
        i, (p1, p2) = next(
            (i, p) for i, p in enumerate(zip(packet_1, packet_2), 1) if p[0] != p[1]
        )
        if type(p1) is int:
            if (res := cmp([p1], p2)) != 0:
                return res
        elif type(p2) is int:
            if (res := cmp(p1, [p2])) != 0:
                return res
        elif (res := cmp(p1, p2)) != 0:
            return res
        return cmp(packet_1[i:], packet_2[i:])


pairs = [
    tuple(map(eval, pair.rstrip("\n").split("\n")))
    for pair in open("input.txt", "r").read().split("\n\n")
]
print(
    sum(
        i
        for i, (packet_1, packet_2) in enumerate(pairs, 1)
        if cmp(packet_1, packet_2) < 1
    )
)
(packets := [packet for pair in pairs for packet in pair]).extend(
    divider_packets := ([[2]], [[6]])
)
print(
    prod(sorted(packets, key=cmp_to_key(cmp)).index(dp) + 1 for dp in divider_packets)
)
