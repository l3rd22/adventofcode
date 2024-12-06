#!/usr/bin/env python3

from math import prod


def main():
    games = {}
    with open("input.txt", "r") as fobj:
        for line in fobj:
            game, subsets = line.rstrip().split(": ")
            games[int(game[5:])] = [
                {
                    cubes.split(" ")[1]: int(cubes.split(" ")[0])
                    for cubes in subset.split(", ")
                }
                for subset in subsets.split("; ")
            ]
    print(
        sum(
            (
                id_
                if not any(
                    [
                        cubes.get(color, 0) > maxnum
                        for cubes in subsets
                        for maxnum, color in (
                            (12, "red"),
                            (13, "green"),
                            (14, "blue"),
                        )
                    ]
                )
                else 0
            )
            for id_, subsets in games.items()
        )
    )
    print(
        sum(
            prod(
                max([cubes.get(color, 0) for cubes in subsets])
                for color in ("red", "green", "blue")
            )
            for subsets in games.values()
        )
    )


if __name__ == "__main__":
    main()
