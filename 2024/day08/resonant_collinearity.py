#!/usr/bin/env python3

import re


def out_of_bounds(pos, nrows, ncols):
    return pos[0] < 0 or pos[0] >= nrows or pos[1] < 0 or pos[1] >= ncols


def main():
    with open("input.txt", "r") as fobj:
        map_ = fobj.read()
    ncols = map_.index("\n")
    nrows = map_.count("\n")
    antennae = {}
    for ant in re.finditer(r"[^.\n]", map_):
        antennae.setdefault(ant[0], []).append(divmod(ant.span()[0], ncols + 1))
    antinodes = set()
    for pos in antennae.values():
        for p1 in pos:
            for p2 in pos:
                if p1 == p2:
                    continue
                if not out_of_bounds(
                    an := (2 * p2[0] - p1[0], 2 * p2[1] - p1[1]), nrows, ncols
                ):
                    antinodes.add(an)
    print(len(antinodes))

    for pos in antennae.values():
        for p1 in pos:
            for p2 in pos:
                if p1 == p2:
                    continue
                i = 0
                while not out_of_bounds(
                    an := (p2[0] + i * (p2[0] - p1[0]), p2[1] + i * (p2[1] - p1[1])),
                    nrows,
                    ncols,
                ):
                    antinodes.add(an)
                    i += 1
    print(len(antinodes))


if __name__ == "__main__":
    main()
