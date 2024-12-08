#!/usr/bin/env python3

import re


def main():
    with open("input.txt", "r") as fobj:
        almanac = fobj.read().split("\n\n")
    seeds = list(map(int, re.findall(r"\d+", almanac[0])))
    maps = [
        [tuple(map(int, range_.split(" "))) for range_ in map_.rstrip().split("\n")[1:]]
        for map_ in almanac[1:]
    ]
    locations = []
    for seed in seeds:
        for map_ in maps:
            for range_ in map_:
                if seed >= range_[1] and seed < (range_[1] + range_[2]):
                    seed += range_[0] - range_[1]
                    break
        locations.append(seed)
    print(min(locations))

    seeds = [(s, s + rn) for s, rn in zip(seeds[::2], seeds[1::2])]
    maps = [{(ss, ss + rn): (ds, ds + rn) for ds, ss, rn in map_} for map_ in maps]
    for map_ in maps:
        dest = []
        for sr, dr in map_.items():
            remaining = []
            for seed in seeds:
                split = (
                    seed[0],
                    min(seed[1], max(seed[0], sr[0])),
                    max(seed[0], min(seed[1], sr[1])),
                    seed[1],
                )
                if split[0] < split[1]:
                    remaining.append(split[:2])
                if split[2] < split[3]:
                    remaining.append(split[2:])
                if split[1] < split[2]:
                    dest.append((split[1] + dr[0] - sr[0], split[2] + dr[1] - sr[1]))
            seeds = remaining
        seeds.extend(dest)
    print(min(seeds)[0])


if __name__ == "__main__":
    main()
