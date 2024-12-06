#!/usr/bin/env python3

import re


def main():
    games = []
    with open("input.txt", "r") as fobj:
        for line in fobj:
            win = set(map(int, re.findall(r"\d+", line.split(":")[1].split("|")[0])))
            mynums = set(map(int, re.findall(r"\d+", line.split("|")[1])))
            games.append((win, mynums))
    print(sum(int(2 ** (len(game[0] & game[1]) - 1)) for game in games))

    matching = [len(game[0] & game[1]) for game in games]
    instances = [1] * len(games)
    for i, match in enumerate(matching):
        for j in range(match):
            instances[i + 1 + j] += instances[i]
    print(sum(instances))


if __name__ == "__main__":
    main()
