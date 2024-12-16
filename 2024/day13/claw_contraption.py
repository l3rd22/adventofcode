#!/usr/bin/env python3

import re


def main():
    machines = []
    with open("input.txt", "r") as fobj:
        for m in fobj.read().split("\n\n"):
            machines.append(list(map(int, re.findall(r"\d+", m))))
    for error in (0, 10_000_000_000_000):
        tokens = 0
        for ax, ay, bx, by, X, Y in machines:
            X, Y = X + error, Y + error
            # luckily, none of the inputs seem to be linearly dependent
            det = ax * by - bx * ay
            A, Ar = divmod(by * X - bx * Y, det)
            B, Br = divmod(-ay * X + ax * Y, det)
            if Ar or Br:
                continue
            tokens += 3 * A + B
        print(tokens)


if __name__ == "__main__":
    main()
