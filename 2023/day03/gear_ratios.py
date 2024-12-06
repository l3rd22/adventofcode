#!/usr/bin/env python3

import re


def main():
    with open("input.txt", "r") as fobj:
        schematic = fobj.read()
    ncols = schematic.index("\n") + 1
    schematic = f"\n{'.' * (ncols - 1)}\n" + schematic
    total = 0
    gears = {}
    for match in re.finditer(r"\d+", schematic):
        adjacent = "".join(
            schematic[
                slice(
                    match.span()[0] - 1 + offset,
                    match.span()[1] + 1 + offset,
                )
            ]
            for offset in (-ncols, 0, ncols)
        )
        total += int(match[0]) if re.search(r"[^\.\d\n]", adjacent) is not None else 0
        for gear in re.finditer(r"\*", adjacent):
            row, col = divmod(gear.span()[0], len(match[0]) + 2)
            gears.setdefault(match.span()[0] - 1 + col + (row - 1) * ncols, []).append(
                int(match[0])
            )
    print(total)
    print(sum(val[0] * val[1] if len(val) == 2 else 0 for val in gears.values()))


if __name__ == "__main__":
    main()
