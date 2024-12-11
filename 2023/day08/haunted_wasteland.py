#!/usr/bin/env python3

import re
from itertools import cycle


def main():
    with open("input.txt", "r") as fobj:
        instruction = cycle({"L": 0, "R": 1}[d] for d in next(fobj).rstrip())
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


if __name__ == "__main__":
    main()
