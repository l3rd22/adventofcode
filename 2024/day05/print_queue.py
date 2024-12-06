#!/usr/bin/env python3

from functools import cmp_to_key


def main():
    with open("input.txt", "r") as fobj:
        rules = []
        for line in fobj:
            if line in ("\n", "\r\n"):
                break
            rules.append(tuple(map(int, line.split("|"))))
        updates = [list(map(int, line.split(","))) for line in fobj]
    precedes = {}
    for rule in rules:
        precedes.setdefault(rule[1], []).append(rule[0])
    correct_order = []
    for update in updates:
        correct = True
        for i, page in enumerate(update):
            for page_after in update[i + 1 :]:
                if page_after in precedes.get(page, []):
                    correct = False
                    break
            if not correct:
                break
        correct_order.append(correct)
    print(
        sum(
            update[len(update) // 2] if correct else 0
            for update, correct in zip(updates, correct_order)
        )
    )
    cmp = lambda item1, item2: 2 * (item2 in precedes.get(item1, [])) - 1
    updates = [
        update if correct else sorted(update, key=cmp_to_key(cmp))
        for update, correct in zip(updates, correct_order)
    ]
    print(
        sum(
            update[len(update) // 2] if not correct else 0
            for update, correct in zip(updates, correct_order)
        )
    )


if __name__ == "__main__":
    main()
