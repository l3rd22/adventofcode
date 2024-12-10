#!/usr/bin/env python3


def dfs(r, c, height_map):
    if (h := height_map[r][c]) == 9:
        return [(r, c)]
    trailheads = []
    for rn, cn in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
        if rn < 0 or cn < 0:
            continue
        try:
            hn = height_map[rn][cn]
        except IndexError:
            continue
        if hn == h + 1:
            trailheads.extend(dfs(rn, cn, height_map))
    return trailheads


def main():
    with open("input.txt", "r") as fobj:
        height_map = [[int(h) for h in line.rstrip()] for line in fobj]
    total1 = 0
    total2 = 0
    for r in range(len(height_map)):
        for c in range(len(height_map[r])):
            if height_map[r][c] == 0:
                total1 += len(set(trailheads := dfs(r, c, height_map)))
                total2 += len(trailheads)
    print(total1)
    print(total2)


if __name__ == "__main__":
    main()
