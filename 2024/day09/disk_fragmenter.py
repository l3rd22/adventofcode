#!/usr/bin/env python3


def main():
    with open("input.txt", "r") as fobj:
        disk_map = fobj.read().rstrip()
    file_blocks = (i for i, f in enumerate(disk_map[::2]) for _ in range(int(f)))
    file_blocks_r = (
        len(disk_map) // 2 - i
        for i, f in enumerate(disk_map[::-2])
        for _ in range(int(f))
    )
    free = (i % 2 == 1 for i, f in enumerate(disk_map) for _ in range(int(f)))
    num_file_blocks = sum(map(int, disk_map[::2]))
    print(
        sum(
            i * next((file_blocks, file_blocks_r)[next(free)])
            for i in range(num_file_blocks)
        )
    )

    files = [
        (sum(int(k) for k in disk_map[: 2 * i]), int(f), i)
        for i, f in enumerate(disk_map[::2])
    ]
    empty = [
        (sum(int(k) for k in disk_map[: 2 * i + 1]), int(f))
        for i, f in enumerate(disk_map[1::2])
    ]
    for i, f in enumerate(files[::-1]):
        for j, e in enumerate(empty):
            if e[0] >= f[0]:
                break
            if e[1] > f[1]:
                files[-(i + 1)] = (e[0], *f[1:])
                empty[j] = (e[0] + f[1], e[1] - f[1])
                break
            if e[1] == f[1]:
                files[-(i + 1)] = (e[0], *f[1:])
                empty.pop(j)
                break
    print(sum(f[2] * (f[0] * f[1] + (f[1] * (f[1] - 1)) // 2) for f in files))


if __name__ == "__main__":
    main()
