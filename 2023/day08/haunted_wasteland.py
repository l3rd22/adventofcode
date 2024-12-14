#!/usr/bin/env python3

import sys
import re
from itertools import cycle
from math import lcm, ceil

sys.path.append("../../")
from utils.math import gcd


def find_cycle(val, func):
    t = func(val)
    h = func(t)
    while t != h:
        t = func(t)
        h = func(func(h))

    idx = 0
    t = val
    while t != h:
        t = func(t)
        h = func(h)
        idx += 1

    len_ = 1
    h = func(t)
    while t != h:
        h = func(h)
        len_ += 1
    return idx, len_


def main():
    with open("input.txt", "r") as fobj:
        first_line = [{"L": 0, "R": 1}[d] for d in next(fobj).rstrip()]
        instruction = cycle(first_line)
        network = {
            m[1]: (m[2], m[3])
            for m in re.finditer(
                r"([A-Z]{3}) = \(([A-Z]{3}), ([A-Z]{3})\)", fobj.read()
            )
        }
    node = "AAA"
    steps = 0
    while node != "ZZZ":
        node = network[node][next(instruction)]
        steps += 1
    print(steps)

    def advance(node, instructions=first_line):
        for i in instructions:
            node = network[node][i]
        return node

    len_instr = len(first_line)
    ghosts = {}
    for s, start in enumerate(n for n in network if n.endswith("A")):
        g = ghosts[s] = {}
        g["mu"], g["lam"] = find_cycle(start, advance)
        g["z"] = []
        for j in range(g["mu"] + g["lam"]):
            for i, instr in enumerate(first_line, j * len_instr + 1):
                if (start := advance(start, [instr])).endswith("Z"):
                    g["z"].append(i)
        g["mu"] *= len_instr
        g["lam"] *= len_instr

    # since every loop only contains one end node at the end of the
    # loop, the results is simply lcm(z_i)
    print(lcm(*(g["z"][0] for g in ghosts.values())))

    # for a more general solution that allows for multiple visited xxZ
    # nodes per cycle and ones before entering the loop
    # first: check if end condition is met before all ghosts enter their
    # cycles
    mu_max = max(g["mu"] for g in ghosts.values())
    for i, g in enumerate(ghosts.values()):
        lead_i = {z for z in g["z"] if z < g["mu"]}
        lead_i |= {
            z + k * g["lam"]
            for z in g["z"]
            if z >= g["mu"]
            for k in range(ceil((mu_max - g["mu"]) / g["lam"]))
        }
        if i == 0:
            leading = lead_i
            continue
        leading &= lead_i
    if leading:
        print(min(leading))
        return
    for i, g in enumerate(ghosts.values()):
        if i == 0:
            zij = [z % g["lam"] for z in g["z"] if z >= g["mu"]]
            lamij = g["lam"]
            muij = g["mu"]
            continue
        gcd_, u, v = gcd(lamij, g["lam"])
        zij = [
            zi * v * (g["lam"] // gcd_) + (zj % g["lam"]) * u * (lamij // gcd_)
            for zi in zij
            for zj in g["z"]
            if zj >= g["mu"]
        ]
        lamij = lcm(lamij, g["lam"])
        muij = max(muij, g["mu"])
        zij = [z % lamij + ceil((muij - (z % lamij)) / lamij) * lamij for z in zij]
    print(min(zij))


if __name__ == "__main__":
    main()
