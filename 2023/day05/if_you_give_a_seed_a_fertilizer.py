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


if __name__ == "__main__":
    main()
