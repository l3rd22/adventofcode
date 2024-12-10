#!/usr/bin/env python3

from collections import Counter


dct = {
    "T": "a",
    "J": "b",
    "Q": "c",
    "K": "d",
    "A": "e",
}


def apply_jokers(count):
    j = count.pop(".", 0)
    if j == 5:
        return {".": j}
    k = max(count, key=count.get)
    count[k] += j
    return count


def main():
    hands = []
    bets = []
    with open("example_input.txt", "r") as fobj:
        for line in fobj:
            hand, bet = line.rstrip().split(" ")
            for k, v in dct.items():
                hand = hand.replace(k, v)
            hands.append(hand)
            bets.append(int(bet))
    types = [tuple(sorted(Counter(hand).values(), reverse=True)) for hand in hands]
    game = sorted(zip(types, hands, bets), key=lambda x: x[:2])
    print(sum((i + 1) * g[2] for i, g in enumerate(game)))

    hands = [hand.replace("b", ".") for hand in hands]
    types = [
        tuple(sorted(apply_jokers(Counter(hand)).values(), reverse=True))
        for hand in hands
    ]
    game = sorted(zip(types, hands, bets), key=lambda x: x[:2])
    print(sum((i + 1) * g[2] for i, g in enumerate(game)))


if __name__ == "__main__":
    main()
