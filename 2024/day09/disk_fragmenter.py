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


if __name__ == "__main__":
    main()
