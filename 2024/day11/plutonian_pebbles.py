#!/usr/bin/env python3

from functools import cache
from collections import Counter


@cache
def blink(n):
    if n == 0:
        return (1,)
    if (len_n := len(str_n := str(n))) % 2 == 0:
        return (int(str_n[: len_n // 2]), int(str_n[len_n // 2 :]))
    return (n * 2024,)


def main():
    with open("input.txt", "r") as fobj:
        stone_count = Counter(map(int, fobj.readline().split(" ")))
    for i in range(75):
        new_count = Counter()
        for n, count in stone_count.items():
            new_count.update({n_: c_ * count for n_, c_ in Counter(blink(n)).items()})
        stone_count = new_count
        if i in (24, 74):
            print(sum(stone_count.values()))


if __name__ == "__main__":
    main()
