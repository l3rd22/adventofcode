#!/usr/bin/env python3


def main():
    games = []
    with open("input.txt", "r") as fobj:
        for line in fobj:
            winning, mynums = line.split("|")
            game, winning = winning.split(":")
            winning = set(
                map(int, [winning[i : i + 3] for i in range(0, len(winning) - 2, 3)])
            )
            mynums = set(
                map(int, [mynums[i : i + 3] for i in range(0, len(mynums) - 2, 3)])
            )
            games.append((winning, mynums))
    print(sum(int(2 ** (len(game[0] & game[1]) - 1)) for game in games))

    matching = [len(game[0] & game[1]) for game in games]
    instances = [1] * len(games)
    for i, match in enumerate(matching):
        for j in range(match):
            instances[i + 1 + j] += instances[i]
    print(sum(instances))


if __name__ == "__main__":
    main()
