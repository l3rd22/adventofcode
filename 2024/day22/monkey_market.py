#!/usr/bin/env python3


def evolve(secret_num):
    secret_num = (secret_num ^ secret_num << 6) & ((1 << 24) - 1)
    secret_num = (secret_num ^ secret_num >> 5) & ((1 << 24) - 1)
    secret_num = (secret_num ^ secret_num << 11) & ((1 << 24) - 1)
    return secret_num


def main() -> None:
    with open("input.txt") as fobj:
        secret_nums = map(int, fobj.readlines())
    total = 0
    for secret_num in secret_nums:
        for _ in range(2000):
            secret_num = evolve(secret_num)
        total += secret_num
    print(total)


if __name__ == "__main__":
    main()
