#!/usr/bin/env python3

import re


def main():
    with open("input.txt", "r") as fobj:
        schematic = fobj.read()
    ncols = schematic.index("\n") + 1
    total = 0
    for match in re.finditer(r"\d+", schematic):
        adjacent = "".join(
            schematic[
                slice(
                    max(match.span()[0] - 1 + offset, 0),
                    max(match.span()[1] + 1 + offset, 0),
                )
            ]
            for offset in (-ncols, 0, ncols)
        )
        total += int(match[0]) if re.search(r"[^\.\d\n]", adjacent) is not None else 0
    print(total)


if __name__ == "__main__":
    main()
