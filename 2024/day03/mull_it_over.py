#!/usr/bin/env python3

import re
import numpy as np


def main():
    with open("input.txt", "r") as fobj:
        memory = fobj.read()
    multipliers = np.array(
        [
            list(map(int, mul))
            for mul in re.findall("mul\((\d{1,3}),(\d{1,3})\)", memory)
        ]
    )
    print(np.sum(multipliers[:, 0] * multipliers[:, 1]))

    enabled_memory = " ".join(
        [
            "do()".join(block.split("do()")[1:])
            for block in ("do()" + memory).split("don't()")
        ]
    )
    multipliers = np.array(
        [
            list(map(int, mul))
            for mul in re.findall("mul\((\d{1,3}),(\d{1,3})\)", enabled_memory)
        ]
    )
    print(np.sum(multipliers[:, 0] * multipliers[:, 1]))


if __name__ == "__main__":
    main()
