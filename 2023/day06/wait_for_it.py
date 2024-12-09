#!/usr/bin/env python3

import re
from math import sqrt, floor, ceil, prod


def main():
    with open("input.txt", "r") as fobj:
        times = list(map(int, re.findall(r"\d+", fobj.readline())))
        distances = list(map(int, re.findall(r"\d+", fobj.readline())))
    print(
        prod(
            floor(t / 2 + sqrt(t**2 / 4 - d - 1e-12))
            - ceil(t / 2 - sqrt(t**2 / 4 - d - 1e-12))
            + 1
            for t, d in zip(times, distances)
        )
    )
    t = int("".join(map(str, times)))
    d = int("".join(map(str, distances)))
    print(
        floor(t / 2 + sqrt(t**2 / 4 - d - 1e-12))
        - ceil(t / 2 - sqrt(t**2 / 4 - d - 1e-12))
        + 1
    )


if __name__ == "__main__":
    main()
