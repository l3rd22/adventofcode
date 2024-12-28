#!/usr/bin/env python3


def main() -> None:
    with open("input.txt", "r") as fobj:
        schematics = fobj.read().split("\n\n")
    keys = set()
    locks = set()
    for scm in schematics:
        profile = tuple(scm[i::6].count("#") - 1 for i in range(5))
        if scm.startswith("#"):
            locks.add(profile)
        else:
            keys.add(profile)
    print(
        sum(all(l + k < 6 for l, k in zip(lock, key)) for lock in locks for key in keys)
    )


if __name__ == "__main__":
    main()
